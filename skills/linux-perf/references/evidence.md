# 性能证据边界

- **事件口径。** 同名事件在不同 CPU、内核或修饰符下不必等价；核对用户态／内核态、线程／进程／CPU、采集窗口与采集的有效工作量。权限失败、`<not supported>` 和 `<not counted>` 不产生可解释的零值。未记录适用的缓存类事件不影响已匹配的 cycles 样本作为局部热点线索，但不能据此断言缓存根因。
- **计数器复用。** 有运行时间和启用时间时，查看实际运行占比、是否缩放，以及几项事件是否覆盖同一阶段。占比低且负载分阶段变化时，缩放结果可能不代表整个窗口，直接计算比率可能失真。必要时在获准条件下缩小事件集合或选择能同时调度的事件，不规定统一占比门槛。
- **采样和归因。** 确认采样事件、样本或周期权重、目标线程和回溯方式；注明丢样、截断和未知帧。按实际工件及可用 Build ID 核对符号，不用另一份名字相同的二进制补符号。分开自身和含子调用的样本占比，不把 cycles 压力、缓存事件与端到端时间混为一体。

权限或平台受限时，先说明哪些观察仍成立及缺项；可用已有应用时间、日志或获准的进程级证据，不提权或更改系统设置。计数与采样选项按目标版本对照 Linux 源码中的 [`perf stat`](https://github.com/torvalds/linux/blob/master/tools/perf/Documentation/perf-stat.txt) 和 [`perf report`](https://github.com/torvalds/linux/blob/master/tools/perf/Documentation/perf-report.txt)。
