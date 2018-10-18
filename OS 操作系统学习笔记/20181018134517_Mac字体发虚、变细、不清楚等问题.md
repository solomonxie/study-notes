# Mac字体发虚、变细、不清楚等问题

Mac一直保持不关机状态，总是盖上盖子就可以了。然后几个月以来，操作了很多东西，都没有直接反应，直到重启了一次才发现问题层出不穷。

这次主要发现的是字体问题，原本没事的，结果连命令行的字体都调整不过来。我用的iTerm2，不管怎么设置字体都是看上去很奇怪都样子，很难看。

试了很多方法都不好使，比如：
[参考：更改系统默认字体](https://laoshuterry.gitbooks.io/mac_os_setup_guide/content/3_ChangeDefaultFont.html)
和
[参考：如何排查Mac OS X上的字体问题](https://blogs.adobe.com/CCJKType/2009/08/troubleshoot.html)

然后用了一个简单的方法：直接打开Mac的`Font Book`，然后点击File -> restore...，把字体全部还原到初始状态，删除所有后装的字体。然后重启一下，就好了。

以后再也不用什么乱七八糟的软件比如`Right font`等在机器上装字体了，各种捣乱。
