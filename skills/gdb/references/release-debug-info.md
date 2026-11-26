# 发行构建的离线取证

- 先从 core 的映射及当次发布记录对上可执行文件、DSO 与构建域。同名文件、Git 版本一致或时间戳相近不够。缺档时区分可证实的模块／地址与未符号化的帧；不用另编副本还原原运行。
- 独立调试文件按 Build ID 或 `.gnu_debuglink` 对应关系核验。若该产物采用 split DWARF，核对指定的 `.dwo`/`.dwp` 与编译单元身份；匹配一个主文件不证明所有 DSO、调试单元和源文件路径可用。只允许离线时不请求符号服务。
- 调试器显示的内联帧可说明源码级调用关系，不等于物理栈多了一层。变量标为 `<optimized out>` 可能没有可恢复的位置；结合匹配工件和可核实的 PC／反汇编解释，不从它推断变量值或分支未执行。

见 [GDB 独立调试文件](https://sourceware.org/gdb/current/onlinedocs/gdb.html/Separate-Debug-Files.html)和 [GDB 优化代码调试](https://sourceware.org/gdb/current/onlinedocs/gdb.html/Optimized-Code.html)。不改变系统 core 生成策略，也不默认解引用 core 中的敏感内容。
