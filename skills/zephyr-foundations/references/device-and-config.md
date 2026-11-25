# Zephyr 设备与配置证据

- **Kconfig：** 区分 `Kconfig` 中声明符号、应用和板级 `.conf` 请求值，以及目标域 `.config` 的实际取值。查符号可见性、依赖、choice 和合并日志。Devicetree `.overlay` 不是 Kconfig `.conf`；若使用 Devicetree 派生条件，分别证明两侧配置及相应的桥接规则。`traceconfig` 是否可用、是否应在干净构建目录运行，按目标版本核验。
- **设备树与实例：** 确定生效节点、`compatible`、绑定、状态、总线和依赖。遇到 `__device_dts_ord_*` 链接错误，先在出错域的生成头文件中用序号定位节点，再查该域的 DTS、编译规则和实例定义。拿到设备引用不等于 `device_is_ready()` 成立；设备就绪也不等于后续 I/O 成功。
- **工作项的交接和停止：** 找出哪些 ISR、线程或回调仍会提交或重新排队。核对取消接口是否等待当前处理函数结束、能从什么上下文调用；在停止新提交且确认最后一次使用后，再回收承载工作项或处理函数访问的资源。不要用某一时刻的忙闲状态证明释放安全。按目标版 [Zephyr 工作队列](https://docs.zephyrproject.org/latest/kernel/services/threads/workqueue.html)核对。
- **运行与测试：** 针对目标域选择构建或测试。Twister 发现了用例、场景标为仅构建、由模拟器运行和由板卡运行是不同证据；未验证依赖或时序时不能外推。

入口：[Zephyr Kconfig 值追踪](https://docs.zephyrproject.org/latest/build/kconfig/tracing.html)、[Devicetree 排错](https://docs.zephyrproject.org/latest/build/dts/troubleshooting.html)、[Twister](https://docs.zephyrproject.org/latest/develop/test/twister.html)。阅读与目标版本一致的文档。
