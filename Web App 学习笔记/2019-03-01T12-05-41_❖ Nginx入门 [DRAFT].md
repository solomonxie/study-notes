# ❖ Nginx入门 [DRAFT]



## 理解Nginx配置

入门Nginx，主要是学配置文件。
理解Nginx，才需要懂背后逻辑。

大概的结构是：
```conf
http {
    server {
        listen 80
        location / {
            #....
        }
    }
}
```

可以看到这个整体结构：最外面是`Protocol`，即传输协议，可以是http／https／pop3等；然后是这个协议下的`server`服务应用，一个`server`只能对应一个`port`端口，即一个本机唯一的网络进程；这个服务应用下，能够对应多个`location`，进行灵活的地址映射。

在Server中：
一个`Server`其实就对应一个`port`端口**入口**，相当于本机一个唯一的网络进程。
一个`Server`可以有多个`location`位置，如根路径`/`，或子路径`/api/v3/get`。
一个`Server`可以把入口`port`”的不同`location`映射“到其它多个`port`上，即反向代理 。
一个`Server`的设置可以完全独立于其它`Server`不同，如`chartset`, `reversed proxies`
一个配置文件，可以有多个`Server`。

对于多个应用，一个应用配置一个`port`是肯定的，所以也就是要配置多个对应的`Server`，如80给Flask用，8080给PHP用。


