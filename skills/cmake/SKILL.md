---
name: cmake
description: 实现、审查或诊断 CMake 工程的目标接口、preset、生成器、工具链、缓存与构建目录。适用于含 CMakeLists.txt 或实际使用 CMake 的 C/C++ 工程，不把 Meson、手写 Make 或 BitBake 当作 CMake。
---

# CMake 工程

从真实命令、preset 与项目声明核对 CMake 最低版本、源目录、构建目录、生成器和编译器身份。拿不出这些证据时不猜测默认值，也不通过重新配置抹去旧证据。

1. **从消费目标出发。** 用目标属性解释 include、编译定义和链接依赖，按下游是否需要区分 `PRIVATE`、`PUBLIC`、`INTERFACE`。先检查导入目标、传递依赖和已有包契约，不优先加全局标志或新下载。
2. **从 preset 跟到实际缓存。** 区分 configure、build、test preset、继承和手工参数，核对它们选中的同一 `binaryDir`。生成器、工具链或编译器已写入旧构建目录时，不以另一个目录的值解释现场；若确需换工具链，保留旧工件并在获准的新目录验证。
3. **确认问题属于哪一步。** configure 完成不等于目标已构建，构建完成不等于测试已发现或执行。交叉构建时先确认宿主工具、目标依赖和可执行器。Ninja 的增量问题，用生成图解释上游 CMake 输入，不直接编辑 `build.ninja`；按需读[生成图取证](references/generated-graph.md)。
4. **只在已获准的目标工程中运行。** configure 本身可能执行项目代码；不自动下载依赖、安装、迁移生成器或升最低版本。给出最小变更、消费方影响、预期验证和实际已执行项。

工具链细节查对应版本的 [CMake Toolchains](https://cmake.org/cmake/help/latest/manual/cmake-toolchains.7.html)，不要套用示例项目的标准、flags 或 preset 版次。
