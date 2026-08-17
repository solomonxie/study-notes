# Linux进程管理 [DRAFT]


## 查看进程

```sh
# 常用：
ps aux

# 直接根据进程名查看进程ID：
pgrep zsh
```

## 关闭进程

```sh
# 关闭单个进程
kill <进程ID>

# 关闭所有进程
pkill <进程名>

# 或
killall <进程名>

# 或
pgrep <进程名> |xargs kill
```
