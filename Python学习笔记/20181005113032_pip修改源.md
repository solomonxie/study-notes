# pip修改源

有很多pip源都非常慢，所以有必要改用国内的源。

常用源有：
- 豆瓣：http://pypi.douban.com/ 
- 阿里云：http://mirrors.aliyun.com/pypi/simple/
- 中国科学技术大学：http://pypi.mirrors.ustc.edu.cn/simple/ 

临时性指定源：
```sh
$ pip install <package> -i <源地址> -- trusted-host <源服务器>

#如
$ pip install Flask -i http://pypi.douban.com/simple -- trusted-host pypi.douban.com
```

永久性修改源，需要创建一个`~/.pip/pip.conf`文件，内容如下：
```
[global]
trusted-host=mirrors.aliyun.com
index-url=http://mirrors.aliyun.com/pypi/simple/
```
