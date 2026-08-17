# SSH 端口转发

## 本地端口转发: 从本地的一个端口转发到另一个接口

首先确认端口转发功能在配置里是开的：
```sh
sudo vim /etc/ssh/sshd_config

# 开启tcp转发
AllowTcpForwarding yes

# 重启sshd
sudo /etc/rc.d/init.d/sshd restart
```
