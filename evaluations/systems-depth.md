# 系统工程深化评测

用 `case.py` 只渲染合成输入，不把判据、文件路径或入口名称另行提示给被测会话。用冻结的完整候选集合，在相同模型和受控工具权限下分别起新会话。评价分开记录入口及必要参考的实际读取、工程判断、停止条件；列目录和自称已读都不算成功读取。

| 场景 | 必须实际读取 | 不应接管的入口或行为 |
| --- | --- | --- |
| `depth-cpu-output` | `systems-performance` 与 `benchmark.md` | 给出了优化对照而非 `perf` 读取问题；不以其他指标掩盖错误语义和 P99 退化。 |
| `depth-memory-scope` | `systems-performance` 与 `linux-evidence.md` | 无追踪或插桩工件，不以 `linux-perf`、`linux-observability` 或运行时诊断替代内存证据。 |
| `gdb-build-id` | `gdb` | 无匹配符号不确认源码行；不启动程序、连接目标或补跑插桩。 |
| `depth-shutdown-wait` | `linux-userspace-development` | 已给出完成通道和等待关系，不改用 GDB、`io_uring` 或 Linux 追踪采集。 |
| `c-alloc` | `c-systems` | 不套用 C++ 所有权类型；保持失败时输出参数和旧对象责任。 |
| `cpp-view` | `cpp-coding-standards` | 不强行更换编译器、引入异常或在回调分配。 |
| `python-timeout` | `python-system-scripting` 与 `failure-and-rerun.md` | 不把包装器退出当成实际写者全部停止；不复用或更改真实输出。 |
| `transfer-bash-pipeline` | `bash-defensive-patterns` 与 `failure-and-cleanup.md` | 不读 POSIX 入口取代 Bash 语义；区别退出状态、部分临时工件和发布状态。 |
| `depth-posix-pipeline` | `posix-shell-pro` | 不读 Bash 入口，不推定两个目标解释器都支持 `pipefail`。 |
| `v2-perf-valid` | `linux-perf` | 留出例，不参与文案调整；不读取通用性能入口接管报告判读。 |

Bash 行为夹具由 `python3 -B -m unittest discover -s tests -p test_bash_failure_fixture.py -v` 执行。它绑定临时目录，核对管道错误、命令替换、提前关闭、临时工件清理和重跑；不把 Bash 的结果当作对 dash 或 BusyBox ash 的验证。

该矩阵只支持所列场景，不证明真实服务的性能或任意输入的路由。预检、会话、模型转发和定向复测的硬上限按当前任务合同记录；筛选通过样本不能抵消失败或越权记录。
