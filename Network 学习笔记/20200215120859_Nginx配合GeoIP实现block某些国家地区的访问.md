# Nginx配合GeoIP实现block某些国家地区的访问

> 注意：这种地理限制，只会对HTTP／HTTPS生效。对于tcp流量转发一类，这个做不到。

```sh
# 安装数据库及相关的lib
sudo apt-get install geoip-database libgeoip1 libgeoip-dev

# 备份
sudo mv /usr/share/GeoIP/GeoIP.dat /usr/share/GeoIP/GeoIP.dat_bak

# 下载最新的库，只有4k左右 (如果此连接失效，则搜索 "github GeoIP.dat"）
cd /usr/share/GeoIP/
sudo wget https://github.com/maxmind/geoip-api-c/raw/master/data/GeoIP.dat

# 此时目录有：
/usr/share/GeoIP$ ls
GeoIP.dat  GeoIP.dat_bak  GeoIPv6.dat
```

然后需要配置nginx的主配置文件：
```cfg
http {
    # 其它配置...

    # 这个地方只是用来设置 $allowed_country 变量值
    geoip_country /usr/share/GeoIP/GeoIP.dat;
    map $geoip_country_code $allowed_country {
        default no;
        CN yes;
        US no;
    }
    # IF语句必须放在http的server的location里面才行：
    server {
        location / {
            if ($allowed_country = no) {
                return 404;
            }
            # 也可以这么写，更简单直接，连上面的map字典也用不到：
            if ($geoip_country_code = CN) {
                return 404
            }
        }
    }

   # 其它配置...
}
```
