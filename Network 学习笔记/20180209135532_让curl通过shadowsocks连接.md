# 让curl通过shadowsocks连接
shadowsocks是Socks5的连接方式。本地打开shadowsocks的客户端后，找到它在本机使用的端口。比如1080。然后输入如下命令就可以查看到效果：
```
curl --socks5-hostname localhost:1080 http://httpbin.org/ip
```
其中 http://httpbin.org/ip 是一个可以返回访问者ip地址的网站。
如果你的命令行返回的是你的服务器ip，那么就成功。
实践成功。
