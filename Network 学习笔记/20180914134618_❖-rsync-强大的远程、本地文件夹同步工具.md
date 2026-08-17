# ❖ rsync 强大的远程、本地文件夹同步工具

> 主要将「目录与目录」的同步，个体文件上传下载的就不需要这个程序了。

一般Mac、Ubuntu等主流*nix系统，都原生搭配了这个命令，非常好用。但是命令比较复杂，需要学习。

[参考：rsync参数详解、利用ssh、rsync 实现数据的定时同步](http://blog.51cto.com/colderboy/132054)
[参考：rsync参数详解、利用ssh、rsync 实现数据的定时同步](http://blog.51cto.com/colderboy/132054)

注意事项：
- 目录名后有或没有`/`是很不同的，非常复杂。具体参考：[cp拷贝文件夹时`/`的用法](https://github.com/solomonxie/solomonxie.github.io/issues/27#issuecomment-421560989)
- 不是所有参数都能搭配在一起用的，经常会互相冲突，所以要记住常用搭配方式。

缺陷：
- rsync**不支持**双向同步，只能单方向的向上同步或向下同步。
- rsync**不支持**两个remote之间直接同步，必须要一个第三方作为中间环节才行。

参数：
```
-r, --recursive 对子目录以递归模式处理;
-u, --update  仅仅进行更新，也就是跳过所有已经存在于DST，并且文件时间晚于要备份的文件；
--delete 删除那些target中有而source没有的文件;
-a, --archive  归档模式，表示以递归的方式传输文件，并保持所有文件属性不变，相当于使用了组合参数-rlptgoD;
--progress                    显示备份过程
-v, --verbose  详细模式输出；

-R, --relative                  使用相对路径信息
-b, --backup                  创建备份，也就是对于目的已经存在有同样的文件名时，将老的文件重新命名为~filename。可以使用--suffix选项来指定不同的备份文件前缀。
--backup-dir                  将备份文件(如~filename)存放在在目录下。
-suffix=SUFFIX             定义备份文件前缀
-l, --links                         保留软链结
-L, --copy-links              想对待常规文件一样处理软链结
--copy-unsafe-links        仅仅拷贝指向SRC路径目录树以外的链结
--safe-links                     忽略指向SRC路径目录树以外的链结
-H, --hard-links              保留硬链结
-p, --perms                    保持文件权限
-o, --owner                    保持文件属主信息
-g, --group                     保持文件属组信息
-D, --devices                 保持设备文件信息
-t, --times                      保持文件时间信息
-S, --sparse                   对稀疏文件进行特殊处理以节省DST的空间
-n, --dry-run                  现实哪些文件将被传输
-W, --whole-file             拷贝文件，不进行增量检测
-x, --one-file-system      不要跨越文件系统边界
-B, --block-size=SIZE   检验算法使用的块尺寸，默认是700字节
-e, --rsh=COMMAND 指定使用rsh、ssh方式进行数据同步
--rsync-path=PATH      指定远程服务器上的rsync命令所在路径信息
-C, --cvs-exclude          使用和CVS一样的方法自动忽略文件，用来排除那些不希望传输的文件
--existing                      仅仅更新那些已经存在于DST的文件，而不备份那些新创建的文件
--delete                         删除那些DST中SRC没有的文件
--delete-excluded          同样删除接收端那些被该选项指定排除的文件
--delete-after                传输结束以后再删除
--ignore-errors             及时出现IO错误也进行删除
--max-delete=NUM     最多删除NUM个文件
--partial                        保留那些因故没有完全传输的文件，以是加快随后的再次传输
--force                          强制删除目录，即使不为空
--numeric-ids                不将数字的用户和组ID匹配为用户名和组名
--timeout=TIME IP       超时时间，单位为秒
-I, --ignore-times          不跳过那些有同样的时间和长度的文件
--size-only                    当决定是否要备份文件时，仅仅察看文件大小而不考虑文件时间
--modify-window=NUM 决定文件是否时间相同时使用的时间戳窗口，默认为0
-T --temp-dir=DIR      在DIR中创建临时文件
--compare-dest=DIR   同样比较DIR中的文件来决定是否需要备份
-P 等同于 --partial
-z, --compress             对备份的文件在传输时进行压缩处理
--exclude=PATTERN  指定排除不需要传输的文件模式
--include=PATTERN   指定不排除而需要传输的文件模式
--exclude-from=FILE   排除FILE中指定模式的文件
--include-from=FILE   不排除FILE指定模式匹配的文件
--address                     绑定到特定的地址
--config=FILE             指定其他的配置文件，不使用默认的rsyncd.conf文件
--port=PORT              指定其他的rsync服务端口
--blocking-io               对远程shell使用阻塞IO
-stats                           给出某些文件的传输状态
--log-format=formAT  指定日志文件格式
--password-file=FILE 从FILE中得到密码
--bwlimit=KBPS         限制I/O带宽，KBytes per second
-h, --help                    显示帮助信息
```

## 本地同步
以下为常用的同步语句：
```sh
# 单方向拷贝，同cp命令
$ rsync -r <source>  <target>

# 单方向同步 --recursive --delete 注意这两个是固定搭配
# 如果source中没有的，target目录中有的会被删除
$ rsync -r --delete <source>  <target>
```


## 远程同步 （SSH连接）
> 远程目录的格式都为`<user@remote:path>`，如`pi@192.168.1.2:/home/pi`。以下都以`<remote>`代替。
无论方向如何，操作和效果是一摸一样的。

本地->远程
```sh
$ rsync -r <local> <remote>

# 如
$ rsync -r  ~/source/  pi@192.168.1.123:~/target
```

远程->本地
```sh
$ rcyn -r <remote> <local>

# 如
$ rsync -r pi@192.168.1.123:/home/pi/remote  ~/local/
```


把本地文件夹local中的内容拷贝到远程的remote文件夹中：
（传输所有本地有的文件-r，保留时间戳等所有信息-a，删除remote中和本地不同的-u --delete）
```sh
$ rsync -rau --delete <local>/ <remote>
```


## 进程锁Lock
一般人用文件同步，自然而然的就会要求它自动化，那也就是需要类似`crontab`的定期执行任务的机制。但是问题来了，假设我在`crontab`里面设置每1分钟同步一次，保持高频率同步，那么如果这次文件过多，1分钟完成不了，然后下一个rsync任务又来了，怎么办？

这就需要rsync的进程锁了。原理很简单，就是每次rsync执行任务，都找个地方存一个叫`xx.lock`的文件，执行完任务后就删除它。下一个rsync任务执行的时候，先要看一眼那个地方有没有这个lock文件，没有的话就执行，有的话就**取消**。

[参考：Rsync添加进程锁，防止重复进程](http://www.voidcn.com/article/p-evayrzik-bn.html)



## 参数为变量的问题

`rsync`中的参数如源位置、目标位置等，直接用`"variable"`这种是不行的。所以要用到Bash中比较tricky的小技巧才能做到。

[参考Stackoverflow: Running an rsync command from a variable — quoting not honored](https://stackoverflow.com/a/43617604/9172013)

```sh
opts=( -vtrin 
       -e ssh
       --exclude '._*'
       --exclude '.@*'
       --exclude .DS_Store
       --progress
       /Path/
       user@IP:/Path
)
# echo rsync ${opts[*]}

rsync ${opts[@]}
```
