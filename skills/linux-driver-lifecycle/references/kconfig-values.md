# Linux Kconfig 值追踪

先确认内核树提交、`ARCH`、实际构建目录和配置命令。区分符号定义、输入 `defconfig`／片段、最终 `.config` 与实际构建的工件；不能拿宿主内核的配置或不同目录的输出作证。

1. 查目标版本是否定义该符号，及其类型、提示可见性、`depends on`、`select`、`imply`、默认值及上层菜单条件。区分符号不存在、不允许自行赋值、依赖不满足和后来被其他输入覆盖。
2. 按实际构建入口确定配置来源、片段合并顺序、生成后的 `.config` 和 `CONFIG_MODULES`。`m` 和 `y` 的含义以及允许值取决于符号类型与当前配置；不能据某个文本片段认定驱动在镜像中。
3. 需要重新生成时先确认可信树与隔离输出位置。已有输入和构建结果能回答问题时不启动生成；缺文件时说明证据限度。不要手工编辑生成文件来掩盖源配置问题。

对照目标分支的 [Kconfig 语言](https://docs.kernel.org/kbuild/kconfig-language.html) 和 [配置目标](https://docs.kernel.org/next/kbuild/kconfig.html)。不用 Zephyr 的 `.conf`、`west` 或 Devicetree 规则解释 Linux 内核值。
