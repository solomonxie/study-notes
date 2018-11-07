# ❖ Webdav Server Overview 使用总结

尝试了各种各样的Webdav实现，包括Apache版的Webdav Module, Python版的Wsgidav, Docker版的wsgidav, Seafile版的Seadav(其实就是wsgidav)，Nginx版的Webdav等等。

绕来绕去，重新学习各种配置各种框架，到最后还是回到了最初的Apache版。
虽然很多人对Apache不屑，但是就Webdav实现来说，是最稳定也最能受众多平台支持了。

下面指出一些看法：

- Webdav Apache: 需要调配Apache配置，用户权限问题搞不明白会403无权访问。
- Wsgidav：Python版的默认运行极其简单，但是真要配置却需要学很多东西。最重要的是，对Mac和Cyberduck的支持非常非常非常不好，非常不稳定，经常断掉重连，或是重试几次才能连接。
- Seadav：是Seafile基于Wsgidav做的，所以毛病一样。
- Webdav Nginx： 不支持Mac和Cyberduck等，那也就相当于没用了。


在本系统用Apache安装Webdav还是挺方便的，但是感觉上会“搞乱”生产环境，所以不喜欢。
所以就用docker包装起来用，也很方便。唯一的毛病就是docker的内外权限所有权不统一，导致客户端无权写文件。
解决方案就是：先查看Dockerfile中对webdav文件夹的所有权定义，比如www-data。然后到docker外的host中，把webdav文件夹改成一样的www-data，然后就OK了。
即使这个webdav文件夹中还挂载了几个外部磁盘，且磁盘所有者权限也不一样，也没关系。
