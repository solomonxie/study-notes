#  ❖ 如何用SSH与Github连接（push等）

为了让服务器自动push本地仓库，试过了`git config credential.helper cache`这样让它缓存用户名。
但是这个不稳定，每过一段时间github又会要求你再手动输入密码。
如果想让脚本自动推送，最可靠的还是用ssh访问github。
可是一般都知道，ssh要访问哪里，本地还是需要输入一个密码来解锁ssh的private key的，说白了就跟不用ssh连接直接输入密码没区别了嘛！
网上解决方案一般都是用什么openssl之类的，重新生成一个没有密码的ssh key。太麻烦，
发现其实ssh自带生成密钥的工具就能够设置不带密码的key。

方法：
直接输入`ssh-keygen`命令，就会提示输入`key pair`密钥对的地址和名称，不输的话就默认为`~/.ssh/id_rsa`这个文件作为私用密钥，同目录的`id_rsa.pub`作为公用密钥。
然后会提示输入密码，这时只要什么都不输直接回车，就可以创建好一个不用输`passphrase`的ssh key了。
然后到github的个人设置页里，找到ssh处，把`id_rsa.pub`的内容完全拷贝进去保存即可。
这时候，随意的`git push`之类与远程仓库连接都不需要输什么密码了。

问题：
目前只有默认名的`~/.ssh/id_rsa`这个管用，自己起名字的ssh key现在还不能用。



## 针对Github某个Repo指定SSH key进行连接
在个人帐户里，可以设置全局的SSH-key，任意操控各个repo。
其实，还可以限制权利，只针对某个repo设置ssh-key。

方法是：打开Repo -> Settings -> Deploy keys -> Add deploy key -> 把自己指定的ssh-key粘贴进来。
下次就可以免密码与github连接了。

但是，这里还有一个问题：如果针对每个repo设置不同的key，怎么让`git push`选择用哪一个key进行通讯呢？
看下面：



## 指定SSH key对Github进行连接
这个问题网上一样众说纷纭，因为没有官方设计的直接方法，`git push`也没有指定key的选项。

目前有这几种常用方式可以达到指定key的作用：
- `ssh-agent` 命令：不推荐
- 修改`GIT_SSH`环境变量：不推荐
- 修改`core.sshCommand` Git配置
- 修改`GIT_SSH_COMMAND` 环境变量
- 修改`~/.ssh/config`配置文件

在当前用户目录下建立／修改`~/.ssh/config`文件，在里面指定默认的key文件位置。唯一的问题就是，只能指定一个key。

`~/.ssh/config`中的设置大概格式是：
```
Host github.com
    HostName github.com
    IdentityFile /path/to/your/personal/github/private/key
    User dandv

Host github-work
    HostName github.com
    IdentityFile /path/to/your/work/github/private/key
    User workuser

```

注意，ssh-key文件的权限需要是400，所以要记得修改权限：
```sh
$ chmod 400 ~/.ssh/id_rsa_github
```
