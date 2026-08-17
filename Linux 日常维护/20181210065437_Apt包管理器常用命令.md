# Apt包管理器常用命令

`apt`包管理器有很多命令可以使用：
- `apt`
- `apt-get`
- `apt-cache`
- `dpkg`

显示已安装的某包具体信息：
```sh
$ apt-cache show 包名
```

显示已用`apt-get`安装的某包的所有安装位置：
```sh
$ dpkg -S 包名
```


