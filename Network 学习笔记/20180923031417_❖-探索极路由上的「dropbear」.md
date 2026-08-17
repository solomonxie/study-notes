# ❖ 探索极路由上的「dropbear」

极路由如果开通了`开发者工具`，我们就可以ssh进路由器。但是极路由（以及其它路由）通常用的都不是一般Linux上默认的`OpenSSH`(sshd)服务，而是一个叫`dropbear`的服务实现ssh协议的。
这也就是为什么在路由器系统里找不到`sshd`或`~/.ssh`类似的东西。

[参考：轻量级SSH服务器dropbear 的安装使用指南](http://blog.51cto.com/1inux/1638874)

> "dropbear是一款基于ssh协议的轻量sshd服务器，与OpenSSH相比，他更简洁，更小巧，运行起来占用的内存也更少。每一个普通用户登录，OpenSSH会开两个sshd进程，而dropbear只开一个进程，所以其对硬件要求更低，也更利于系统的运行。Dropbear特别用于“嵌入”式的Linux（或其他Unix）系统"

`dropbear` 主要有以下程序：
- 服务程序：`dropbear` （类似于Openssh的 sshd）             
- 客户程序：`dbclient` （类似于Openssh的 ssh）   
- 密钥生成程序：`dropbearkey`

默认dropbear是支持SCP上传下载的，但是默认没有开启SFTP的支持。

如果要开启SFTP的支持，需要依赖一个二进制文件，或者干脆安装一个`OpenSSH`的服务。
        

## Dropbear SSH 免密码登录
`authorized_keys`位置和openSSH不同，`Dropbear`的配置文件夹在`/etc/dropbear/`，然后授权的公钥存在`/etc/dropbear/authorized_keys`中，如果没有，就新建一个。
过程一样，把本机的`~/.ssh/id_rsa.pub`公钥或其它公钥复制粘贴到dropbear的授权文件中即可：
```sh
# 一键操作
cat ~/.ssh/id_rsa.pub | ssh root@<路由器IP> 'cat >> /etc/dropbear/authorized_keys'
```

无需重启任何东西，直接免密码登录即可。

对了，如果本机没有公钥，那就生成一个，直接输入`ssh-keygen`命令，一路回车（全部都默认设置），就生成了一对钥匙，包括私钥`~/.ssh/id_rsa`和公钥`~/.ssh/id_rsa.pub`。


## Dropbear 生成本机的密钥对

不同于OpenSSH的`ssh-kengen`命令，dropbear是用`dropbearkey`生成密钥的。

```sh
# 生成id_rsa私钥
$ dropbearkey -t rsa -f /etc/dropbear/id_rsa

# 生成id_rsa.pub公钥
$ dropbearkey -y -f /etc/dropbear/id_rsa | grep "^ssh-rsa " > /etc/dropbear/id_rsa.pub
```
