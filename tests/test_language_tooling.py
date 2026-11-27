"""Small real compiler fixtures; these do not imply target or schedule coverage."""

from pathlib import Path
import shutil
import subprocess
import tempfile
import unittest


def run(*command, cwd=None):
    return subprocess.run(command, cwd=cwd, capture_output=True, text=True, timeout=30)


class LanguageToolingTests(unittest.TestCase):
    def setUp(self):
        scratch = tempfile.TemporaryDirectory(prefix="language-tools-")
        self.addCleanup(scratch.cleanup)
        self.root = Path(scratch.name)

    def success(self, *command):
        result = run(*command, cwd=self.root)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        return result.stdout

    @unittest.skipUnless(shutil.which("cc"), "requires a native C compiler")
    def test_c17_unaligned_source_and_failure_preserves_output(self):
        (self.root / "example.c").write_text(r"""
#include <assert.h>
#include <stddef.h>
#include <limits.h>
_Static_assert(CHAR_BIT == 8, "the wire format uses octets");
static int decode(const unsigned char *p, size_t n, unsigned *out) {
    if (n < 2) return 0;
    *out = ((unsigned)p[0] << 8) | (unsigned)p[1];
    return 1;
}
int main(void) {
    _Alignas(unsigned) unsigned char packet[] = {0, 0x12, 0x34};
    unsigned out = 7;
    assert(!decode(packet + 1, 1, &out) && out == 7);
    assert(decode(packet + 1, 2, &out) && out == 0x1234);
}
""")
        self.success("cc", "-std=c17", "-Wall", "-Wextra", "-Werror", "example.c", "-o", "fixture")
        self.success("./fixture")

    @unittest.skipUnless(shutil.which("c++"), "requires a native C++ compiler")
    def test_cpp17_last_read_precedes_release_for_reuse(self):
        (self.root / "example.cpp").write_text(r"""
#include <atomic>
#include <cassert>
#include <thread>
int main() {
    std::atomic<bool> full{false};
    unsigned slot = 0;
    constexpr unsigned total = 512;
    std::thread consumer([&] {
        for (unsigned n = 1; n <= total; ++n) {
            while (!full.load(std::memory_order_acquire)) std::this_thread::yield();
            const unsigned &borrow = slot;
            assert(borrow == n);
            full.store(false, std::memory_order_release);
        }
    });
    for (unsigned n = 1; n <= total; ++n) {
        while (full.load(std::memory_order_acquire)) std::this_thread::yield();
        slot = n;
        full.store(true, std::memory_order_release);
    }
    consumer.join();
}
""")
        self.success("c++", "-std=c++17", "-O2", "-pthread", "example.cpp", "-o", "fixture")
        self.success("./fixture")

    @unittest.skipUnless(all(shutil.which(tool) for tool in ("clang-tidy", "cmake", "ninja", "cc")),
                         "requires clang-tidy and the native CMake/Ninja toolchain")
    def test_clang_tidy_uses_the_selected_compilation_database(self):
        (self.root / "CMakeLists.txt").write_text("""
cmake_minimum_required(VERSION 3.20)
project(probe C)
add_library(probe OBJECT example.c)
option(BOARD_WIDE "Select the alternate test configuration" OFF)
if(BOARD_WIDE)
  target_compile_definitions(probe PRIVATE BOARD_WIDE)
endif()
""")
        (self.root / "example.c").write_text("""
int f(int x) {
#ifdef BOARD_WIDE
    if (x)
        return 1;
#else
    if (x) {
        return 1;
    }
#endif
    return 0;
}
""")
        checker = "readability-braces-around-statements"
        for label, switch in (("host", "OFF"), ("target", "ON")):
            self.success("cmake", "-G", "Ninja", "-S", ".", "-B", label,
                         "-DCMAKE_EXPORT_COMPILE_COMMANDS=ON", f"-DBOARD_WIDE={switch}")
            self.success("cmake", "--build", label)
            result = run("clang-tidy", "-p", label, f"--checks=-*,{checker}",
                         "--warnings-as-errors=*", "example.c", cwd=self.root)
            output = result.stdout + result.stderr
            self.assertNotIn("clang-diagnostic-error", output)
            if switch == "ON":
                self.assertNotEqual(result.returncode, 0, output)
                self.assertIn(checker, output)
            else:
                self.assertEqual(result.returncode, 0, output)
                self.assertNotIn(checker, output)
