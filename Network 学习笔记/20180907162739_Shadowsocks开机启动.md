# Shadowsocks开机启动
参考了好几篇文章，怎么说的都有，看起来靠谱的不多。最后挑了一个最简单的方法，生效了。[原文在这里](https://www.zybuluo.com/Hederahelix/note/245179)。
编辑`rc.local`开机启动项：
```
sudo vi /etc/rc.local
ssserver -c /etc/shadowsocks.json -d start
```
保存退出，用`sudo reboot`重启，有效。


## 无法通过rc.local开机启动
shadowsocks开机启动一直很好用，直到最近突然不能开机启动了。
在`rc.local`中的命令，复制过来，自己在命令行里输入就没问题。

后来发现，有可能是我把配置文件`shadowsocks.json`放在了用户文件夹`~/`的缘故。
因为按照启动顺序的逻辑，启动到`rc.local`时候，用户文件夹可能还没有加载好，这个时候去引用用户文件夹的内容显然可能会失效。

所以还是把配置文件放到了`/etc/shadowsocks.json`中。
