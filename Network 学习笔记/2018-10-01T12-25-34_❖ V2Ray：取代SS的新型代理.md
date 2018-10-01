# ❖ V2Ray：取代SS的新型代理

> 自从这几天自建的Shadowsocks不断被断线，就开始找解决方案。发现原来“官方”已经有了攻破方案还发了论文了。所以就在搜替代方案。
然后，谷歌给的答案只有一个——`V2Ray`。

仔细阅读了文档，发现真的是个新时代的好东西。真的可以取代Shadowsocks，不光创造了自己的协议`Vmess`，还可以兼容Shadowsocks协议。也就是说你也可以安装v2ray来实现shadowsocks的一切，而且还具备更多的属性。

这里就简单研究一下吧。

[参考官方白话：V2Ray 配置指南](https://toutyrater.github.io/)

数据的双向传输过程如下(最好仔细看看，明白这个流程就都明白了)：
```
{浏览器} <--(socks)--> {V2Ray 客户端 inbound <-> V2Ray 客户端 outbound} <--(VMess)-->  {V2Ray 服务器 inbound <-> V2Ray 服务器 outbound} <--(Freedom)--> {目标网站}
```

## 安装
> 这里就不讲客户端安装了，各个客户端都有GUI很容易。主要就是服务器需要用命令行安装下。


官方一键安装脚本：
```sh
$ sudo su
$ bash <(curl -L -s https://install.direct/go.sh)
```
（注意，这里一定不要用`sudo`，必须要切换到root账户，否则会发生错误无法识别当前用户的错误）



启动停止方法：
```sh
# 启动
$ sudo systemctl start v2ray
# 或
$ sudo /usr/bin/v2ray/v2ray -config /etc/v2ray/config.json

# 停止
$ sudo systemctl stop v2ray

# 重启
$ sudo systemctl restart v2ray

# 查看运行状态
$ sudo systemctl status v2ray
```



## 推荐配置

[参考官方白话入门：VMess](https://toutyrater.github.io/basic/vmess.html)

需要了解的有这么几点：
- 服务端的outbound是服务器访问目标网站，没有什么限制，所以是`freedom`协议，“直连”的意思。
- `alterId`必须与客户端**相同**。这个参数是加强防探测能力的，越大越好（越占内存），一般30-100之间合适，64就够用。
- `id`相当于随机密码，用的`uuid`格式，随便改。

官方推荐的最简配置（其它什么都不用改，只要改个IP地址即可）如下：
（注意，配置中的注释需要删掉，因为JSON不支持注释）


### 服务端默认配置
安装好程序后，服务器的配置文件为`/etc/v2ray/config.json`：
```json
{
  "inbound": {
    "port": 16823, //服务器监听端口
    "protocol": "vmess",    //主传入协议
    "settings": {
      "clients": [
        {
          "id": "b831381d-6324-4d53-ad4f-8cda48b30811",  //用户ID,客户端与服务器必须相同
          "alterId": 64
        }
      ]
    }
  },
  "outbound": {
    "protocol": "freedom",  //主传出协议
    "settings": {}
  }
}
```


### 客户端默认配置

> 其实客户端一般不用自己写配置，设备上都是用GUI客户端的。但是树莓派这种只有命令行的，那就需要了。

```json
{
  "inbound": {
    "port": 1080, //监听端口
    "protocol": "socks", //入口协议为SOCKS-5
    "domainOverride": ["tls","http"],
    "settings": {
      "auth": "noauth"  //Socks的认证设置,noauth 代表不认证,由于socks通常在客户端使用,所以这里不认证
    }
  },
  "outbound": {
    "protocol": "vmess", //出口协议
    "settings": {
      "vnext": [
        {
          "address": "serveraddr.com", //服务器地址,请修改为你自己的服务器IP或域名
          "port": 16823,  // 服务器端口
          "users": [
            {
              "id": "b831381d-6324-4d53-ad4f-8cda48b30811",  //用户ID,必须与服务器端配置相同
              "alterId": 64 //此处的值也应当与服务器相同
            }
          ]
        }
      ]
    }
  }
}
```


## 数据包伪装

[参考：高级篇](https://toutyrater.github.io/advanced/)

Shadowsocks当年可是据称最靠谱的协议，没人知道你从哪来去哪里，内容完全隐藏。但是这反而成了最大的缺点：把自己裹这么严实的肯定有问题，所以见一个封一个。

V2Ray最重要的就是解决了这个问题：能把一个数据包伪装称HTTP网页流，或BT下载流、视频通话流等。做法就是给数据包加上header，包装成正常的数据。


### 伪装成HTTP包

[参考：TCP 传输方式](https://www.v2ray.com/chapter_02/transport/tcp.html)

`"header"`是加到服务器`/etc/v2ray/config.json`中的， 和`inbound`, `outbound`同级，一般放在后面即可。

`type`为伪装的数据类型，一般有：
- `none`: 没有，这样的话就和shadowsocks没什么区别了，容易被查出来
- `http`: 最常用，只是在每个包上包了一层`user-agent`，像是一个手机在浏览网页一样。

```json
"header": {
  "type": "http",
  "request": {
    "version": "1.1",
    "method": "GET",
    "path": ["/"],
    "headers": {
      "Host": ["www.baidu.com", "www.bing.com"],
      "User-Agent": [
        "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 10_0_2 like Mac OS X) AppleWebKit/601.1 (KHTML, like Gecko) CriOS/53.0.2785.109 Mobile/14A456 Safari/601.1.46"
      ],
      "Accept-Encoding": ["gzip, deflate"],
      "Connection": ["keep-alive"],
      "Pragma": "no-cache"
    }
  },
  "response": {
    "version": "1.1",
    "status": "200",
    "reason": "OK",
    "headers": {
      "Content-Type": ["application/octet-stream", "video/mpeg"],
      "Transfer-Encoding": ["chunked"],
      "Connection": ["keep-alive"],
      "Pragma": "no-cache"
    }
  }
}
```



## 使用感受

目前来讲，感受速度没有变快（一般是比原生SS更慢）。而且也不知道是不是我的混淆配置没有弄好，断线频率也比较高，比没有混淆的SS高很多。

而且，V2Ray的学习成本太高了，网上文档也不够多，想学都学不好。连学带倒腾了几天，还没弄出个所以然。加上速度和体验也没有那么棒，就放弃了。
