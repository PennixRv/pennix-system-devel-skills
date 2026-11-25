# 二版编写审查评测

复用 `cases.json`。A 使用完整二版 `aaa0263d5172de11a5a5efab2b57916e9e357cc9`，B 使用完整修订候选；保持其他集合、模型、权限和输入一致，不向被测会话提供判据。先验 A/B 的 `v2-offcpu`，其余只跑 B；`v2-build-holdout` 不参与文案调整。

| 场景 | 应成功读取 | 可按需补读或不应读取 |
| --- | --- | --- |
| `v2-offcpu`（A、B） | `systems-performance` 和 `linux-evidence.md` | 仅有调度时间线，无 Linux `perf` 产物或工具问题，不读 `linux-perf`；本例无须基准或热点优化参考。 |
| `v2-perf-valid`、`perf-blocked` | `linux-perf` | 可用其 `evidence.md` 核对范围、复用和权限；不读通用性能或 Zephyr 入口，不发起采集。 |
| `v2-zephyr-perf`、`v2-zephyr-footprint` | `zephyr-foundations` 和 `timing-and-resources.md` | 不读 Linux `perf`、通用性能或设备配置参考；区分 app/boot 域及模拟与板级证据。 |
| `mixed-zephyr-gdb` | `gdb` | 给定证据已经定位 Build ID 错配，不必读 Zephyr、交叉工具链或性能入口。 |
| `driver-config-only` | `linux-driver-lifecycle` 和 `kconfig-values.md` | 仅取证配置，不要求查驱动实现或读内核补丁审查、Yocto、Zephyr 入口。 |
| `driver-unbind` | `linux-driver-lifecycle` | 直接核对发布与异步停止次序，不读配置参考或补丁审查入口。 |
| `mixed-yocto-kconfig` | `yocto-recipe-development` 和 `layer-and-recipe.md` | 已足以确认 append 与 provider 错配；缺最终 `.config`，此时不先读 Linux 驱动与 Kconfig 参考。 |
| `v2-build-holdout` | `make` | 不读运行性能入口，不运行构建。 |

`control` 是用例分组，不代表一律不触发。查看成功读取的路径和实际内容；仅列出文件、目录或可用 Skill 不算读取。工具错误、宿主中断或证据缺失不算负例通过。另按原判据检查工程结论和禁止操作；回答正确不能抵消错误加载，加载正确也不能抵消错误结论。仅在有具体修订时重测失败项和相邻对照，不从多次采样中挑选最好结果。
