# 网络网站连不同的诊断方法

## `Hosts`大法
`/etc/hosts`文件的语法格式：
```
[Target-IP] [Target-URL] [Alias]

# IP和URL关联指定
220.181.57.216 baidu.com

# 给某ip起别名（注意：中间是两个空格，代表忽略了target-url）
192.168.199.111   pi.local
```

因为hosts支持注释和自由缩进，所以为了方便查看，我们还可以这样写：
```
# Jianshu {
    180.150.186.235 jianshu.com
    70.39.191.89 cdn2.jianshu.io
# }

# Douban {
    123.125.7.219 *.doubanio.com 
# }

# AWS {
    # *.aws.amazon.com {
        #54.239.96.98 *.aws.amazon.com
    # }
    # console.aws.amazon.com {
        #54.239.96.98 console.aws.amazon.com
    # }
    # lightsail.aws.amazon.com {
        #54.239.96.98 lightsail.aws.amazon.com
        #52.95.193.21 lightsail.aws.amazon.com
        54.239.96.82 lightsail.aws.amazon.com

        #52.95.18.74 us-east-2.lightsail.aws.amazon.com
        52.95.16.89 us-east-2.lightsail.aws.amazon.com

        #52.94.104.110 ca-central-1.lightsail.aws.amazon.com
        221.130.32.116 ca-central-1.lightsail.aws.amazon.com
    # }
# }
```

Troubleshoot strategy:

1. Use Chrome DevTool to checkout which resources can't be load
2. Ping each site contains those recourses
3. Use online DNS lookup to find a fast target IP (Big corps like oogle 
4. Ping and test the target IP
5. Redirect the recources site url to the target IP we have found.
6. Test browsing in chrome (Turn off all vpn)
