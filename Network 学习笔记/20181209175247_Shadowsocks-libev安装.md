# Shadowsocks-libev安装

Shadowsocks服务器分为很多版本，每个版本都同时包含server和client等程序，每个版本所使用的JSON配置文件也都完全一样。不同的只有启动方式、速度、体积、网络处理方式等等。

ss-libev这个版本是C语言写的，体积小速度快。


## 安装

Ubuntu / Debian / 树莓派等安装方法：
```sh
sudo apt-get install -y shadowsocks-libev
```

如果一些平台不支持，则需要自行编译，但是不推荐。
Debian系编译方法如下：
```sh
# Dependencies
yes | sudo apt-get install --no-install-recommends gettext build-essential autoconf libtool libpcre3-dev asciidoc xmlto libev-dev libc-ares-dev automake libmbedtls-dev libsodium-devA && \
echo "[OK]"
mkdir -p ~/local/build_source/
cd ~/local/build_source/
# Installation of libsodium
export LIBSODIUM_VER=1.0.16
wget https://download.libsodium.org/libsodium/releases/libsodium-$LIBSODIUM_VER.tar.gz && \
tar xvf libsodium-$LIBSODIUM_VER.tar.gz && \
pushd libsodium-$LIBSODIUM_VER && \
./configure --prefix=/opt && \
make && sudo make install && \
popd && sudo ldconfig && echo "[OK]"
# Installation of MbedTLS
export MBEDTLS_VER=2.6.0 && \
wget https://tls.mbed.org/download/mbedtls-$MBEDTLS_VER-gpl.tgz && \
tar xvf mbedtls-$MBEDTLS_VER-gpl.tgz && \
pushd mbedtls-$MBEDTLS_VER && \
make SHARED=1 CFLAGS=-fPIC && \
sudo make DESTDIR=/opt install && \
popd && sudo ldconfi && echo "[OK]"

git clone https://github.com/madeye/shadowsocks-libev.git
cd shadowsocks-libev
git submodule update --init --recursive
# Start building
./autogen.sh && \
./configure --prefix=/opt/shadowsocks-libev  && \
make && sudo make install && \
echo "[ OK ]"
```

这个编译步骤目前没法保证都能成功，还要仔细研究。。。


## 配置

配置文件和一般都ss-local方法一样。

shadowsocks-libev的配置文件一般位于：`/etc/shadowsocks-libev/config.json`。
内容参考如下：
```json
{
    "server":"My-Server-IP-Address",
    "server_port": 8888,
    "local_port": 1080,
    "password":"password123",
    "method":"aes-256-gcm",
    "timeout": 10
}
```


## 启动停止方法



和其它版本不同，这个版本比较好操作：

客户端:
```sh
# 前端启动（无需多余参数），停止的话直接Ctrl+C
$ ss-local

# 以后台服务启动

```
