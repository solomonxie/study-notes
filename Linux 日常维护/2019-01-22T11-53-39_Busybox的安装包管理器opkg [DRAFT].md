# Busybox的安装包管理器opkg [DRAFT]

`opkg`是OpenWrt系统下的安装包管理器，相当于Ubuntu的`apt`，或CentOS的`yum`，或Mac的`Homebrew`。

使用方法：
```sh
# 更新
$ opkg update

# 查看已安装软件
$ opkg list-installed
$ opkg list

# 安装指定软件
$ opkg install 包名
```

但是，opkg目前只支持少量的软件。如果要查看当前支持哪些软件安装，可以查看这个目录下的各个文件。其中每个文件代表一个提供源：
```sh
$ cat /var/opkg-lists/barrier_breaker

$ cat /var/opkg-lists/openwrtio
```

更改安装源`/etc/opkg.conf`，
```

```
[参考：OpenWrt.io - `opkg 软件源`](https://openwrt.io/docs/opkg/)



常用的软件安装：
```sh
$ opkg install tcpdump
```
