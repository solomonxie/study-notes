# Python 环境变量$PATH怎么设置

Mac上的命令后有时候会找不到用`pip`安装的命令行程序，这很大原因会出于系统环境变量`$PATH`没有设置正确的`pip`的`bin`的位置。

一般可以设置如下:
```
export PATH="$HOME/Library/Python/3.7/bin:$PATH"  # pip executables are here

export PATH="/usr/local/bin:$PATH"
export PATH="/usr/local/sbin:$PATH"
export PATH="$HOME/.local/bin:$PATH"
```
