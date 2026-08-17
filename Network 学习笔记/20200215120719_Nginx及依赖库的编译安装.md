# Nginx及依赖库的编译安装

参考：https://segmentfault.com/a/1190000014783064
参考：http://nginx.org/en/docs/configure.html
参考：https://www.mgchen.com/251.html

安装顺序是：
- 编译安装依赖
    - PCRE
    - OpenSSL
    - Zlib
- 编译安装Nginx
    - 安装其它依赖库
    - 指定依赖库的路径时，不是指定安装位置，而是**`源码位置`**


```sh
cd /tmp

# 安装PCRE, 官方下载列表：https://ftp.pcre.org/pub/pcre/
# 注意：一定不要选PCRE版本2xx，因为会在nginx安装时候出错
wget https://ftp.pcre.org/pub/pcre/pcre-8.36.tar.gz
tar -xzvf pcre-8.36.tar.gz

# 安装OpenSSL, 官方下载列表：https://www.openssl.org/source/:
wget https://www.openssl.org/source/openssl-1.1.0g.tar.gz
tar -xzvf openssl-1.1.0g.tar.gz

# 安装Zlib, 官方下载列表：http://www.zlib.net/
wget https://downloads.sourceforge.net/project/libpng/zlib/1.2.11/zlib-1.2.11.tar.gz
tar -xzvf zlib-1.2.11.tar.gz
```

安装其它依赖包：
```sh
# GeoIP 模块
sudo apt-get install libgeoip-dev -y

#  HTTP XSLT 模块
sudo apt-get install libxslt-dev -y
```

安装Nginx，并指定某些依赖包的位置：
```sh
cd /tmp
# 官方下载列表：https://nginx.org/en/download.html
wget https://nginx.org/download/nginx-1.16.1.tar.gz
tar -xzvf nginx-1.16.1.tar.gz
cd nginx-1.16.1

# 开始编译安装
./configure \
--prefix=/usr/local/nginx \
--conf-path=/usr/local/nginx/conf/nginx.conf \
--http-log-path=/usr/local/nginx/logs/access.log \
--error-log-path=/usr/local/nginx/logs/error.log \
--lock-path=/usr/local/nginx/nginx.lock \
--pid-path=/usr/local/run/nginx.pid \
--with-debug \
--with-pcre-jit \
--with-http_ssl_module \
--with-http_stub_status_module \
--with-http_gzip_static_module \
--with-http_realip_module \
--with-http_auth_request_module \
--with-http_addition_module \
--with-http_dav_module \
--with-http_geoip_module \
--with-http_gunzip_module \
--with-http_v2_module \
--with-http_sub_module \
--with-http_xslt_module \
--with-stream \
--with-stream_ssl_module \
--with-mail \
--with-mail_ssl_module \
--with-threads \
--with-file-aio \
--with-pcre=/tmp/pcre-8.36 \
--with-openssl=/tmp/openssl-1.1.0g \
--with-zlib=/tmp/zlib-1.2.11 \
&& make && make install && echo OK.

# 为了用起来方便，可以改下权限，省去sudo：
sudo chown -R ubuntu:ubuntu /usr/local/nginx/
```

注意：
- 上面configure里面没有指定`rewrite`和`openssl`等模块是因为，这些模块都是编译时候默认安装的，如果不想要可以用`--without-http_rewrite_module`来代替。
- 指定模块安装路径时候结尾一定**不要**带`/`，正确的是：`-with-pcre=/tmp/pcre-8.36`
- 路径中不要用`~`，而是用展开的全路径，否则默写依赖模块不能识别
- 如果安装中断报错：`src/core/ngx_regex.h:15:18: fatal error: pcre.h: No such file or directory`，那么说明PCRE版本问题。不要用PCRE版本2xx，直接选用`pcre-8.36`即可。
- 记得在nginx.conf里面调用的文件，最好也指定自己有权限的文件，这样就不用任何sudo了

