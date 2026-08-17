# 树莓派更新国内源

更多源，请参考：[树莓派—raspbian软件源（全）](https://www.jianshu.com/p/67b9e6ebf8a0)

需要修改两个文件：

- `/etc/apt/sources.list`
```
#科大源
deb http://mirrors.ustc.edu.cn/raspbian/raspbian/ jessie main contrib non-free rpi
```
- `/etc/apt/sources.list.d/raspi.list`
```
#科大源
deb http://mirrors.ustc.edu.cn/archive.raspberrypi.org/debian/ jessie main ui
```

然后运行更新：
```sh
$ sudo apt-get update
```
