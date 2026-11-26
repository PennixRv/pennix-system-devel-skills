# Zephyr 测试平台的覆盖判据

- **宿主与 `native_sim`：** 查宿主 ABI、编进来的驱动或替身及其断言，不能外推实际 CPU 架构、可用外设、真实中断或栈时序。宿主可执行不等于产出的任意目标镜像可执行。
- **QEMU 或 Renode：** 固定机器与模型版本，只接受对本次断言相关的模型证据。串口输出证明当次可观察路径，不证明未建模的 DMA、计时、电气或功耗；不能用模型启动代替测试执行。
- **实板通道：** 先核对当前板、runner、固件/构建域、硬件映射与设备测试记录。没有实际结果时只说明所缺环境；不因测试报告总数为绿而把实板项补算通过。

参见 [Zephyr native_sim](https://docs.zephyrproject.org/latest/boards/native/native_sim/doc/index.html) 和 [Renode 测试说明](https://renode.readthedocs.io/en/latest/introduction/testing.html)；以目标版本和该用例真正覆盖的能力为准。
