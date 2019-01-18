# ❖ FRP内网穿透 （进阶）

## 用配置文件运行

服务器端：
```ini
# FRP Server-side configuration
# Environment: All platforms
# How to run:
#   $ cd /path/to/frp/
#   $ ./frps -c ./frps.ini
#
```

客户端：
```ini
# FRP Client-side configuration
# Purpose: Expose Rpi's SSH / Web to public
# How to run (Linux):
#   $ cd /path/to/frp/
#   $ ./frpc -c ./frpc.ini
# How to connect:
#   SSH -> $ ssh ClientUser@ServerIP:2200
#   Website -> http://ServerIP:8001/index.html 
#   Webdav -> http://ServerIP:8088/webdav

[common]
server_addr = 13.228.20.100
server_port = 7000
privilege_token = frp123

# Logging settings:
log_file = /tmp/frpc.log
log_level = info
log_max_days = 3


# How to Connect SSH:
# $ ssh ClientUser@ServerIP -p 2200
# Equivalent to CLI command:
#   $ ./frpc tcp --server_addr "13.228.20.100:7000" \
#      --local_port "22" --remote_port "2200"
[SSH]
type = tcp
local_ip = 127.0.0.1
local_port = 22
remote_port = 2200

# Only allow ONE http definition at client frp
# because you can only define ONE vhost on server
# HTTP protocol has to set [vhost] on server:
#   vhost_http_port = 7800
#   vhost_https_port = 7443
# "remote_port" is USELESS if it's HTTP connection
# and the port is defined on server's "vhost"
# How to connect:
#   http://ServerIP:vhostPort/
#   http://13.228.20.100:7800 or https://13.228.20.100:7443
# Equivalent to CLI command:
#   $ ./frpc http --server_addr "13.228.20.100:7000" \
#      --custom_domain "13.228.20.100" --local_port "8888"
[Website]
type = http
local_port = 80
custom_domains = 13.228.20.100


# Only allow ONE http definition at client frp
# because you can only define ONE vhost on server
# HTTP protocol has to set [vhost] on server:
#   vhost_http_port = 7800
#   vhost_https_port = 7443
# "remote_port" is USELESS if it's HTTP connection
# and the port is defined on server's "vhost"
# How to connect:
#   http://ServerIP:vhostPort/
#   http://13.228.20.100:7800
# Equivalent to CLI command:
#   $ ./frpc http --server_addr "13.228.20.100:7000" \
#      --custom_domain "13.228.20.100" --local_port "8888"
[Webdav]
type = http
local_port = 8888
custom_domains = 13.228.20.100
```


## 用CLI命令运行

### 服务端
实际上服务端没太大必要用命令行执行，因为比较固定，没什么动态和经常改动的东西。

### 客户端：
客户端经常变动，所以用配置文件这种静态文件很不方便（尤其是在docker中），所以有时候用命令执行是一种好的选择。

> 注意：客户端只能针对某个服务器运行一个`frpc`命令，不像配置文件中可以设计多个定义。

- 暴露自己的HTTP服务(网页、Webdav等): 
```sh
$ ./frpc http --server_addr "13.228.20.100:7000" \
       --custom_domain "13.228.20.100" --local_port "8888"
```
- 暴露自己的SSH连接:
```sh
$ ./frpc tcp --server_addr "13.228.20.100:7000" \
       --local_port "22" --remote_port "2200"
```



## 设置为服务开机启动

Ubuntu中，把这种小服务设置到`systemd`中是最最方便的了，用`systemctl`即可开启或关闭。

客户端配置：
```ini
# FRP-Client system service file
# Environment: Ubuntu
# Owner: Solomon Xie
# Email: solomonxiewise@gmail.com
# How to set this service
#   1. Save this file as:
#       `/etc/systemd/system/frpc.service`
#   2. Enable start on login:
#       `sudo systemctl enable frpc.service`
#   3. Start now:
#       `sudo systemctl start frpc.service`
# How to inspect its status:
#   `tail -f /tmp/frpc.log`

[Unit]
Description=frpc daemon
After=syslog.target  network.target
Wants=network.target

[Service]
Type=simple
ExecStart=/usr/sbin/frpc -c /etc/frp/frpc.ini
Restart= always
RestartSec=1min
ExecStop=/usr/bin/killall frpc


[Install]
WantedBy=multi-user.target
```
