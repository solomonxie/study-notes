# Ubuntu将命令或脚本变成服务开机启动

有很多程序比如ssh-tunnel、frp、jekyll、Jupyter notebook等网络服务，都是在前台执行监听的，必须一直保持进程连接才行，每次还要手动输入命令打开，不方便，也不稳定。
比如ssh-tunnel，如果其中哪个节点的终端稍稍断开，那就都断了，不稳定。在这种情况下非常有必要把它转为后台运行的服务，且开机自动启动，不需要手动打开。

Linux的各种distro的添加服务方式都不一样，所以需要分别查。
Linux的服务，其实就是自定义的shell脚本。需要做的主要就是把这个脚本以各种系统要求的格式或位置放好，然后用某个工具添加到服务中即可。

Redhat系是用`chkconfig`命令，而Ubuntu系是用`update-rc.d`命令。具体做法如下：
- 假设现在手里有个`HAHAHA.sh`脚本
- 把`test.sh`脚本保存在`/etc/init.d/`目录中
- 添加或删除服务：
```sh
添加：sudo update-rc.d 服务名 defaults
删除：sudo update-rc.d -f 服务名 remove
```
- 启动、关闭、重启服务：
```sh
/etc/init.d/服务名 start
/etc/init.d/服务名 stop
/etc/init.d/服务名 start
```

## 关于自定义脚本的编写
Linux的服务的本质是一个shell脚本，但是需要遵循service的标准模版，比如在头注释中编写service描述等，以供系统读取；还要定义每种操作的具体实行方式，比如在`service start`时会执行脚本中的start()函数。

[参考：在Ubuntu下添加自定义服务](https://blog.csdn.net/xkjcf/article/details/78698232)

以下为标准模版：
```sh
#!/bin/bash
### BEGIN INIT INFO
#
# Provides:  location_server
# Required-Start:   $local_fs  $remote_fs
# Required-Stop:    $local_fs  $remote_fs
# Default-Start:    2 3 4 5
# Default-Stop:     0 1 6
# Short-Description:    initscript
# Description:  This file should be used to construct scripts to be placed in /etc/init.d.
#
### END INIT INFO

## Fill in name of program here.
PROG="location_server"
PROG_PATH="/opt/location_server" ## Not need, but sometimes helpful (if $PROG resides in /opt for example).
PROG_ARGS="" 
PID_PATH="/var/run/"

start() {
    if [ -e "$PID_PATH/$PROG.pid" ]; then
        ## Program is running, exit with error.
        echo "Error! $PROG is currently running!" 1>&2
        exit 1
    else
        ## Change from /dev/null to something like /var/log/$PROG if you want to save output.
        $PROG_PATH/$PROG $PROG_ARGS 2>&1 >/var/log/$PROG &
    $pid=`ps ax | grep -i 'location_server' | sed 's/^\([0-9]\{1,\}\).*/\1/g' | head -n 1`

        echo "$PROG started"
        echo $pid > "$PID_PATH/$PROG.pid"
    fi
}

stop() {
    echo "begin stop"
    if [ -e "$PID_PATH/$PROG.pid" ]; then
        ## Program is running, so stop it
    pid=`ps ax | grep -i 'location_server' | sed 's/^\([0-9]\{1,\}\).*/\1/g' | head -n 1`
    kill $pid

        rm -f  "$PID_PATH/$PROG.pid"
        echo "$PROG stopped"
    else
        ## Program is not running, exit with error.
        echo "Error! $PROG not started!" 1>&2
        exit 1
    fi
}

## Check to see if we are running as root first.
## Found at http://www.cyberciti.biz/tips/shell-root-user-check-script.html
if [ "$(id -u)" != "0" ]; then
    echo "This script must be run as root" 1>&2
    exit 1
fi

case "$1" in
    start)
        start
        exit 0
    ;;
    stop)
        stop
        exit 0
    ;;
    reload|restart|force-reload)
        stop
        start
        exit 0
    ;;
    **)
        echo "Usage: $0 {start|stop|reload}" 1>&2
        exit 1
    ;;
esac
```
其中，PROG变量为所要运行的可执行程序的名称， PROG_PATH为可执行文件所在的目录，PROG_ARGS为执行程序的各个参数。 
