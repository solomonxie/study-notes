# ❖ ffmpeg 超强视频处理程序 [DRAFT]

> 开源视频处理几乎必用的一个程序，功能强大。

## Installation

```
# for Ubuntu 14.04 (no need to install on 15.04)
sudo add-apt-repository ppa:mc3man/trusty-media
sudo apt-get update
sudo apt-get dist-upgrade
sudo apt-get install ffmpeg -y
```

## 以最低CPU优先率执行命令

```
nice -19 ffmpeg 各种参数
```


## mp4 to mp3
```sh
# 
$ ffmpeg -i <FILE> -vn <OUT>
```



## .webm to .mp4

```
nice -19 ffmpeg -i input.webm -c:v libx264 -crf 20 -c:a aac -strict experimental out.mp4
```

## Split Video

```
# 不转码截取片段（）
nice -19 ffmpeg -i "input.mp4" -ss 00:03:25 -to 00:05:42 -c copy "output.mp4"
```

## 调整音频与视频匹配不上的问题

### 方法1

```
nice -19 ffmpeg -i "input.mp4" -itsoffset 2.0 -i "input.mp4" -vcodec copy -acodec copy -map 0:0 -map 1:1 "output.mp4"
```

### 方法2: 一开始就分开截取音频视频 然后再合并

```
# ...
```

ffmpeg的参数顺序很重要, 不同的顺序造成截然不同的结果

## 切割视频

```
# 从指定开始点到指定结束点
ffmpeg -i 文件名 -ss 01:00:00 -t 00:06:00  -vcodec copy -acodec copy 输出文件名
ffmpeg -i 文件名 -ss 00:01:00 -to 00:02:00 -c copy 输出文件名
# 从指定开始点到指定时长
ffmpeg -ss 00:01:00 -i 文件名 -to 00:02:00 -c copy 输出文件名
# 调整音频匹配不上的问题 #方法1
ffmpeg -i "test.mp4" -itsoffset 2.0 -i "test.mp4" -vcodec copy -acodec copy -map 0:0 -map 1:1 "new.mp4"

# 调整音频匹配不上的问题 #方法2: 一开始就分开截取音频视频 然后再合并
# 
```
