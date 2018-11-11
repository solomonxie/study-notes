# 清理本地DNS／hosts缓冲
因为有时候改hosts，或者改远端DNS时候，本地都没有及时响应，所以有时候会考虑清一下缓冲。

Mac OS X 环境下，通常可以使用以下命令：
```sh
sudo dscacheutil -flushcache
```

Linux/Unix环境下，根据系统DNS缓存机制的不同设置 
系统使用NSCD的DNS缓存，可以通过以下命令：
```sh
sudo /etc/init.d/nscd restart
```

服务器或者路由器如果使用DNSMASQ的话，可以通过以下命令：
```sh
sudo dnsmasq restart
```

Windows环境下，可以使用以下命令：
```sh
ipconfig /flushdns
```

