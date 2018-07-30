# wget 常用命令

[参考：wget命令](http://www.cnblogs.com/peida/archive/2013/03/18/2965369.html)

```sh
# 下载多个链接 --input-file
$ wget -i List.txt

# 下载到指定目录 --directory-prefix
$ wget <url> -P ./folder

# 强制按照url的层级结构，创建多层目录 --force-directories
$ wget <url> -x

# 不覆盖已有文件 --no-clobber
$ wget <url> -nc 

# 输出log下载日志 小写o，--output-file
$ wget <url> -o logname

# 保存文件为指定的名字 大写O， --output-document
$ wget <url> -O filename

# 限速下载
$ wget <url> --limit-rate 300k

# 每次下载都等待3秒
$ wget <url> --wait 3

# 每次下载随机等待0~2秒之间
$ wget <url> --random-wait

# 每次重新连接retry时等待1秒
$ wget <url> --waitretry 1

# 响应超时为5秒 --timeout
$ wget <url> -T 5

# 打印调试输出 --debug
$ wget <url> -d
# 不输出信息 --quiet
$ wget <url> -q
```


