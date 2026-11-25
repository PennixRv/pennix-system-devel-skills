---
name: zephyr-foundations
description: 设计、实现、审查或排查 Zephyr 的设备、构建域、Devicetree、Kconfig、线程和中断；也用于核对 Zephyr 的时序、栈、RAM 或 Flash 报告，以及由 Zephyr 串口 shell 采集的 perf record。仅有 GDB 工件身份问题时不优先查平台。
---

# Zephyr 开发基础

本文件根据 `beriberikix/zephyr-agent-skills` 的 `zephyr-foundations` 修改，收窄了平台和验证条件，并移除了默认扫描和模板入口。

先确认实际 Zephyr 版本、目标板及修订、应用目录和构建域；按问题核对已有 `west`/CMake 参数、生成文件或日志，不默认某厂商 SDK、`build/` 路径、板卡或单域。

按问题选择检查项，不必逐一执行：

1. **区分硬件描述和软件启用。** 用目标板、DTS binding、活动 overlay 与生成后的 DTS 解释硬件；另用最终 Kconfig 和构建规则证明驱动或功能编入。对设备实例、设备树序号、GPIO/I2C/SPI 或 `CONFIG_*` 未带入，读[设备与配置证据](references/device-and-config.md)。
2. **确认设备、所有权和执行上下文。** 区分配置常量和每个实例的运行状态、设备就绪和本次 API 调用成功。涉及 ISR 转交工作队列或驱动停止时，读[设备与配置证据](references/device-and-config.md)的工作项部分，检查生产者、调用上下文和资源的最后使用。
3. **核对时序与资源。** 分析中断到线程或工作项的时延、栈余量、映像占用或 Zephyr shell `perf` 时，直接读[时序与资源证据](references/timing-and-resources.md)；仅在确实涉及设备或功能配置时才补查对应参考。

输出板卡和构建域、与问题有关的配置、设备路径或测量证据，以及结论或最小改动。分开报告静态结论、构建、模拟和板卡运行。获准构建或测试时使用匹配目标域的项目入口并保留现有工件；没有真机不阻断静态取证，也不默认下载模块、刷写或使用硬件探针。参考中的例子不代替实际 binding，也不以正则检查作为语义或运行验收。
