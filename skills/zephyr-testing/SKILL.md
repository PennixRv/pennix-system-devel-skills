---
name: zephyr-testing
description: 设计或判读 Zephyr 的 Ztest/Twister 测试，区分案例选择、过滤、仅构建、宿主或模型运行与实板结果。仅追查域配置、Devicetree 或 GDB 符号身份时不接管。
---

# Zephyr 测试与运行证据

先核对版本、案例定义、实际 Twister 调用、板名及限定符、构建域、执行器和测试输出。测试名相同不说明跑的是同一个目标或镜像。

1. **明确断言与被测层。** 无硬件契约的逻辑可考虑现有单元测试或 `native_sim`；Zephyr 应用和内核交互可在支持的宿主或模型上验证；真实外设响应、板级时序等需要相应目标证据。`native_sim` 不模拟某一具体板卡，模型标称支持设备名称也不代表涵盖所需行为。
2. **追踪从选择到结果。** 查案例定义与过滤原因、目标有效配置、构建及 runner/harness 的实际执行日志。构建成功、仅构建、跳过、超时和通过要分开；不能用总表或 ELF 存在替代对应案例和运行环境的证据。
3. **用最小匹配环境补证。** 复用项目已有 Ztest/Twister、设备模拟或实板通道；对特殊模型读[平台覆盖判据](references/platform-evidence.md)。没有授权不下载依赖、改硬件映射、刷写、连串口或占用设备。

输出案例、目标/域、选择—构建—运行的证据链与下一步。以目标版本的 [Zephyr 测试文档](https://docs.zephyrproject.org/latest/develop/test/index.html)和匹配 runner 为准。
