# Project: 自制客户端或改进shadowsocks客户端或改chrome插件proxyswitch

其实在国内最主要的需求是：让所有IP在国内的站点走本地网络，只有国外的站点走VPN。
这样就全解决了。
但是怎么没人做呢？

也不用每个网页的所有资源都ping一遍，如果本地存有ip或hosts数据库，可以直接使用了。数据库里没有的再ping一下，加入到数据库中，也不会太慢。
总之这样就省去了很多手动添加gfw被屏蔽网址的时间。

目前市面上已有的相关方案和技术：
- [COW](https://github.com/cyfdecyf/cow)
- shadowsocks-libev
- [GeoIP](https://www.maxmind.com/en/geoip-demo)


