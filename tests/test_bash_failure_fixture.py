import shutil
import subprocess
import tempfile
import unittest
from pathlib import Path


@unittest.skipUnless(shutil.which("bash"), "Bash interpreter unavailable")
class BashFailureFixtureTests(unittest.TestCase):
    def run_fixture(self, script):
        with tempfile.TemporaryDirectory() as directory:
            result = subprocess.run(
                ["bash", "--noprofile", "--norc", "-c", script],
                cwd=directory,
                env={"PATH": "/usr/bin:/bin"},
                capture_output=True,
                text=True,
                timeout=10,
            )
            self.assertEqual(result.returncode, 0, result.stderr)
            return result.stdout.splitlines()

    def test_conditional_pipeline_preserves_artifact_only_when_guarded(self):
        result = self.run_fixture(r"""
set -e
printf 'old\n' > final
producer() { printf '%s\n' "$1"; return "$2"; }
wrong() { producer partial 7 | cat > stage; mv stage final; }
publish() (
    set -o pipefail
    trap 'rc=$?; rm -f -- stage; exit "$rc"' EXIT
    if producer "$@" | cat > stage; then
        mv stage final
    else
        return "$?"
    fi
)
report() {
    if "$@"; then rc=0; else rc=$?; fi
    test ! -e stage
    printf '%s:%s\n' "$rc" "$(cat final)"
}
report wrong
printf 'old\n' > final
report publish partial 7
report publish complete 0
report publish complete 0
""")
        self.assertEqual(result, ["0:partial", "7:old", "0:complete", "0:complete"])

    def test_declaration_can_mask_command_substitution(self):
        result = self.run_fixture(r"""
producer() { printf partial; return 7; }
masked() { local value=$(producer); printf '%s\n' "$?"; }
checked() {
    local value
    if value=$(producer); then
        printf 'unexpected\n'
    else
        printf '%s\n' "$?"
    fi
}
masked
checked
""")
        self.assertEqual(result, ["0", "7"])

    def test_early_consumer_exit_is_visible_in_pipeline_status(self):
        result = self.run_fixture(r"""
set -o pipefail
yes | head -n 1
printf '%s,%s,%s\n' "$?" "${PIPESTATUS[0]}" "${PIPESTATUS[1]}"
""")
        self.assertEqual(result, ["y", "141,141,0"])
