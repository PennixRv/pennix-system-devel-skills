# CMake 到 Ninja 的生成图取证

先通过实际构建目录、preset 和输入版本确定图身份。记录为何某个目标被判定脏、实际编译命令、缺失依赖或生成头文件的生产者；已有日志足够时不重新运行构建。

确认项目采用 Ninja 时，依版本和授权选择只读取现有图的入口，区分普通输入、顺序依赖、隐式依赖与验证目标。正确性修复回到 `target_sources()`、`target_link_libraries()` 或对应生成输入，不直接改生成文件。若生成器是 Meson，则按它的输入查证，不修改 CMake 入口。详见 [Ninja 手册](https://ninja-build.org/manual.html)。
