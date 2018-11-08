# Project: `Free-Spotify` or `Spoilfy`

在自己的服务器上建立一个类似Spotify的在线听歌网站，像Emby一样的服务器，但是和Spotify更贴合。
本质上是一个`私有云`，不对外公开的。所以不太涉及版权问题。

参考同类产品：
- Emby
- OwnCloud
- NextCloud
- Seafile

利用Spotify API，读取用户的所有信息，备份到自己的服务器，生成和SPotify一样的界面。一边提供了备份的功能，一边提供在线听歌。

问题在于，歌曲的来源问题。需要用户自己去下载，然后上传到服务器。然后，`Free-Spotify`会自动识别歌曲(MusicBrainz)，让你听。不用手动一首一首去对应。
这样一来，就算无法连接spotify，还是可以听自己标记过的歌和playlist。

由于歌太多，自己一个一个去搜索下载太麻烦。所以系统会生成一个列表：告诉你现在还缺哪些歌手的哪些专辑需要下载。默认的话可以直接自动搜索youtube上的歌并播放出来，这样甚至不需要上传歌也没有版权问题。像`Whatsthesong`一样。

涉及技术问题：
- [x] Spotify API （Python）
- [ ] MusicBrainz自动识别local歌曲并匹配Spotify中的歌曲
- [ ] Python后端的HTTP服务器
- [ ] Youtube歌曲搜索（很难匹配上准确的）


## 更新
来源问题：
Spotify API其实提供每首歌的30秒预览，足够一般浏览了，这样能够快速填充实际内容。
然后再配合本地歌曲库来补充，那么就非常完善了。
也就是说，本地有的，直接听全曲。本地没有的，提供30s预览，并提示用户自行去下载（提示需要下载的artist和album），并提供youtube搜索结果链接。

推荐问题：
推荐其实也不需要自己构建了，API中有Recommandation，和主页的大众推荐。那么就相当于Spotify的所有功能都有了。

也就是说，可以完全完全完全模拟一个Spotify，然后再其之上增加个人数据的导入导出，再加上本地音乐的完全可控，个人服务器运行，就是一个非常讨喜的在线音乐播放平台了。

家庭音乐共享到公网：
数据库存在本地的Webdav中，配合frp连接，公网服务器建立一个网页，读取家里音乐库，这样就达成了统一。


## 更新
Youtube等歌曲来源问题，可以通过这个库解决：`Track`（http://developers.music-story.com/developers/track）
![image](2018-11-08T14-44-23_Project `Free-Spotify` or `Spoilfy`_files/img_01.png)

