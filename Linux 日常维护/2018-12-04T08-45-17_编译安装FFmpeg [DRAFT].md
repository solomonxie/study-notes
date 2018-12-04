# 编译安装FFmpeg [DRAFT]

[参考官方：Compile FFmpeg for Ubuntu, Debian, or Mint](https://trac.ffmpeg.org/wiki/CompilationGuide/Ubuntu)

编译安装FFmpeg不光是需要编译它本身，还需要编译安装一系列的视频处理器。
基本安装步骤：
- 安装后面编译所需的依赖：`autoconf automake build-essential cmake git-core libass-dev libfreetype6-dev libsdl2-dev libtool libva-dev libvdpau-dev libvorbis-dev libxcb1-dev libxcb-shm0-dev libxcb-xfixes0-dev pkg-config texinfo wget zlib1g-dev`
- 编译安装视频处理器：
    - NASM
    - YASM
    - libx264
    - libx265
    - libvpx
    - libfdk-aac
    - libmp3lame
    - libopus
    - libaom
- 编译安装FFmpeg本身

注意：`lib265`和`libaom`这两个高清编码器，对于树莓派这种小机器来说还是有点费劲了。所以目前也很难找到正确能编译安装上的方式。

```sh
# Download
cd /tmp
wget https://github.com/FFmpeg/FFmpeg/archive/n4.1.tar.gz
tar -xzvf n4.1.tar.gz
cd n4.1*

# Build
./configure --prefix=/opt/ffmpeg-4.1  && echo OK.
make && echo OK.
sudo make install  && echo OK.
```


## MacOS编译问题

### Error: nasm/yasm not found or too old.

查看了下本机的yasm版本`$ yasm --version`，发现是1.3.0。
所以就用homebrew重新安装了一下：
```sh
$ brew instlal yasm
```
得到的版本是1.3.0.1。
