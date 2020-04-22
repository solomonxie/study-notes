# 关于Python协程

The sockets are still synchronous / blocking with merely gevent.pawn().
The way to solve it is to use gevent monkey patch to patch all from the begining so that it could capture the socket status (poll / select).
Or directly use `gevent.sleep()` to force worker sleep and initiate another worker.


Facts:
- 光使用Yield/send/next等生成器相关，无法解决I/O阻塞问题。也就是遇到I/O阻塞依然会阻挡整个程序
- 需要利用到内核的Poll/Select和事件池，才能实现遇到I/O阻塞自动切换
- gevent必须要打上`monkey patch`才能在阻塞时自动切换
- `gevent.sleep` 做的实际上就是强制创建阻塞，让当前函数调到后台运行

Refer to: https://blog.csdn.net/LWL_WLiang/article/details/72787027
