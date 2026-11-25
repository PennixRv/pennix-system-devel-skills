---
name: bitbake-debug
description: 解释一次 Yocto/OpenEmbedded BitBake 构建为何失败、报 QA 错误或成功后仍缺包；从任务日志、运行脚本和实际工件取证。若请求是编写配方或查明某个 append 是否匹配，先看配方选择与元数据。
---

# BitBake 排错

确认目标 release、recipe、image、机器、失败任务和工作目录。没有失败且问题是最终镜像缺包时，直接读[镜像缺包](references/image-rootfs.md)，不要先重跑 `do_rootfs`。

1. **从首个失败开始。** 使用对应 `log.do_*`、`run.do_*` 及已有配置，区分解析、fetch、patch、configure、compile、install、package/QA、rootfs 和 image。定位执行的具体命令、错误发生前的状态和输出归属，不以 BitBake 最后一行替代根因。
2. **核对生效上下文。** 确认配方提供者、实际版本、任务使用的宿主工具或目标 sysroot 以及值的来源。`bitbake -e` 可以暴露完整环境且解析可执行项目代码；优先使用已过滤的可分享证据，未获准不自行运行解析、任务或 `devshell`。
3. **选能区分原因的最小验证。** 先用已有证据解释能确定的部分，再说明缺少哪个日志片段或工件。需要执行验证时，使用已获准且与问题匹配的构建环境，并核对影响范围。不要默认强制重跑、清共享缓存、关闭 QA、修改配方或上传日志。

报告失败阶段、可核对证据、最小改动或验证建议和未执行项。诊断入口按目标版 [Yocto 调试手册](https://docs.yoctoproject.org/dev/dev-manual/debugging.html)核对。
