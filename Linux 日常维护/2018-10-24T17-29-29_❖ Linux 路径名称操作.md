# ❖ Linux 路径名称操作

Linux自带的`basename`和`dirname`命令就极其好用，很多情况都不需要`sed`和`awk`等高级复杂工具。

常用命令：
```sh
# 获取路径名
$ dirname "/etc/apt/abc.txt"
>>> /etc/apt

$ dirname "/etc/apt/"
>>> /etc

# 获取<当前目录>的绝对路径
$ echo ${PWD##*/}

# 获取<当前目录>的父目录的绝对路径
$ dirname $(pwd)
# 或
$ echo ${PWD%/*}


# 获取文件名（或最后一个目录名）
$ basename "/etc/apt/abc.list"
>>> abc.list

$ basename "/etc/apt/"
>>> apt

# 获取名称不包括扩展名
# (通过去掉结尾的指定文字来达到)
$ basename "/etc/apt/abc.list" .list
>>> abc
```


常用脚本中路径命令：
```sh
# 获取<当前脚本>的绝对路径
$ dirname $0

# 获取<当前脚本>的父目录的绝对路径
cd $(dirname $0)
echo $(dirname $(pwd))
```
