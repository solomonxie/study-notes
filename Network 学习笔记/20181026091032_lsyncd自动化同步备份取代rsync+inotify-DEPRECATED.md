# ~lsyncd自动化同步备份取代rsync+inotify~ [DEPRECATED]

> 学习了半天，夸了半天，发现：不能用！看最后的`错误`。

Ubuntu安装：
```sh
$ sudo apt-get install lsyncd
```

Mac安装：
```sh
# 安装Ruby依赖
ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)" < /dev/null 2> /dev/null

# 安装lsyncd
brew install lsyncd
```

启动`lsyncd`：
在`lsyncd.conf`配置文件已经设计好了后，输入这个命令启动lsyncd的守护进程(daemon)，自动执行同步：
```sh
$ sudo lsyncd -log Exec ~/lsyncd.conf
```
注意：lsyncd需要sudo权限。

## `配置文件 lsyncd.conf`
> `lsyncd`的一切任务和行为都是在`lsyncd.conf`这个文件里设置的。从命令中就可以看出，无需其它参数只要指定一个配置文件即可。

[参考：lsyncd实时同步搭建指南——取代rsync+inotify](http://seanlook.com/2015/05/06/lsyncd-synchronize-realtime/)

`lsyncd.conf`的文件结构和JSON类似。每一个任务是一个类似JSON的定义块，设置包括来源、目标、传输方法（rsync或普通的cp）等。结构是：
- 全局设置：`settings { ....... }`
- 同步任务1: `sync { ...... }`
- 同步任务2: `sync { ...... }`
- 同步任务3: `sync { ...... }`

如：
```
settings {
    ......
}

sync {
    ......
}

sync {
    ......
}
```

### `全局设置 settings { ....... }`

```
settings {
    logfile ="path-to-a-log-file",
    statusFile ="path-to-a-status-file",
    inotifyMode = "CloseWrite",
    maxProcesses = 10
}
```

其中：
- `logfile`: 日志文件，随便设置
- `statusFile`: 状态文件，随便设置
- `inotifyMode`: inotify的模式，可以是`CloseWrite`或`Modify`。
- `maxProcess`: 进程数，越大越快，也越占资源

### `任务定义 sync {......}`
```
sync {
    default.YourMethod,
    source   = "path-to-the-source",
    target    = "path-to-the-target",
    delay = 1
    maxProcesses = 5
    YourMethodDetails = {
        ......
    }
}
```

- `default.???`，代表你想使用的传输方法，有：`default.direct`：直接用cp, mv, rm命令同步；`default.rsync`：用rsync进行本地同步；`default.rsyncssh`：用rsync+SSH进行远程同步
- `delay`：重要，查询文件变化的时间间隔。比如15s。
- `maxDelays`：累计到多少所监控的事件激活一次同步，就算delay的延迟时间还未到也执行同步。
- `excludeFrom`
- `delete`: `true` or `false`，是否删除目标文件夹中多余的文件；`startup`；`running`
- `rsync`：如果用的rsync方法传输，则在这里定义具体的传输方案
    - `binary`：rsync在本机的位置, 如`/usr/bin/rsync`
    - `bwlimit`：band width limit，限速。比如`2000`，代表2000 k/s
    - `compress`：true或false，是否压缩传输
    - `perms`：permissions，是否保留源文件相同的文件权限
    - `verbose`：是否详细输出传送过程的信息



## `查看运行状态和任务执行情况`
因为刚才定义了两个文件，`lsyncd.log`和`lsyncd.status`，所以直接用cat查看即可。如果想获得实时的输出，那么用`tail -f`命令查看也行。

注意，`lsyncd`是在ps进程里看不到的。


## 错误

报错如下：
```
rsync: -lst: unknown option
rsync error: syntax or usage error (code 1) at /BuildRoot/Library/Caches/com.apple.xbs/Sources/rsync/rsync-51/rsync/main.c(1337) [client=2.6.9]
Sat Oct 27 15:53:15 2018 Error: Failure on startup of "/Users/solomonxie/Workspace/tests/shell/lsyncd1/": 1
Sat Oct 27 15:53:15 2018 Error: Critical exitcode.
```
说明需要更新rsync版本，最少3.0以上。
Mac上的默认rsync版本相当低，一般是2.6左右，所以不支持新的lsyncd语法。
可以试试`brew upgrade rsync`。

更新：
仍然没有解决。。。
