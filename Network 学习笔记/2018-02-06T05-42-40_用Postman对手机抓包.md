# 用Postman对手机抓包
一般人会抓头，Postman明明是API调试工具，和抓包有什么关系。其实这也就是官方对一个小tip，本身存在是为了监控本机某端口数据包的。但其实，如果指定某一个监视端口，然后让同局域网的手机通过这台电脑的这个端口联网而已。这样的话Postman就间接监控到了手机数据包。
操作没有任何难度，主要就是大家对手机将电脑视为代理连接比较陌生罢了。注意：不是让电脑开启热点充当wifi，而是手机本身已经连了wifi时设置代理为电脑而已。
具体操作在[Postman官网博客中](http://blog.getpostman.com/2016/06/26/using-postman-proxy-to-capture-and-inspect-api-calls-from-ios-or-android-devices/)
