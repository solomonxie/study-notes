# ❖ Mac安装包管理器MacPorts：从入门到放弃

## 安装

MacPorts的pkg安装包经常遇到的问题是：卡住不动。不用想也知道是网络问题。

不过经过多次尝试，最好的做法还是直接自己编译：

```sh
# Download
cd /tmp
sudo curl -O https://distfiles.macports.org/MacPorts/MacPorts-2.5.4.tar.bz2
sudo tar xf MacPorts-2.5.4.tar.bz2

# Build
cd MacPorts-2.5.4/
./configure --prefix=/opt/macports-2.5.4   && echo "[ OK ]"
make   && echo "[ OK ]"
sudo make install   && echo "[ OK ]"

# Export Path or Create symlink
echo "export PATH=/opt/local/bin:/opt/local/sbin:$PATH" >> ~/.bash_profile
# or
ln -s /opt/local/bin/port /usr/local/bin/port
```


更新：
```sh
sudo port selfupdate
```

安装：
```sh
sudo port install ffmpeg
```



## 体积

在都还没装什么软件的时候（只装了一个ffmpeg），整个macports的目录就高达3.5GB，这个在MBA笔记本上来说实在是太重了！而且编译一个ffmpeg，用了半个小时还没完成，这实在是匪夷所思。
注：和网络没关系，镜像已经设为了国内的。看时间卡住的，纯在Build上。

想着，既然安装一个都这么费劲，还不如自己compile。
