# ❖ Linux任务在服务器上持续／不间断运行

> 通过ssh登录服务器运行一个python脚本，想让它24小时不间断运行。可是一旦我退出ssh，整个程序就断了。这是由于ssh的session特性——它本身就是一个session，连接上开启session，断开ssh连接则关闭session，关闭时所有你在这个session里运行的东西都会被中断。

### 关于ssh关闭连接就关闭运行程序的问题

[在这里可以看到一些解决方案](https://askubuntu.com/questions/8653/how-to-keep-processes-running-after-ending-ssh-session)。

## 解决方案一："tmux"

很幸运，在学习怎么把vim分屏浏览时知道了tmux，然后看视频时学到：原来ssh是这样的特性，断开就会停止所有之前连接ssh期间运行的所有processes，而tmux的核心业务不在于把屏幕分成几块好看，而是它能保存session！而且还能多端实时直播session！

### 解决方案二："nohup"

网上一般说到不间断任务，一般也都会先提到这个，可以说是常规方案。
`nohup`一般都是Linux系统自带的，使用极其简单：

```sh
$ nohup 具体指令 &
```
加`&`是让其转入后台运行，而不在前台显示。

### 解决方案三："screen"或"byobu"

这据说是现在更常用的方法，[参考文章](https://www.howtogeek.com/howto/ubuntu/keep-your-ssh-session-running-when-you-disconnect/)。

### 解决方案四："disown"

据说的最简单方案：在命令后加`&`或者用`ctrl+z`把任务转到后台，然后用`disown -a`将任务解除与当前session的关联（意思就是当前session关闭也不影响它）
