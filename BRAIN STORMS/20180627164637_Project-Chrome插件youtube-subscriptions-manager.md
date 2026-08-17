# Project: Chrome插件youtube subscriptions manager

代替现在流行的youtube collections管理器——太手动了。。。全部靠手动选择，且不会根据自己的订阅更新和取消——和自己管理bookmarks标签完全没区别。

首先需要做到这个功能：
- [ ] 自动读取当前用户的所有订阅（直接爬取当前网页的侧边栏，比api更快）
- [ ] 不是每次加载网页都读取侧边栏的订阅，而是每天或定期更新。（减少网页压力）
- [ ] 根据youtube channel 自动分类：math、tech、gadget等等，也可以自己修改
- [ ] 在网页的侧边栏自动显示（和youtube collections一样）
- [ ] 自动读取rss（youtube.com/subscriptions_manager 里面有rss）
- [ ] 根据rss，可以点击出一个popup页面显示当前所有更新，按浏览量排序
- [ ] 订阅按照自己的点击量或history排名
- [ ] history导出（api虽然方便但是授权会比较让人拒绝）直接后台爬取更好，页面不会太多。而且增量爬取，压力不大。


## 更新
重点是无需授权等等，完全根据当前网页内容分析。如果已经登录了，就自动匹配本地的管理记录。

