# OpenWrt 配置HTTP Proxy透明代理

一般我们自己路由器的话，喜欢安装OpenWrt系统，而且会配置Shadowsocks/V2Ray等服务端，然后在局域网内共享它们的服务端口，比如1080之类的。
但是这些服务端口共享出来的，一般都是Socks协议，也就是说我们必须在电脑/手机/浏览器上安装支持socks的专门程序才行。但是对于没有安装这些客户端程序的客户端来说，非常的不友好。比如家人的iPhone手机，绝大部分都不会有美区apple账号去下载shadowrocket客户端。比如家中的电视盒子，也很难安装支持socks的客户端让你看netflix。

这种情况下，最好的解决方法就是要把socks的服务端口转换成http端口，这样任何设备都可以在连wifi的时候设置http proxy代理，也就是透明代理。

把Socks代理转发成Http代理，需要privoxy程序，用ssh登入路由器后：
```sh
# Openwrt安装privoxy
opkg install privoxy

# 编辑配置文件
vim /etc/config/privoxy
```

下面是配置文件，注意，我们监听路由器上socks端口1080，然后把它转发为1088，而不是默认的8118。因为如果使用默认的比较不安全容易被人利用，很可能在防火墙内已经被屏蔽。所以我们换另外一个端口：
```
# /etc/config/privoxy >>>
listen-address 0.0.0.0:1088
toggle  1
enable-remote-toggle 1
enable-remote-http-toggle 1
enable-edit-actions 0
enforce-blocks 0
buffer-limit 4096
forwarded-connect-retries  0
accept-intercepted-requests 0
allow-cgi-request-crunching 0
split-large-forms 0
keep-alive-timeout 5
socket-timeout 60

forward-socks5 / 127.0.0.1:1080 .
forward         192.168.*.*/     .
forward         10.*.*.*/        .
forward         127.*.*.*/       .
# <<< END OF FILE
```

这时候我们手动启用程序，并在后台运行：
```sh
nohup privoxy /etc/privoxy/config > /tmp/privoxy.log &
```

然后在路由器本机实验转发是否成功：
```sh
all_proxy=http://127.0.0.1:1088 curl https://httpbin.org/ip
```

如果上面返回的是期待的服务器IP，就证明配置成功了。

然后回到自己的电脑上，试试看连接路由器这个http-proxy端口是否能成功：
```sh
all_proxy=http://192.168.1.xxx:1088 curl https://httpbin.org/ip
```

如果成功就万事大吉。但是也有可能因为防火墙没有开放这个端口，导致访问失败。
这时候需要到firewall里开放这个端口的访问权限。iptables命令行配置比较麻烦，可以直接到openwrt的页面上点击菜单 -> 网络 -> 防火墙 -> 流量规则 -> ”打开路由器端口“栏目 -> 输入端口号和协议 -> 添加 -> 保存配置:
<img width="1109" alt="image" src="2021-02-28T13-04-41_OpenWrt 配置HTTP Proxy透明代理_files/img_01.png">

这时候在路由器的命令行里输入 `iptables -L` 然后搜索1088，看看是否配成功，主要看是否有其它程序也占用了这个端口。如果没有，我们就再回到自己主机上尝试：
```sh
all_proxy=http://192.168.1.xxx:1088 curl https://httpbin.org/ip
```

基本上到这里就没太大问题了。

至于手机、电视盒子等客户端，都可以在wifi连接的设置里找到手动设置代理的地方，填入局域网的路由器IP和刚刚配置的端口，就可以连接上了。
