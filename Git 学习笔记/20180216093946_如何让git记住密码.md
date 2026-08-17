# 如何让git记住密码
全局的话：
```shell
git config --global credential.helper cache
```
只是当前repo的话：
```shell
git config credential.helper cache
```
这两句话的做的工作是一样的，就是在`~/.gitconfig`全局配置文件或者`.git/config`当局配置文件中加入这段话：
```
[credential]
        helper = cache
```
所以直接找到配置文件加入这两句话也是一样的。

上面三种配置都完成后，git push的时候就会记住密码，下次不用再输入了。

不过有个问题是，最好在全局配置user.name 和user.email，不然的话还是需要每次都让你输入用户名密码。



