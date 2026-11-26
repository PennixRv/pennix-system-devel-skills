---
name: meson
description: 实现、审查或诊断 Meson 的目标、选项、机器文件、依赖解析和测试执行器。用于问题由实际 Meson 配置或生成决定时；已证明是宿主库混入或 ELF 装载失败时不接管。
---

# Meson 配置与执行

先固定 Meson 版本、源目录、构建目录和实际 `setup` 参数。分清项目声明、机器文件和构建目录中已生效的配置；改了文件不等于已有构建目录随之更新。

1. **确认要构建哪一个目标。** 查 `meson.build` 中的目标及消费关系、项目选项和 `dependency()` 的来源。外部依赖、fallback 子项目和可在构建机执行的生成器承担不同职责；先证明已选中谁，不默认下载 wrap、启用 fallback 或迁移项目。
2. **对照机器和执行能力。** build machine 执行生成器和构建工具，host machine 运行产物；只有开发编译器等工具时通常还需单独考虑 target machine。机器文件、实际编译器和目标 ELF 要对上。项目已有受支持的 `exe_wrapper` 或实机时，仍须证明测试真的运行；仅生成、构建或标为跳过不算执行。
3. **修所属层并复核。** 用项目块、机器文件、有效选项和已有 Meson 日志说明最小修改。生成的 `build.ninja` 可用来定位最终命令、缺依赖边和增量差异，不直接编辑它。配置和测试会运行代码；只在获准环境按项目最小入口验证，不为了清状态直接 wipe。

报告生效配置、目标和依赖来源、构建与执行分别的证据，以及尚缺的运行条件。按目标版本查 [Meson 交叉编译](https://mesonbuild.com/Cross-compilation.html)和 [Wrap 依赖机制](https://mesonbuild.com/Wrap-dependency-system-manual.html)。
