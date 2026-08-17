# Apt-get 的`upgrade`和`dist-upgrade`区别

`upgrade`只是单纯的将各个软件的版本升级到最新，不关心各个软件编译时候的依赖是否更新
`dist-upgrade`则不光让各个软件自身更新，还会检查其依赖，让软件的依赖包也更新到最新版本。

很多时候如果`upgrade`不管用，我们就可以用`dist-upgrade`来试试。
