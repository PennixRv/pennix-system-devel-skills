# 层与配方生效

按实际 `bblayers.conf`、`conf/layer.conf`、层集合与版本/兼容性、选中的配方路径和已有 `bitbake-layers` 输出核对。目录存在不证明启用；配方启用不证明 append 匹配；append 有效也不证明通过了机器或发行 override。检查 recipe 版本匹配和 provider 选择，再改最上游错误的位置。

只在任务涉及机器/内核时，从 `MACHINE`、所选 provider 和 kernel append/片段找到配置与部署工件，不假定完整 BSP 交付。发现许可、CVE 或 SPDX 疑点时对照目标版类和已有产物；存在报告不等于已合规或已消除风险。资料：[机器配置](https://docs.yoctoproject.org/dev/dev-manual/new-machine.html)、[内核任务](https://docs.yoctoproject.org/dev/kernel-dev/common.html)、[SBOM](https://docs.yoctoproject.org/dev/dev-manual/sbom.html)。
