# ❖ Authlib强大OAuth框架入门

基于Python的Authlib是集所有主流WebAPI权限认证协议的客户端、服务端、底层实现、高层架构于一身的强大工具库。

[参考官方：Authlib: Python Authentication](https://docs.authlib.org/en/latest/)

Authlib几乎是能将RFC所有相关的API认证协议都包括进来了，甚至从协议的底层实现、高层架构，从客户端到服务端都能实现的，当之无愧称为`Monolithic project `的一个项目。

目前Authlib支持的Authentication协议有：
- OAuth 1.0
- OAuth 2.0
- JWT
- many more...

安装：
```sh
$ pip install Authlib
```


## Oauth2.0客户端验证

[参考官方：Authlib - Client Guide - OAuth 2 Session](https://docs.authlib.org/en/latest/client/oauth2.html)

Authlib中用来登录验证OAuth2.0的对象叫`Session`，其中包括了所有相关的验证所需方法函数。

```py
from authlib.client import OAuth2Session

# 生成session，用来之后的创建URL、获取token、刷新token等所有动作
session = OAuth2Session(
    client_id='Your Client ID', client_secret='Your Client Secret',
    scope='user:email',  # 这个授权范围根据每个API有所不同
    redirect_uri='https://MyWebsite.com/callback'
)


# 生成URL
uri, state = session.create_authorization_url(
    'https://目标网址的授权入口/authorize'
)
print(uri)

# 「手动」打开浏览器访问URI，登录API帐户，点击授权，然后获取最终的URL
# 或者自己有服务器的话，可以自己接收
#。。。
# 将callback返回的URL复制下来，因为其中包含授权code
authorization_response = 'https://MyWebsite.com/callback?code=42..e9&state=d..t'

# 用获得的Code去访问access_token入口
tokens = session.fetch_access_token(
    access_token_url='https://目标网址的授权入口/api/access_token',
    authorization_response=authorization_response
)
print(tokens)  #返回字典格式: {'access_token': 'e..ad', 'token_type': 'bearer', 'scope': 'user:email'}


# 过期后，刷新token。需重建session对象：
session = OAuth2Session(
    client_id='Your Client ID', client_secret='Your Client Secret',
    scope='user:email', state=state, redirect_uri='https://MyWebsite.com/callback'
)
new_tokens = session.refresh_token(
    access_token_url, refresh_token=tokens['refresh_token']
)
print('[Refreshed tokens]:', new_tokens)

```

## 设置的callback或redirect_url不存在怎么获取Code？

在调试过程中，如果我们向上面一样手动去打开浏览器复制URL，再复制回应过来的URL是很麻烦的。

Oauth2的逻辑就是：要求各种客户自己在自己的浏览器里登录帐户，然后给你的App授权。所以这一步redirect_url是躲不过的。但是我们测试过程中，还没来得及专门建一个服务器或网页来接收这个callback回调怎么办呢？
有办法！

### 方法一：直接截取

我们可以在第一次登录并授权后，复制cookies，然后在测试中直接使用requests带着cookies登录信息去访问，就不再需要手动打开浏览器了：
```py
raw_cookies = """ 这里是你复制过来的cookies """
cookies = dict([line.split("=", 1) for line in raw_cookies.strip().split("; ")])

try:
    r = requests.get(uri, cookies=cookies, allow_redirects=True)
except requests.exceptions.ConnectionError as e:
    print( '[Final URL]: ', e.request.url )
    authorization_response = e.request.url
```
由于你最开始设置的`callback`是公网上的某个网址，应该是不存在的（只要你没有设置的话）。
所以，这里去request的时候，肯定会报错，且是`ConnectionError`。所以我们可以将最终报错的URL获取到，这个里面就包含了我们想要的`Code`码。


### 方法二：更改本地hosts

如果本地已经搭建了测试服务器，比如Nginx或Flask，这种方法更简单。

比如在供应商中设定的redirect_url为`http://example.com/callback`，那么只需简单编辑hosts:
```
# /etc/hosts

127.0.0.1   example.com
```

那么，只要本机设置了Nginx或Flask等服务器，只需要获取`127.0.0.1/callback`即可得到需要的内容。
