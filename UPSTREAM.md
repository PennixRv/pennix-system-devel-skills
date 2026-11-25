# 成员来源与维护边界

集合原创文件采用 MIT。成员目录自带对应许可；如纳入第三方文件，逐件记录上游路径、固定提交、适用许可和差异，保留分发所需的许可、署名和声明。不以本仓库的 MIT 重新许可外部材料。

当前清单为 W1 本地候选，未通过行为评测，不用于部署。列出的工程文档用于核对接口和行为，不复制其正文。

| 成员 | 工程资料 |
| --- | --- |
| `linux-driver-lifecycle` | [Linux Driver API](https://docs.kernel.org/driver-api/)、[Devres](https://docs.kernel.org/driver-api/driver-model/devres.html)、[Kbuild](https://docs.kernel.org/kbuild/)及 [Kconfig 语言](https://docs.kernel.org/kbuild/kconfig-language.html)。 |
| `linux-userspace-development` | [libuv 的设计](https://docs.libuv.org/en/v1.x/design.html)用于核对异步关闭和资源寿命；[systemd 就绪通知](https://www.freedesktop.org/software/systemd/man/latest/sd_notify.html)用于区分进程启动和服务就绪。两者均非运行依赖。 |
| `python-system-scripting` | Python [`subprocess`](https://docs.python.org/3/library/subprocess.html)用于核对子进程与超时合同，[SQLite 测试策略](https://sqlite.org/testing.html)提供失败后重跑与持久状态的对照思路。 |
| `c-systems`、`posix-shell-pro` | 聚合仓 `sickn33/agentic-awesome-skills` 的 `166f581cfdc37d94cf56efe4454fb06a5759776c` 下，两个候选都只声明 `source: community`；所查文件未证明具体原始作者或条目许可传递。按合同独立撰写，不复制候选正文或脚本。适用证据分别为 [SEI CERT C](https://wiki.sei.cmu.edu/confluence/display/c/SEI+CERT+C+Coding+Standard) 和 [Portable Shell](https://www.gnu.org/software/autoconf/manual/autoconf.html#Portable-Shell)。 |

## 按固定提交适配的成员

表中上游路径是本地成员 `SKILL.md` 及所列参考的出处。本地正文根据目标范围重新整理；没有列出的上游脚本、模板、插件或参考文件不分发。每个成员的 `LICENSE` 保留相应的上游许可文本。

| 成员 | 固定来源及许可 | 本地分发范围及变化 |
| --- | --- | --- |
| `cpp-testing` | `affaan-m/ECC` `4adeee6732a12d1540f49a4d50a38ce8c97f9a53`，`skills/cpp-testing/SKILL.md`，MIT。 | 接入已有测试夹具和 CTest；不复制联网下载框架的 quickstart；补交叉发现和运行边界。`references/failure-paths.md` 按本文测试边界和 SQLite 先例独立写作。 |
| `cmake`、`make`、`cross-toolchain`、`gdb` | `mohitmishra786/low-level-dev-skills` `18f29518a47fda070e6ec1268cb577692fae9a10`，`skills/build-systems/cmake/SKILL.md`、`skills/build-systems/make/SKILL.md`、`skills/compilers/cross-gcc/SKILL.md`、`skills/debuggers/gdb/SKILL.md`，MIT。 | 保留目标/preset、规则和 depfile、三元组/sysroot、符号和回溯的取证顺序；不引入安装、CMake 最低版本、全量构建、QEMU、新符号重编或默认附加。两份本地参考只补 Ninja 和交叉配置边界。 |
| `bash-defensive-patterns` | `wshobson/agents` `c96b5f6552dba32e4492307493ee613581430715`，`plugins/shell-scripting/skills/bash-defensive-patterns/SKILL.md`、同目录 `references/details.md`，MIT。 | 保留参数、失败与临时物清理；不强制严格模式或 Bash 迁移。`references/failure-and-cleanup.md` 适配其中错误与清理模式。 |
| `elf-abi-compatibility` | `jiying2007/agent-dev-kit` `c030a8e147441799b458f5310107124e2ce8816f`，`skills/adk-component-api-stability/SKILL.md`，MIT。 | 保留旧消费者与三层证据；不依赖 ADK 或默认运行示例，ABI 工具用法按目标版本引用。 |
| `embedded-systems` | `Jeffallan/claude-skills` `d98d06edb54c25cfb94017c0ef830342a34a43ba`，`plugin/skills/embedded-systems/SKILL.md`，MIT。 | 收窄到裸机和 FreeRTOS；不夹带芯片初始化模板，不把 `volatile` 当同步或假定看门狗和板卡量测。 |
| `linux-kernel-review` | `masoncl/review-prompts` `5865de7c40414e157f688eb1e95914e3784f11bc`，`kernel/review-core.md`、`kernel/subsystem/` 的导航规则，MIT。 | 保留差异取证、子系统和反例核对；省略原自动编排、导航依赖、固定排除项及写出评论；`references/subsystem-evidence.md` 只给证据索引。 |
| `linux-perf` | `intel/skills` `f6e32edbb75cc0d473905da8775116061fdeea39` 的 `skills/linux-perf/SKILL.md` 和同目录 `.source.json`；后者及分发仓的 `NOTICE` 明确其来自 `intel/intel-performance-skills` `e9d0b6410fb1ad7a50fb81e0868fd23ae886882c`，此成员为 MIT，不是汇总仓默认的 Apache-2.0。 | 只适配通用计数、采样和报告；`LICENSE` 源于分发仓 `NOTICE` 中该上游的完整 MIT 文本，不分发 `branchprob.py` 或 `gccbranchprob.py`，不更改权限。 |
| `zephyr-foundations` | `beriberikix/zephyr-agent-skills` `ed63cdfb8cdfbeb5946ea39c33f4aa6bcf3a5cce`，`skills/zephyr-foundations/SKILL.md`，Apache-2.0。`ksachdeva/zephyr-rtos-ai` `60c5856de9c1e4290b233b325d4ed1eb22ce7fd7` 的 `zephyr-device-drivers`、`zephyr-kconfig` 用于交叉对照。 | 修改入口而不分发脚本或模板；配套设备与配置参考独立按官方文档整理，修正 DTS 和 Kconfig 边界。 |
| `yocto-recipe-development`、`bitbake-debug` | `Higangssh/yocto-agent-skills` `53643acdbfecdc3e2186d478c7ae5b19fe0adf12`，`skills/yocto-recipe-review/SKILL.md`、`skills/yocto-layer-review/SKILL.md`、`skills/bitbake-debug/SKILL.md` 和 `skills/yocto-image-rootfs/references/image-rootfs.md`，MIT。 | 配方审查补开发路径，层与镜像资料按需；不允许默认重跑、输出完整环境或改真实工作区。 |

## 未分发的候选

`cpp-coding-standards` 原候选为 [`affaan-m/ECC` 固定文件](https://github.com/affaan-m/ECC/blob/4adeee6732a12d1540f49a4d50a38ce8c97f9a53/skills/cpp-coding-standards/SKILL.md)。其声明派生自 [C++ Core Guidelines](https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines)，内容含编号及规则措辞；未将 ECC 根 MIT 视为能够转授全部上游内容。本地同名条目根据目标工程的版次、接口和证据独立撰写，采用集合 MIT，不复制上述正文、编号表和示例。
