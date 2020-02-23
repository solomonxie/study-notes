# Mac 安装Shadowsocks算法依赖


## libsodium依赖


默认Homebrew安装`libsodium`经常会在下载源码包的时候卡住下载不动，因为源码会从libsodium官网去下，官网速度非常慢。

参考：https://bin.zmide.com/?p=408

```sh
wget https://github.com/jedisct1/libsodium/releases/download/1.0.18-RELEASE/libsodium-1.0.18.tar.gz
tar xzvf libsodium*.tar.gz
cd libsodium*
./configure
make -j8 && make install
pip install https://github.com/shadowsocks/shadowsocks/archive/master.zip --user
```


## 更好的方法是homebrew

```sh
# 在外网的环境下安装（需要代理）
# ...

$ brew install shadowsocks-libev
```
