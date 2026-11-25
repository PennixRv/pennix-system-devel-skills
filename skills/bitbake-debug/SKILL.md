---
name: bitbake-debug
description: 排查 Yocto/OpenEmbedded BitBake 构建任务失败、QA 报错或构建通过但镜像缺包，从日志、运行脚本、版本和实际工件取证。不默认重跑任务、输出完整环境或修改层。
---

# BitBake 排错

确认目标 release、recipe、image、机器、失败任务和工作目录。没有失败且问题是最终镜像缺包时，直接读[镜像缺包](references/image-rootfs.md)，不要先重跑 `do_rootfs`。

1. **从首个失败开始。** 使用对应 `log.do_*`、`run.do_*` 及已有配置，区分解析、fetch、patch、configure、compile、install、package/QA、rootfs 和 image。定位执行的具体命令、错误发生前的状态和输出归属，不以 BitBake 最后一行替代根因。
2. **核对生效上下文。** 确认配方提供者、实际版本、任务使用的宿主工具或目标 sysroot 以及值的来源。`bitbake -e` 可以暴露完整环境且解析可执行项目代码；优先使用已过滤的可分享证据，未获准不自行运行解析、任务或 `devshell`。
3. **提出只改变一个判断的验证。** 缺任务日志或目标身份就索取相应最小片段；不要默认强制重跑、清共享缓存、关闭 QA、修改配方或上传日志。实际运行只在匹配且获准的隔离环境进行。

报告失败阶段、可核对证据、最小改动或验证建议和未执行项。诊断入口按目标版 [Yocto 调试手册](https://docs.yoctoproject.org/dev/dev-manual/debugging.html)核对。
