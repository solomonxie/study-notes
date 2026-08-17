# Cmake入门 [DRAFT]

Cmake是一个编译程序。

目前官方推荐的安装方法只有编译安装，Mac／Linux都是一样。

[参考官方：Installing CMake](https://cmake.org/install/)

```sh
# Download
cd /tmp
wget https://github.com/Kitware/CMake/releases/download/v3.13.1/cmake-3.13.1.tar.gz
tar -xzvf cmake-3.13.1.tar.gz
cd cmake-3.13.1.tar.gz

# Build
./bootstrap
make
make install
```

当然，已经有很多包管理器可以一键安装。

Mac：
```sh
brew install cmake
```
