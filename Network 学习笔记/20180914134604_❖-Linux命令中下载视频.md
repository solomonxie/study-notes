# ❖ Linux命令中下载视频

## 「youtube-dl」 支持站点 1000+
最强大的命令行下载器，支持1000+网站，几乎包含了**所有国家**的**所有主流**视频网站。

> 常用支持站点：
Youtube, facebook, ESPN, Instagram, 土豆，优酷，bilibili，CCTV，音悦台，爱奇艺，搜狐，网易云音乐，虾米音乐，QQ音乐
[参考youtube-dl源代码。](https://github.com/rg3/youtube-dl/tree/master/youtube_dl/extractor)目录下有很多extractor脚本，每个脚本代表一个视频网站。
[参考：Supported sites](https://rg3.github.io/youtube-dl/supportedsites.html)

安装：
```sh
$ pip install youtube-dl
```

## 下载方法

最简单下载方式 (默认下载最高清的)：
```sh
$ youtube-dl <URL>
```

最常用下载方式：
```sh
$ youtube-dl -civw -f bestvideo+bestaudio  --proxy "localhost:1080" <URL>
```

通过代理下载：
```sh
$ youtube-dl --proxy "http://localhost:1080" <URL>
```

根据不同分辨率下载：
```sh
# 下载所有分辨率
$ youtube-dl  --all-formats <URL>

# 查看所有分辨率选项（不下载）
$ youtube-dl --list-formats

# 根据分辨率ID编号，比如2090989834555288v，选择下载：
$ youtube-dl -f 2090989834555288v <URL>

# 下载最高清视频中音频质量最好的（视频本身不一定最清楚）
$ youtube-dl -f bestvideo+bestaudio <URL>
# 或下载mp4格式和m4a格式质量最高选项
$ youtube-dl -f 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best'

# 下载最高清视频和最高质音频并合并（Youtube的高清视频都是音频视频分离的）
$ youtube-dl -f 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/bestvideo+bestaudio' --merge-output-format mp4<URL>
```

常用附加选项：
```sh
# 最常用选项：断点续传c、忽略错误i、显示全部信息v、不覆盖已有文件w
$ youtube-dl -civw <URL>

# 强制覆盖
$ youtube-dl --no-continue <URL>

# 生成Description文件 （如果有支持的视频描述，则生成描述文件）
$ youtube-dl --write-description  <URL>
```

### 下载列表
```sh
# 默认下载全列表 (断点续传、忽略错误）
$ youtube-dl -ci <URL>

# 从第3个视频开始下载列表
$ youtube-dl --playlist-start 3 <URL>

# 从文件读取多视频链接
$ youtube-dl --batch-file='~/URL-LIST.txt'
```

### 下载字幕
```sh
# 只下载字幕不下载视频
$ youtube-dl --all-subs --write-auto-sub --skip-download https://youtu.be/3mhx5XUYmGw
```


### 配置文件
每次都输入一大串参数很麻烦，所以可以把常用的写到配置文件里。默认位于`~/.config/youtube-dl/config`。

**还好youtube-dl的配置文件中没有什么语法，参数使用完全和命令行里相同！**

创建`~/.config/youtube-dl/config`文件，然后输入：
```
# 使用代理
--proxy 127.0.0.1:1080

# 默认保存到指定文件夹，且保存为指定格式文件名
-o ~/Movies/%(title)s.%(ext)s
```


## 授权文件
Linux很多程序都采用`~/.netrc`授权文件，保存一些网站的用户名、密码等信息，这样程序就能自动登录并下载了。

创建授权文件：
```sh
$ touch $HOME/.netrc
$ chmod a-rwx,u+rw $HOME/.netrc
```

授权文件语法：
```
machine youtube login myaccount@gmail.com password my_youtube_password
machine twitch login my_twitch_account_name password my_twitch_password
```

## 「you-get」 支持站点 ~100

对国内支持比较好，国内视频下载速度极快（比youtube-dl快很多倍），使用方便，语法简单。

> 支持：YouTube, Twitter, VK, Vine, Vimeo, Vidto, Videomega, Veoh, Tumblr, TED, SoundCloud, SHOWROOM, Pinterest, MusicPlayOn, MTV81, Mixcloud, Metacafe, Magisto, Khan, Academy, Internet, Archive, Instagram, InfoQ, Imgur, Heavy, Music, Archive, Google+, Freesound, Flickr, FC2, Video, Facebook, eHow, Dailymotion, Coub, CBS, Bandcamp, AliveThai, interest.me, 755, ナナゴーゴー, niconico, ニコニコ動画, 163, 网易视频, 网易云音乐, 56网, AcFun, Baidu, 百度贴吧, 爆米花网, bilibili, 哔哩哔哩, Dilidili, 豆瓣, 斗鱼, Panda, 熊猫, 凤凰视频, 风行网, iQIYI, 爱奇艺, 激动网, 酷6网, 酷狗音乐, 酷我音乐, 乐视网, 荔枝FM, 秒拍, MioMio弹幕网, 痞客邦, PPTV聚力, 齐鲁网, QQ, 腾讯视频, 企鹅直播, Sina, 新浪视频, 微博秒拍视频, Sohu, 搜狐视频, Tudou, 土豆, 虾米, 阳光卫视, 音悦Tai, Youku, 优酷, 战旗TV, 央视网, 花瓣, Naver, 네이버, 芒果TV, 火猫TV, 全民直播, 阳光宽频网, 西瓜视频, 快手, 抖音

安装：
```sh
$ pip install -U you-get
```

## 下载方法
最简单下载方式：
```sh
$ you-get <URL>
```

最常用下载方式：
```sh
$ you-get -x localhost:1080 <URL>
```

通过代理下载：
```sh
$ you-get -x localhost:1080 <URL>
```

根据不同分辨率下载：
```sh
# 查看可选分辨率（不会开始下载）：
$ you-get -i <URL>

# 根据选项编号，比如itag=18，选择下载：
$ you-get --itag=18 <URL>
```


