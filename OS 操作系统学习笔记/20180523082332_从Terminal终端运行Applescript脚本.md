# 从Terminal终端运行Applescript脚本
Mac上原生安装了`osascript`这个命令行工具，可以直接运行一句applescript脚本，或者执行一个脚本文件。

- 运行一句脚本：
```shell
osascript -e 'display dialog "hello world" '
```
- 运行脚本文件：
```shell
osascript PATH-TO-SCRIPT.scpt
```
