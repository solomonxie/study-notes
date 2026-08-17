# Linux 修改本机时区

[参考：linux修改时区](http://coolnull.com/235.html)

```sh
# 查看当前时间
$ date -R
Fri, 09 Jan 2015 13:56:05 +0700

# 修改时区为中国时区
$ sudo cp /usr/share/zoneinfo/Asia/Shanghai /etc/localtime

# 查看时间
$ date -R
Mon, 07 Sep 2015 02:12:43 -0700
```

