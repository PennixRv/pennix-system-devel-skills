# Pennix 系统软件开发 Skills

用于 Linux 用户态、内核与驱动、Zephyr、裸机与 FreeRTOS，以及 C/C++、Python、Bash 和 POSIX `sh` 的设计、实现、审查和排错。构建、交叉工具链、GDB、ELF ABI、性能和 Yocto 各有独立入口。完整成员以 [`collection.json`](collection.json) 为准，适用范围以各成员的 `SKILL.md` 为准。

按要解决的问题选入口，而不是按仓库出现的文件或框架名选。例如，审查 Linux 补丁是否引入回归，先看补丁证据；设计驱动解绑则先看生命周期。Zephyr 工件的 GDB 符号错配先核对调试工件，只有板卡或构建域仍有疑问时才补查 Zephyr。已有项目规则和验证入口继续生效；Skill 不代替项目约定、操作授权或实际测试。

本仓库维护源码，不负责直接安装。正式集成由 `pennix-lifecycle` 管理；本地候选不应手工复制到实际用户目录。首发成员只分发 `SKILL.md`、许可和声明文件及同目录下的 Markdown 参考，不分发命令或脚本。第三方来源、对应许可及改动见[成员来源](UPSTREAM.md)。

维护时运行 `python3 -B scripts/verify_collection.py` 和 `python3 -B -m unittest discover -s tests -v`。行为场景及证据要求见[评测说明](evaluations/first-release.md)；静态检查和宿主发现不能代替行为结果。
