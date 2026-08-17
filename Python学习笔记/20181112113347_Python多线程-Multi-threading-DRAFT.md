# Python多线程 Multi-threading [DRAFT]

时间片轮转：每个任务执行万分之一秒，然后切换。

- 并行：真的多任务。每个CPU核心执行一个任务
- 并发：假的多任务。启用时间轮转，CPU对每个任务轮流计算，每次只用万分之一秒执行一个任务。

当只有4个任务时，4核CPU可以实现`并行`，即每个核心负责一个任务。
但是当任务数超过CPU的核心数时，则必须要启用时间轮转。

一般情况下，全都是`并发`，因为任务数总是超过核心数。

Python线程代码：
```py
import threading

def func():
    for i in range(10):
        print('Run...')

th = threading.thread(target=func)
th.start()
```

查看当前运行多线程数量：
由于多线程同时运行多个线程，每执行完成一个就销毁一个，所以`当前线程数量`是动态变化的。

代码：
```py
# .....
# .....

th = threading.thread(target=func)
th.start()

while True:
    amount = len(threading.enumerate)
    if amount < 1:
        break
    sleep(0.5)
```
注意：程序执行到`th.start()`开启线程后，不会等待所有线程结束，而会直接执行下一句，**同时**多条线程一起执行。
所以，这时候去读取线程数，是一个**动态**的过程，需要每隔一段时间重复去读取。这时会发现，线程数是逐渐减少的。



## 等待所有线程执行完后再执行语句

如果直接使用多线程的话，结果就是，程序遇到多线程语句后**完全不会等待，而是直接绕过去！**
那么我们多线程所做的`前期处理`也就没有意义了，因为后面的代码还没拿到完全的前期结果，就已经被执行了。

这肯定不是我们想要的。

目前为止比较简答的解决方案：https://stackoverflow.com/questions/46301933/how-to-wait-till-all-threads-finish-their-work

```py
import threading
import time

# Lock to serialize console output
output = threading.Lock()

def threadfunc(a,b):
    for i in range(a,b):
        time.sleep(.01) # sleep to make the "work" take longer
        with output:
            print(i)

# Collect the threads
threads = []
for i in range(10,100,10):
    # Create 9 threads counting 10-19, 20-29, ... 90-99.
    thread = threading.Thread(target=threadfunc,args=(i,i+10))
    threads.append(thread)

# Start them all
for thread in threads:
    thread.start()

# Wait for all to complete
for thread in threads:
    thread.join()
```
