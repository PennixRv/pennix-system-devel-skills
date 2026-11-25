# 交叉配置的来源

- **GCC / Clang：** 核对编译器实际报告及命令行目标，Clang 还需看目标参数和所选链接器、运行库。不要根据主机运行一个名称就判断产物 ABI。
- **CMake：** 从 toolchain file、preset、缓存和生成命令查证。目标 `find_*` 搜索范围与构建机器需要运行的程序可不同。参见 [CMake Toolchains](https://cmake.org/cmake/help/latest/manual/cmake-toolchains.7.html)。
- **Meson：** 从实际 cross file、各机器声明和项目选项查证。测试或探测是否运行取决于目标可执行性与配置的执行包装器；不默认安装包装器。参见 [Meson Cross Compilation](https://mesonbuild.com/Cross-compilation.html)。
- **Yocto SDK：** 从已安装 SDK 的项目版本、环境脚本、宿主/目标 sysroot 和目标镜像核对。SDK 的库与目标设备实际部署的库可能不同；不将 SDK 安装或设备验证作为取证前置。参见 [Yocto 标准 SDK](https://docs.yoctoproject.org/dev/sdk-manual/using.html)。
