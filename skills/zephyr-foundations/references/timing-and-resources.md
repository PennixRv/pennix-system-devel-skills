# Zephyr 时序与资源证据

- **先匹配环境。** 明确板卡、修订、构建域、最终 `.config` 和测量工件；`sysbuild` 各域分别看其 ELF 或 map。先确认时钟来源、单位、分辨率、频率变化与观测开销。能用同一时间线匹配事件时，分开中断入口至提交、工作项排队、线程开始和完成；单有 handler 执行时长不能说明端到端时限。
- **匹配观测与问题。** Timing Functions 测所包围的代码段；Thread Analyzer 给已观测线程的栈或运行统计，不等于请求尾延迟或 ISR 栈余量。若目标版本提供 Zephyr shell 的 `perf`，它不是 Linux `perf`；用对应应用域及构建的 ELF 解释采样地址，不用 boot 域符号推断热点。
- **分开映像占用、运行用量与预算。** 从该域匹配的 map、RAM／ROM 报告读取节和符号，区分静态分配、保留空间和实际运行峰值。核对线程栈与中断栈是否分别有证据；仅有短暂常规负载的 `native_sim` 高水位，不能给出目标板、错误路径或嵌套中断的余量结论。

按目标版本查 [Timing Functions](https://docs.zephyrproject.org/latest/kernel/timing_functions/index.html)、[Thread Analyzer](https://docs.zephyrproject.org/latest/services/debugging/thread-analyzer.html)、[Footprint](https://docs.zephyrproject.org/latest/develop/optimizations/footprint.html) 和 [Zephyr `perf`](https://docs.zephyrproject.org/latest/services/profiling/perf.html)。先说明缺项和可区分解释的最小记录；不开启真实板卡上的采集或刷写。
