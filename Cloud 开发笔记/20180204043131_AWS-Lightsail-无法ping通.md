# AWS Lightsail 无法ping通
ping某一个服务器，是需要服务器防火墙允许ICMP协议的数据包的。经查阅，AWS的所有服务是默认关闭icmp的。

> 除独立的Lightsail外，其它AWS服务都可以在安全组中设置防火墙开启icmp。
然而Lightsail的防火墙设置页面，并没有icmp选项，官方也没有任何相关解决方案。

## 更新
然而发现Lightsail可以在管理后台设置开放端口，如果ping指定的端口，那么还是可以ping通的。如：
```sh
ping 192.168.1.123:8888
```
