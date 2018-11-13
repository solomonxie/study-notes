# Apache 2 reload 失败

背景：
OS：Raspberry Pi Rasbian
Context：第一次安装Apache2，没配置任何文件，就不能reload

Reload Apache时后发生错误：
```sh
$ sudo /etc/init.d/apache2 reload
[....] Reloading apache2 configuration (via systemctl): apache2.service
Job for apache2.service failed. 
See "systemctl status apache2.service" and "journalctl -xe" for details.
```

尝试过的方案：
- `sudo apt-get purge apache2 && sudo apt-get install apache2` --- 没用
- `sudo /etc/init.d/apache2 restart` ---- 可以重启但是还不能reload

解决方案：
```sh
# 找到占用80端口的服务 （发现是Nginx服务器在用）
$ sudo netstat -pant |grep 80
tcp6  0  0  :::80           :::*       LISTEN  769/nginx    -g  daemon

# 找办法关闭这个服务
$ sudo systemctl stop nginx
# 或
$ sudo service <服务名> stop

# 重启并重新加载Apache2
$ sudo /etc/init.d/apache2 restart
$ sudo /etc/init.d/apache2 reload
[ ok ] Reloading apache2 configuration (via systemctl): apache2.service.
```
