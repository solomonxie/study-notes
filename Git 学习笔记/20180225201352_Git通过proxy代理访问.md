# Git通过proxy代理访问
假设本地的代理端口为1087，那么命令行设置：
```
git config --global http.proxy http://127.0.0.1:1087
```
或者直接在`~/.gitconfig`中添加：
```
[http]
    proxy = http://127.0.0.1:1087
```
