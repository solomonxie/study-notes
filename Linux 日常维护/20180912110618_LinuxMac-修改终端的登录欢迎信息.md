# Linux/Mac 修改终端的登录欢迎信息

Linux可以设置登录前后的欢迎信息，可以修改3个文件：

Before login:
```
/etc/issue
/etc/issue.net #网络登陆显示
```
After login:
```
/etc/motd
```

> Mac上默认没有这些文件，需要手动创建。


如果是需要执行某个命令生成信息，那就需要改`~/.zshrc`或`~/.bash_profile`了。只需要在里面加入具体命令即可。

如果是只给SSH登录执行命令，则这么写：
```sh
if [[ -n $SSH_CONNECTION ]] ; then
    echo "I'm logged in remotely"
fi
```
