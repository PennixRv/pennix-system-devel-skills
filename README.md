# Pennix 系统软件开发 Skills

用于 Linux 用户态、内核与驱动、Zephyr、裸机与 FreeRTOS，以及 C/C++、Python、Bash 和 POSIX `sh` 的设计、实现、审查和排错。构建、交叉工具链、GDB、ELF ABI、性能和 Yocto 各有独立入口。完整成员以 [`collection.json`](collection.json) 为准，适用范围以各成员的 `SKILL.md` 为准。

按要解决的问题选入口，而不是按文件、框架或工具名选。例如，审查 Linux 补丁是否引入回归，先看补丁证据；设计驱动解绑则先看生命周期。Zephyr 工件的 GDB 符号错配先核对调试工件，只有板卡或构建域仍有疑问时才补查 Zephyr。Skill 不代替项目约定、操作授权或实际测试。

只解释 Linux `perf` 报告用 `linux-perf`；要设计性能比较、归因或验证优化收益则用 `systems-performance`；直接核对追踪事件、时钟或打点用 `linux-observability`。实际 ELF 链接失败、ABI 承诺与交叉工具链错配也有不同入口。内核和 Zephyr 的验证入口把构建、宿主／模型运行与真实目标证据分开，不把一个测试层当作另一个。

本仓库维护源码，不负责直接安装。正式集成由 `pennix-lifecycle` 管理；本地候选不应手工复制到实际用户目录。成员只分发 `SKILL.md`、许可和声明文件及同目录下的 Markdown 参考，不分发命令或脚本。第三方来源、对应许可及改动见[成员来源](UPSTREAM.md)。

维护时运行 `python3 -B scripts/verify_collection.py` 和 `python3 -B -m unittest discover -s tests -v`。新增或移动参考时，确认对应 `SKILL.md` 在适用位置直接链接该参考，并说清何时需要读；能找到文件不等于知道何时读取。

行为场景及证据要求见[扩充与相邻路由评测](evaluations/expansion.md)、[首版评测说明](evaluations/first-release.md)、[二版性能评测](evaluations/performance-v2.md)和[二版编写审查评测](evaluations/authoring-review.md)。静态检查和宿主发现不能代替行为结果。
