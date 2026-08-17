# 树莓派命令行找不到`ifconfig`命令
> command not found: ifconfig

[参考回答。](https://www.raspberrypi.org/forums/viewtopic.php?f=28&t=23405)

可以用`sudo ifconfig`,或直接指定位置`/sbin/ifconfig`，或者先设置别名`alias ifconfig="/sbin/ifconfg`，然后再正常使用。
