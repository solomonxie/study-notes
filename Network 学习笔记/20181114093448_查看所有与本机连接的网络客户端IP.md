# 查看所有与本机连接的网络客户端IP

假设自己是Server，想知道当前有多少人正在与自己连接，每个人的IP是什么。

`Netstat`:
```sh
$ netstat -pant
```

持续监视(利用watch命令)：
```sh
$ watch netstat -pant
```

> 注意：Mac上默认版本非常低所以不兼容同样的参数，需要更新Mac的gnu utils等。
另外，watch需要额外brew安装

旧版本的用法如下：
```sh
$ watch netstat -ptcp -a
```
