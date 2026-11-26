---
name: linux-kernel-testing
description: 为 Linux 内核内部行为、用户态接口或内存序选择和设计验证，判读 KUnit、kselftest、LTP、LKMM 的配置、执行和结果。仅审查指定补丁、仅查驱动绑定或 Kconfig 值时不接管。
---

# Linux 内核验证

先定要证明的行为、所用内核提交及配置、运行目标和可观察输出。不要因为同一次改动需要两种证据就把它们合为一个通过条件。

1. **按断言选范围。** 小范围内核内部契约优先考虑 KUnit；用户态可见接口或已有子系统 harness 优先看 kselftest，跨版本系统接口回归可沿已有 LTP；内存序允许或禁止的结果可用 LKMM 对照。各自不能代替真实设备、生命周期的动态验证或完整的并发正确性证明。
2. **让失败对照有意义。** 用公开可观察结果或稳定的内部不变量验证边界和回退；测试先过滤到受影响子系统。核对测试已启用、已编译、已被选择及实际执行，读取 KTAP/TAP 或项目的独立运行结果；跳过、环境不支持与失败分开报告。
3. **匹配执行目标。** 隔离 guest 用于其内核、配置和设备模型能表达的断言，QEMU 设备模型的验证不等于 guest 内核回归。真实驱动依赖未建模硬件、权限或厂商行为时，给出剩余证据，不默认启动宿主模块、改内核或占用设备。

输出断言与测试入口对应、配置和环境、结果与未验证项。对照 [内核测试总览](https://docs.kernel.org/dev-tools/testing-overview.html) 和 [LKMM 文档](https://docs.kernel.org/dev-tools/lkmm/index.html)。涉及 QEMU 模型本身时另看 [QTest](https://www.qemu.org/docs/master/devel/testing/qtest.html) 支持的设备验证层。
