# Linux 设计系统时区和时间

把程序运行在树莓派上时，获取的时间默认是美国的，这样记录日志之类的东西也都是美国时间会容易混淆。所以需要在命令行里修改系统时区。

### 改时区
我们在`/usr/share/zoneinfo`这个文件夹里可以看到各种各样的国家和时区，找到自己的时区后拷贝到`/etc/localtime`即可改变时区

```shell
# 中国是ROC
sudo cp /usr/share/zoneinfo/ROC /etc/localtime

# 验证
date
```

### 改时间
一般其实不需要改时间，联网的话默认是从网上获取的。
如果要改，[参考这篇文章](https://www.garron.me/en/linux/set-time-date-timezone-ntp-linux-shell-gnome-command-line.html)
