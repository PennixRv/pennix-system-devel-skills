# 二版性能行为评测

逐例输入与判据仍在 `cases.json`。其他集合、工具、模型和提示固定：A 侧使用完整首版 `773ba4e35aaa01d32c3e259f6cb1162c02d11906`，B 侧使用完整二版候选。两个会话均不能读取私有判据、另一个会话或真实项目。先校验一对的可观测性，再展开；只将渲染后的假设输入交给被测会话。

| 分组 | 用例 ID |
| --- | --- |
| B 性能与平台正例和对照（12） | `v2-compare-design`、`v2-tail-tradeoff`、`v2-offcpu`、`v2-linux-irq`、`v2-hot-copy`、`v2-compiler-remark`、`v2-script-cost`、`v2-firmware-irq`、`v2-zephyr-footprint`、`v2-zephyr-perf`、`v2-perf-valid`、`perf-blocked` |
| B 相邻对照（4） | `cpp-runner-present`、`mixed-yocto-kconfig`、`mixed-zephyr-gdb`、`v2-build-holdout`（不参与描述调优，最后运行） |
| A 同题配对（4） | `v2-compare-design`、`v2-offcpu`、`v2-hot-copy`、`v2-firmware-irq` |

验收分别记录成功读取的入口与参考、对所给证据的判断、相邻或禁止操作，以及每个配对的具体增益、等价或退化。读路径不等于读正文；工具异常或宿主中断不能记为负例通过。对照数据没有证明运行实测或一般正确性的用途。定向重测最多 6 个，仅用于有具体修正的失败项和邻例。
