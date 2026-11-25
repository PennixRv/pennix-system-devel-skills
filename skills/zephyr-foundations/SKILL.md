---
name: zephyr-foundations
description: 设计、实现或诊断 Zephyr 应用与驱动基础，核对板卡、构建域、Devicetree、最终 Kconfig、设备实例和线程/中断上下文。适用于 Zephyr 或明确采用 Zephyr 的 SDK，不用于把 Linux Kconfig 或其他 RTOS API 套到目标项目。
---

# Zephyr 开发基础

本文件根据 `beriberikix/zephyr-agent-skills` 的 `zephyr-foundations` 修改，收窄了平台和验证条件，并移除了默认扫描和模板入口。

先确认实际 Zephyr 版本、工作区、目标板及修订、应用目录和构建域。看已有 `west`/CMake 参数、生成文件和日志，不默认某厂商 SDK、`build/` 路径、板卡或单域。

1. **区分硬件描述和软件启用。** 用目标板、DTS binding、活动 overlay 与生成后的 DTS 解释硬件；另用最终 Kconfig 和构建规则证明驱动或功能编入。对设备实例、设备树序号、GPIO/I2C/SPI 或 `CONFIG_*` 未带入，读[设备与配置证据](references/device-and-config.md)。
2. **确认设备、所有权和执行上下文。** 区分配置常量和每个实例的运行状态；辨认设备就绪与实际 API 是否成功。使用 Zephyr 宏时按实际位宽、容器类型及数组契约判断。线程、ISR 与工作队列能否等待或调用某接口取决于目标 API；共享状态不凭 `volatile` 或错误码形态判断安全。
3. **验证范围与结果。** 区分静态、仅构建、模拟和真实板卡；Twister 计划中的平台、模拟后端和设备测试结果分开。无目标执行条件时清楚报未运行，不默认构建、下载模块、刷写或使用硬件探针。

输出板卡和域、实际配置及设备路径、具体变更和验证限度。参考中的设备示例不代替实际 binding，也不以正则检查作为语义或运行验收。
