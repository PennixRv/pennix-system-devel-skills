# 构建通过但镜像缺包

先确认正在比较的是同一 image、机器、发行和构建产物。查目标镜像 manifest、已有 pkgdata 或 rootfs 内文件，而不是只确认某个 recipe 运行过。

1. 反查文件应由哪个运行时包携带，区分 recipe、主包、子包、开发包与目标架构。先核对安装到暂存根和包拆分的证据，再判断镜像包含关系。
2. 核对实际镜像选择、`IMAGE_INSTALL`、`IMAGE_FEATURES`、packagegroup 和运行依赖。不要把局部 `local.conf` 试验当作团队配方合同。
3. 若包已在清单但文件不符合预期，检查包安装与 post-install、镜像层/分区或使用了旧工件。若 `do_rootfs` 有明确失败，则回到实际失败任务日志；不把缺包和任务失败混为一谈。

参考目标版本的 [Customizing Images](https://docs.yoctoproject.org/dev/dev-manual/customizing-images.html)。未见相应工件就给缺项，不声明已确认缺失原因。
