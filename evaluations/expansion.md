# 扩充与相邻路由评测

用 `case.py` 渲染 `cases.json`，不给被测会话评分内容。A 为完整旧集合，B 为完整候选，其他集合、模型、权限、合成输入和工具形态保持相同。宿主无网发现与模型行为分开验证。

| B 侧场景 | 必须实际成功读取的入口 | 不应以这些入口替代 |
| --- | --- | --- |
| `expand-link` | `native-linking` | ABI 或构建生成 |
| `expand-meson` | `meson` | 真实链接失败或既有 GoogleTest |
| `expand-runtime` | `c-cpp-runtime-diagnostics` | GDB 或普通 C++ 源码审查 |
| `expand-trace` | `linux-observability` | Linux perf 或泛化性能实验 |
| `expand-kernel-test` | `linux-kernel-testing` | 差异审查或驱动实现 |
| `expand-zephyr-test` | `zephyr-testing` | Zephyr 域配置 |
| `expand-startup` | `firmware-startup` | RTOS 运行期或用户态 ELF |
| `expand-uring` | `linux-async-io` | 通用服务或替代数据面 |
| `expand-old-abi`、`expand-old-cross`、`expand-old-gdb`、`expand-old-perf` | 分别 `elf-abi-compatibility`、`cross-toolchain`、`gdb`、`linux-perf` | 对应的新增入口不应被读取 |
| `expand-old-review`、`expand-old-zephyr`、`expand-old-embedded`、`expand-old-service` | 分别 `linux-kernel-review`、`zephyr-foundations`、`embedded-systems`、`linux-userspace-development` | 对应的新增入口不应被读取 |
| `v2-offcpu` | `systems-performance` 及 Linux 证据参考 | 不用追踪本身或 perf 计数器接管性能归因 |
| `v2-build-holdout` | `make` | 不用运行期入口，也不运行构建 |

仅 A/B 配对 `expand-old-abi` 和 `expand-zephyr-test`；A 的后者用于观察，答对不否定 B 的路由增益。B 的 18 个场景和 A 的 2 个场景共 20 个初测会话；`v2-build-holdout` 不参与文案调整。只为有边界的具体修订定向复测，至多 4 个会话；含重试最多 88 次实际转发，转发前实施预算限制。

除真实读取轨迹外，核对每个场景的工程判断、未证实项、禁止动作；不以列目录、回答自称读过或单一总分代替验收。研究性运行、真实连接和硬件测试不在这些合成场景中。
