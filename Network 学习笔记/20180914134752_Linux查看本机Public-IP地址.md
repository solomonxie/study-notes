# Linux查看本机`Public IP`地址
用不着什么命令行工具，直接用`curl`访问一些ip检测的网页就ok了。
比如：
```
curl ipinfo.io/ip
```
或者更常用的httpbin：`curl httpbin.org/ip`
