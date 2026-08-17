# ❖ Ubuntu用Nginx服务器安装WebDav共享盘（NAS）

```sh
# 安装Nginx服务器（连带所有扩展包，其中包括WebDav扩展）
sudo apt update
sudo apt install  nginx-full

# 开始编辑Nginx服务器总配置
sudo vim /etc/nginx/nginx.conf
```

在`nginx.conf`中，替代为以下内容：
```nginx

user www-data;
worker_processes 4;
pid /run/nginx.pid;

events {
    worker_connections 768;
    # multi_accept on;
}

http {

    ##
    # Basic Settings
    ##

    sendfile on;
    tcp_nopush on;
    tcp_nodelay on;
    keepalive_timeout 65;
    types_hash_max_size 2048;
    # server_tokens off;

    # server_names_hash_bucket_size 64;
    # server_name_in_redirect off;

    include /etc/nginx/mime.types;
    default_type application/octet-stream;

    ##
    # SSL Settings
    ##

    ssl_protocols TLSv1 TLSv1.1 TLSv1.2; # Dropping SSLv3, ref: POODLE
    ssl_prefer_server_ciphers on;

    ##
    # Logging Settings
    ##

    access_log /var/log/nginx/access.log;
    error_log /var/log/nginx/error.log;

    ##
    # Gzip Settings
    ##

    gzip on;

    gzip_vary on;
    gzip_proxied any;
    gzip_comp_level 6;
    gzip_buffers 16 8k;
    gzip_http_version 1.1;
    gzip_types text/plain text/css application/json application/javascript text/xml application/xml application/xml+rss text/javascript;

    ##
    # Virtual Host Configs
    ##

    include /etc/nginx/conf.d/*.conf;
    include /etc/nginx/sites-enabled/*;
}
```

然后再创建一个`/etc/nginx/conf.d/0-webdav.conf`文件，并写入内容：
```nginx
$ sudo vim /etc/nginx/conf.d/0-webdav.conf

# 写入以下内容

server {
    listen 80;
    listen [::]:80;

    server_name plans.helenshydrogen.be;

    auth_basic              realm_name;
    auth_basic_user_file    /etc/nginx/.passwords.list;

    dav_methods     PUT DELETE MKCOL COPY MOVE;
    dav_ext_methods PROPFIND OPTIONS;
    dav_access      user:rw group:rw all:r

    client_body_temp_path   /tmp/nginx/client-bodies;
    client_max_body_size    0;
    create_full_put_path    on;

    root /home/pi/webdav-share;
}
```

然后创建用户和密码：
```sh
echo -n 'pi:' | sudo tee /etc/nginx/.passwords.list
openssl passwd -apr1 | sudo tee -a /etc/nginx/.passwords.list
```

测试和启动nginx：
```sh
# 测试配置是否通过
$ sudo nginx -t

# 启动Nginx
$ sudo nginx
```

（未完待续）
