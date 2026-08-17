# Linux开启ssh端口服务

[参考：linux(kali)开启ssh端口服务](https://blog.csdn.net/qq_37458055/article/details/75205282)

ssh链接可以远程管理linux设备，默认端口是22，安装好系统默认是不开启的，需要修改配置文件:

```sh
$ sudo vim /etc/ssh/sshd_config

# ssh端口
Port 22

# 运行密码登录
PasswordAuthentication yes

# 允许Root登录
PermitRootLogin yes

# 授权登录文件
AuthorizedKeysFile ~/.ssh/authorized_keys

# 重启ssh
$ sudo /etc/init.d/ssh start

# 启用开机启动ssh
$ sudo update-rc.d ssh enable
```
