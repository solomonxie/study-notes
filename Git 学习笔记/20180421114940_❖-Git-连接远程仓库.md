#  ❖ Git 连接远程仓库

如果本地已经有了一个repo，想要与远程服务器如Github上的repo建立连接，然后push和pull等，就需要用`git remote`命令操作建立连接。

[参考：阮一峰 Git远程操作详解](http://www.ruanyifeng.com/blog/2014/06/git_remote.html)
[参考：Git Basics - Working with Remotes](https://git-scm.com/book/en/v2/Git-Basics-Working-with-Remotes)

```shell
# 检查现有远程连接，如果没有，则显示空
git remote -v

# 添加远程连接, URL可以是远程repo的http或ssh地址 (先设定为origin)
git remote add origin URL

# 或者修改现有远程URL (这里先设定为origin)
git remote set-url origin URL

# 先与远程同步
git pull origin master

# 提交到远程
git push origin master

# 将本地新建的分之推到远程（远程也新建相应的分之）
git push -u origin <branch>
```

这个时候还不能直接`git push`，因为没有设置默认`push`到远程的`origin master`分支，需要设置默认分支。

[参考：Git push与pull的默认行为](https://segmentfault.com/a/1190000002783245)

```shell
git config push.default simple
```

然后就可以安心的`git push`直接推送到远程的`origin master`了。

更多参考：
[Github Help: Adding a remote](https://help.github.com/articles/adding-a-remote/)
[Github Help: Changing a remote's URL](https://help.github.com/articles/changing-a-remote-s-url/)
