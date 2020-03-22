# Nginx 部署静态网页

参考：https://showzeng.itscoder.com/nginx/2016/10/03/use-nginx-to-deploy-static-pages-easily.html
参考：https://blog.csdn.net/lizhiyuan_eagle/article/details/90639448
参考：https://juejin.im/post/5d7b72b7e51d453b386a63bc

```conf
http {
    server {
        listen       8080;
        server_name  localhost;

        location / {
             root   /var/www/html;
             index  index.html index.html;
        }

        location /sub {
             alias   /path/to/some-other-name;  # 注意这里二级目录一定要用alias而不是root，否则404
             index  index.html index.html;
        }
    }
}
```
