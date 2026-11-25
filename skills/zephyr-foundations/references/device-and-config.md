# Zephyr 设备与配置证据

- **Kconfig：** 区分 `Kconfig` 中声明符号、应用和板级 `.conf` 请求值，以及目标域 `.config` 的实际取值。查符号可见性、依赖、choice 和合并日志。Devicetree `.overlay` 不是 Kconfig `.conf`；若使用 Devicetree 派生条件，分别证明两侧配置及相应的桥接规则。`traceconfig` 是否可用、是否应在干净构建目录运行，按目标版本核验。
- **设备树与实例：** 确定生效节点、`compatible`、binding、状态、总线和依赖，区分节点存在、驱动编入、实例生成及设备就绪。遇到设备序号链接错误，先把序号指回实际节点和产生实例的驱动，不只改 overlay 或 Kconfig 一侧。
- **运行与测试：** 针对目标域选择构建或测试。Twister 发现了用例、场景标为仅构建、由模拟器运行和由板卡运行是不同证据；未验证依赖或时序时不能外推。

入口：[Zephyr Kconfig 值追踪](https://docs.zephyrproject.org/latest/build/kconfig/tracing.html)、[Devicetree 排错](https://docs.zephyrproject.org/latest/build/dts/troubleshooting.html)、[Twister](https://docs.zephyrproject.org/latest/develop/test/twister.html)。阅读与目标版本一致的文档。
