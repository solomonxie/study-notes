# 用SSH免密码登录服务器或树莓派

[参考文章。](http://blog.csdn.net/permike/article/details/52386868)

1. 首先在本机器生成密钥对 key pair:
输入`ssh-keygen`，然后一路回车。这样就成功的在`~/.ssh/`下创建了`id_rsa`私钥和`id_rsa.pub`公钥，且没有passphrase密码。
2. 连接到服务器。一般也是通过SSH连接，因为没配置好ssh呢，所以先用户密码登录。
3. 将本地的`id_rsa.pub`公钥内容复制到服务器的`~/.ssh/authorized_keys`文件中，这个文件支持多个公钥设置，每一行写一个：
```shell
echo "刚刚复制的本机公钥内容" >> ~/.ssh/authorized_keys
``` 
4. 一般来说，到了这里，就可以直接通过ssh登录服务器了。
5. 有的服务器的ssh默认设置，没有允许别人通过密钥登录等等，所以需要在设置文件里修改下：
```shell
vim /etc/ssh/sshd_config

#然后找到以下几样内容，改成一样的：
# 开启密钥登录功能
RSAAuthentication yes
PubkeyAuthentication yes

#  root 用户也可以通过 SSH 登录
PermitRootLogin yes

# 禁用密码登录
PasswordAuthentication no

# 编辑完后，保存退出，然后重启ssh
service sshd restart
```


## 更新
更方便的方法：
```sh
# 将私钥加入 ssh-agent
$ ssh-add ~/.ssh/id_rsa

# 将公钥复制到树莓派上
$ ssh-copy-id pi@192.168.1.2
```
