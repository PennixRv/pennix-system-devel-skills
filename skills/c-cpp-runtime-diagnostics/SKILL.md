---
name: c-cpp-runtime-diagnostics
description: 设计 C/C++ 的运行时诊断验证，或判读实际 ASan、UBSan、TSan、Memcheck 报告。核对被插桩及实际执行的目标和覆盖；普通源码审查、core 的符号身份或 CPU 性能分析不由此入口接管。
---

# C/C++ 运行时诊断

先明确要区分的故障及能执行的最小场景。已有报告时先核对工具、目标工件、编译与最终链接、运行库、输入和退出状态；同名库、测试进程和实际服务可能不是同一构建。

1. **选择能回答问题的检查。** ASan 主要说明被覆盖路径上的地址与内存错误，UBSan 只检查已选的未定义行为类别，TSan 关注运行中可观测的数据竞争；Memcheck 等工具有不同平台、运行负担和覆盖。按实际工具链和目标核对支持、运行库和组合限制，不将各类检查视作可互换。
2. **解释报告与实际覆盖。** 优先关联第一条有用报告的访问、分配、释放或冲突线程；确认工件与符号身份、正常退出还是被中止、日志是否完整。缺被测库的插桩或缺目标执行记录时，报告未验证范围；不把另一工件的通过、过滤后的报告或零发现当作安全证明。
3. **限制实验改动。** 有权执行时用项目已有隔离构建与最小可控输入，保留正常构建的对照。构建、最终链接、运行和结果判定分别取证；不默认部署诊断运行库，不靠 suppression 关闭未知问题，不使用客户数据。

输出所证实的问题、覆盖边界和最小复测。插桩与最终链接核对本机版本的 [AddressSanitizer](https://clang.llvm.org/docs/AddressSanitizer.html)、[UndefinedBehaviorSanitizer](https://clang.llvm.org/docs/UndefinedBehaviorSanitizer.html)或 [ThreadSanitizer](https://clang.llvm.org/docs/ThreadSanitizer.html)。
