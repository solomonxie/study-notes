# ❖ Linux安装Shadowsocks客户端

有时候想让树莓派等Linux机也用shadowsocks，这时就没有GUI客户端用了。
所以我们直接使用Shadowsocks官方命令行客户端：`sslocal`。

## 安装、配置、启动
安装：
```sh
# 服务端和客户端都包括了
$ sudo pip install shadowsocks
```

启动客户端：
```sh
# 连接IP为54.254.184.22 端口为2222的服务器，映射到本地1080端口
# 格式为：sslocal -s 服务端IP  -p 服务端端口 -l 1080 -k "密码" 回车
$ sslocal -s 54.254.184.22 -p 2222  -l 1080 -k "PASSWORD" -t 600 -m aes-256-cfb
```

这样启动其实听不方便的，而且还占用命令行，不能断开。
所以我们用配置文件+start命令的方式启动客户端：
```sh
# 创建一个配置文件
$ touch ~/ss-local.json

# 存入以下内容：
{
  "server":"服务端IP地址",
  "local_address": "127.0.0.1",
  "local_port":1080,
  "server_port": 2222,
  "password":"服务端密码",
  "timeout":300,
  "method":"aes-256-cfb"
}

# 启动客户端
$ sudo sslocal -c ~/ss-local.json -d start
```

重启或关闭客户端：
```sh
# 重启客户端
$ sudo sslocal -c ~/ss-local.json -d restart

# 关闭客户端
$ sudo sslocal -c ~/ss-local.json -d stop
```

## 使用
记住，`sslocal`启用的是`socks5`连接，你不能直接用HTTP方法去连接刚刚创建的本机代理。

所以在命令行里使用任何命令并加上代理参数时，必须要选socks代理才能正确使用：
```sh
$ curl --socks5 127.0.0.1:1080 ip.cn
```

另一种方法就是：再下载一个软件把`socks5代理`映射为`Http代理`。

### 更新
或者更简单的，直接在`~/.zshrc`或者`~/.bash_profile`中设置以下环境变量：
```sh
export ALL_PROXY=socks5://127.0.0.1:1080
```sh
然后重启zsh或bash，就可以发现curl, wget等原生程序都默认走了shadowsocks的socks5代理。
如果要取消代理的话，就用`unset ALL_PROXY`。
当然，还有更方便的方法，就是设置`alias`:
```sh
alias proxy='export ALL_PROXY=socks5://127.0.0.1:1080' 
alias unproxy='unset ALL_PROXY'
```
用的时候就输入`proxy`，不用时候就输入`unproxy`.
