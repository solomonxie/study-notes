# Docker run -d启动后立刻就停止了

现在有一个最简单的Dockerfile
```dockerfile
FROM alpine
MAINTAINER Solomon Xie <solomonxiewise@gmail.com>

COPY entry.sh /

CMD ["/bin/sh", "/entry.sh"]
```

然后entry脚本是这样的：
```sh
#entry.sh
echo OK.
```

现在想要这个docker在后台常驻(-d)，然后我随时可以登陆进container：
```sh
$ docker build . example
$ docker run -d example
```

但是每次run之后，container执行完entry脚本立马就停止了。

原因在于, `-d` 是`detached mode`，有一个大大前提：
**必须有一个foreground前台任务执行，才能把container“挂住”，可以是一个server，也可以是一个死循环，比如：**
```sh
# Correct
tail -f /dev/null

# Correct
FLASK_APP=myapp flask run

# Correct (Cron daemon)
/usr/sbin/crond -fd 0

# Wrong
echo OK
flask run &
```
 脚本的最后一个命令，一定要挂住，不能到"完成"，也不能转后台运行。


