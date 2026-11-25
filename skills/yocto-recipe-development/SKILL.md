---
name: yocto-recipe-development
description: 编写、修改或审查 Yocto/OpenEmbedded 的配方、bbappend、类和层元数据，核对版本、依赖、包拆分和生效路径；不把供应商 BSP 或完整镜像交付当默认范围。
---

# Yocto 配方与层开发

先确认目标 Yocto/OE-Core 与 BitBake 分支、启用层、目标机/发行配置以及当前版本的语法。优先读取已有相近配方和项目的有效元数据证据，不把开发版手册当作目标合同。

1. **选择最小元数据位置。** 已有配方且只做目标层适配时先核对 `.bbappend` 是否匹配、collection、查找路径和 provider；公共行为才考虑类。新增配方明确源码、固定版本/校验、许可、交叉构建方式、安装阶段和分发对象。细节查[层与配方生效](references/layer-and-recipe.md)。
2. **分别核对构建和运行。** `DEPENDS` 关注构建所需的提供者和本机工具；运行依赖按实际拆出的包核对 `RDEPENDS` 等声明。安装进目标暂存根，再看文件由哪个包携带；有配方不等于有同名运行包。
3. **做最小审查和验证。** 检查变更是否误触发其他架构、机器或发行，避免不必要地越过项目的许可和 QA 门槛。用现有日志、清单、配方与可用的已过滤输出说明；运行 BitBake、启用 `devtool` 或生成镜像都需要相应授权及可信构建环境。

输出目标 release/层、最小变更或审查发现、包与依赖关系及当前验证限度。参见目标版本的 [Yocto 编写配方](https://docs.yoctoproject.org/dev/dev-manual/new-recipe.html)和[层管理](https://docs.yoctoproject.org/dev/dev-manual/layers.html)。
