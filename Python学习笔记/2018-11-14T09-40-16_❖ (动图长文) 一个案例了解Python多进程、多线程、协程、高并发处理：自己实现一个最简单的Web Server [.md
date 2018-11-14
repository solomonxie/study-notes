# ❖ (动图|长文) 一个案例了解Python多进程、多线程、协程、高并发处理：自己实现一个最简单的Web Server  [DRAFT]

Python的多任务处理机制一直在尝试学习，但是阅读很多文章、看了很多教学视频，都还是没太理解，或是记不住。可能不止我一个人是这样。就算写代码练习，一般也都只是多任务处理个简单函数，没什么太大感觉，甚至觉得：有必要么？
受到David Beazley在PyCon 2015演讲中的启发，觉得实现一个简单的Web Server能够将Python多任务机制的优缺点一目了然的呈现出来，而且也是现实世界里真实的需求。
所以决定参考他的视频自己写一个Web Server，从头到尾体验一下各种多任务处理方案。

> 本文将根据David Beazley在PyCon 2015中关于并发技术的演讲，对Python处理并发请求进行各种方案的尝试和学习。

和一般的Documentation式讲解不同，为了理清多任务的各种方式，这篇文章我们将采取根据线索展开的方式讲解，大概结构是：
- 单任务处理 （理解单任务的缺陷）
- 高并发设计 （理解高并发是要解决什么问题）
- 多进程 （理解怎么利用多核CPU）
- 多线程 （理解怎么减少进程资源耗费）
- 性能测试 （通过简单的性能测试了解多任务处理的优缺点）
- GIL进程锁 （理解Python的多进程缺陷）
- 生成器 （理解Python Generator的多任务方式）
- 协程 （理解流行的高并发技术）
- AsyncIO （理解流行的高并发技术）
- Socket非堵塞


[参考Youtube: David Beazley - Python Concurrency From the Ground Up: LIVE! - PyCon 2015](https://www.youtube.com/watch?v=MCs5OvhV9S4)
[相关代码参考：dabeaz/concurrencylive](https://github.com/dabeaz/concurrencylive)

这里我们的Web Server将使用简单的`Socket编程`，代码本身不多。至于Socket的具体原理，这里不会太细讲，请自行参考。
另外，为了保证简单，这里的Web Server不处理HTTP交互，而是最单纯的TCP层交互：**也就是说客户端可以随便发送任何内容到服务器如`123abc`，服务器也可以回复任何内容如`hello`，不需要遵守HTTP格式或其它任何格式。**

> Python自己写Web Server很简答，只需要几句话操控`socket`即可。然而要实现同时处理`并发请求`，就必须用到`多进程`或`多线程`或`协程`等。

为了最好的对比各种多任务处理方式的效果，我们需要一个简单的`task`任务，这里我们用一个最简单的函数：根据序号n，返回斐波纳西数列中序号对应的数字：
```py
# fib.py
def fib(n):
    if n <= 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)
```

不要小看这个简单的函数，如果你执行一句`fib(10)`还好，我在Macbook 2017上，就算执行一句`fib(1000)`都要**接近一分钟才能计算完成**！
选择斐波纳西数列的好处在于，它会随着请求数字增大，处理速度会极速下降。

整个系统的设计是这样的：
**我们创建一个server服务器，接受来自client客户端的请求，客户告诉我们一个数字n，我们就返回斐波纳西数列中n对应的数字。**
如`fib(2)`代表第二个数字，那就是1，`fib(6)`是第六个数字，就是8。

其中，处理task任务的代码是相同的，只是server服务端的多任务处理方式不同。也就是说，下面我们只是创建各种不同的server代码，而task还是用上面的代码而没有变化。

我们先从单一请求的处理开始：完全不顾及并发，一次只处理一个client，多一个client都不接受。



## 「Synchronous」最简单：单进程、单线程处理请求

这也是最简单、最基本的socket操作，代码如下：
```py
# server.py
from socket import *
from fib import fib

def fib_server(address):
    sock = socket(AF_INET, SOCK_STREAM)
    sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    sock.bind(address)
    sock.listen(5)
    while True:
        client, addr = sock.accept()
        print('Connected', addr)
        fib_response( client )

def fib_response(client):
    while True:
        req = client.recv(100)
        if not req:
            break
        n = int(req)
        result = fib( n )
        resp = b'fib: ' + str(result).encode('ascii') + b'\n'
        client.send(resp)
    print('Closed.')


fib_server( ('localhost', 9999) )
```

其中，
- `fib_server()`是用来创建一个基本的服务器端socket的，步骤都是很固定的写法，具体怎么理解在这里先不扩展了，只要知道它做的就是：监听指定的某个`IP:Port`，一直循环循环，一旦来了client访问，就马上给出回应。
- `fib_response()`就是具体的回应给client的函数。它做到的是：根据client给的数字，返回`fib()`函数的结果。其中`resp`变量是`client.send()`中的参数，要求必须是010101这样的binary格式，而不是普通的字符串。

然后我们来测试下效果。

- 首先需要让Server运行起来，即`$ python server.py`即可开启一个”持久运行“的监听`localhost:9999`的Web服务器。
- 然后在另一个Shell中，我们模拟客户端来访问这个服务器，并和它交互。两种非常好用的方法：一个是`nc`命令(推荐)，一个是`telnet`命令。两个程序都用来与服务器交互。用nc连接服务器只需要：`$ nc localhost 9999`即可建立连接，进入交互阶段。随便输入一个数字，就会在当前Shell中获得服务器返回的结果。比如输入`1`返回`1`，输入`6`返回`8`。如下：

![rec](2018-11-14T09-40-16_❖ (动图长文) 一个案例了解Python多进程、多线程、协程、高并发处理：自己实现一个最简单的Web Server [_files/img_01.gif)

但是这个最简单的Server有一个致命缺点——同一时间只能接收一个client客户，如果有另一个客户，就会排队等待，直到前一个客户退出连接。展示效果如下：

![rec](2018-11-14T09-40-16_❖ (动图长文) 一个案例了解Python多进程、多线程、协程、高并发处理：自己实现一个最简单的Web Server [_files/img_02.gif)

可见，最简单的Synchronous同步服务器对我们来说，相当于白费！因为我们绝不可能一次只处理一个用户，就算一个小网站怎么也要一次处理10个用户吧。
所以，我们这里要开始修改Server服务器代码，让他支持多任务，即多请求处理机制。




## 「Concurrency」怎么应对高并发？

处理`高并发`，也就是实现`多任务`，也就是防止`Blocking`的技术，也就是防止`I/O阻塞`，都是一回事。

上面我们的Socket服务器中有这几个地方是遇到I/O blocking的：
- `sock.accpet()`
- `client.recv(..)`
- `client.send(..)`

每次server遇到上面这三句话，都会卡在那，等待结果直到超时，所以卡在这一个地方可能就很多秒。
也就是说，我们的主要任务就是：解决这几个blocking语句。

**Blocking怎么解决？——没法解决！客户端不传来数据，服务器就只能等！**
但是，我们可以做到的是，一个客户卡住了，不影响其他客户啊。
所以处理`I/O blocking`的思路是——让把每个Task任务在各个`平行世界`里同时运行，一条线卡住了也不影响其它线。

具体来说就是，在每次

目前能做到这种并行处理任务的方法有：
- Multiprocessing 多进程
- Threads 多线程
- Generator 迭代生成器
- Coroutine 协程

`Multiprocessing`多进程的优点是能够充分利用多核CPU并行计算，但缺点是每条线的内存耗费成本太高，一个任务一个进程的话，每个任务几MB内存，光几百几千个任务就造成几GB级内存消耗，这种消耗级完全不是一般服务器能扛住的。
`Threads`多线程的优点是并行计算的内存消耗很低，但缺点是`GIL锁的不公平性`所带来的每条线的快慢悬殊可能性很大，这样的效果不是我们希望的。
`Generator`生成器实现并发处理可以完全摆脱多线程，但代码要更复杂很多，而且在实际测试性能后发现它并没能避免GIL的难题：一旦出现别的高计算请求，原先的请求就会被CPU强制降速，甚至降到0。
`Coroutine`协程一样**不能避免**GIL锁的计算资源分配不公问题，因为Python里的`Coroutine`本质上就是由Generator实现的。





## 「Multi-processing」多进程处理请求

即，每次来了一个新的client发出请求，Python就新开一个processor进程，来专门处理他的请求。
（一般每个进程耗费几MB以上内存）

代码如下：
```py

```



## 「Theading」多线程处理请求(单进程)

> 开`多进程`的花销太大，因为每次开一个进程都会耗费的大量内存，每一个client消耗几MB，仅一万个请求就要耗费10GB内存，这不太现实。所以可以采用在单进程内，创建多个线程的方式。

注意：多线程一样是可以利用多核CPU的。（但是Python中却不同，几乎相当于只能用单核。后面GIL详解）

针对上面的`Synchronous同步服务器`代码，我们只需要简单改动`fib_server()`函数，就能变成`Asynchronous异步服务器`。需要改动的只有两处：
- 导入`threading.Thread`模块
- 将直接执行task函数的地方改为由一个线程执行：`Thread(target=fib_response, args(client,), daemon=True).start()`

既然程序是在`while True:`中执行的，那么每次有新连接而堵塞的时候，只是堵塞了一个线程，而其它的成千上万的“失败连接”或其它新连接都不会被影响。

服务器端的`fib_server()`函数完整代码如下：
```py
# aserver.py
from socket import *
from threading import Thread
from fib import fib

def fib_server(address):
    sock = socket(AF_INET, SOCK_STREAM)
    sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    sock.bind(address)
    sock.listen(5)
    while True:
        client, addr = sock.accpet()
        print('Connection', addr)
        Thread(target=fib_response, args=(client,), daemon=True).start()

def fib_response(client):
    ..........
```

这样简单的一句`Thread(...).start()`，就能实现多任务处理了。**此时服务器已经具有了同时处理多客户请求的功能。**

下面是效果：

![rec](2018-11-14T09-40-16_❖ (动图长文) 一个案例了解Python多进程、多线程、协程、高并发处理：自己实现一个最简单的Web Server [_files/img_03.gif)




为了更清晰的展现各种不同多任务处理方案的效果，我们需要写个性能测试模块(也就是客户端)来创造`高并发`请求，并展示出请求处理的效率。


## 「Performance」先写一个测试性能的客户端

> 注意：这个性能测试不会对之前的Synchronous同步服务器进行测试，因为它只能接收一个客户端，不支持多任务，也就测试不出来多任务效果。

我们会写两个性能测试模块：
- 第一个显示`每次请求的执行时间`
- 第二个显示`每秒处理请求的次数`

两个模块都是Socket客户端。本质上，这两个Socket客户端只是代替了之前我们手动connect服务器的`nc`命令，因为我们还没有手快到每秒几千次的地步。手写Socket客户端，也能进一步了解Socket交互的两端。


### 性能测试01：`每次请求的执行时间`

这个测试内容主要就是：
利用Socket做一个客户端，然后**不受限制地**频繁向服务器发出请求，然后显示出`每秒处理请求的次数`。之后我们就以这个每秒次数来代表各种多任务方案的处理效率。

```py
# performance01.py
from socket import *
import time

sock = socket(AF_INET, SOCK_STREAM)
sock.connect(('localhost', 9999))

while True:
    start = time.time()
    # -----------------
    sock.send(b'29')
    resp = sock.recv(100)
    # -----------------
    end = time.time()
    print('consumed:', end - start)
```

效果如下：

![rec2](2018-11-14T09-40-16_❖ (动图长文) 一个案例了解Python多进程、多线程、协程、高并发处理：自己实现一个最简单的Web Server [_files/img_04.gif)

可以清楚的看到，在单一客户端访问时，速度是0.2秒处理一条请求。然而另开一个客户端时，两个客户端的速度同时速降到0.4秒一条请求，而开第三个客户端时，所有的请求速度都降到了0.6秒每条。
我的Macbook是双核的，但Python却没有利用多核运算，完全在一个CPU核心上运算，每次增加连接数就直接导致降速。这是为什么？

这就是Python中著名的`GIL`锁了—— `Global Interpreter Lock`。GIL迫使Python集中在一个CPU核心上运算，加强了运算能力，但是减少了多核的利用。


### 性能测试02：`每秒处理请求的次数`

下面这个测试，我们只用`fib(1)`计算极其简单的数字，但是量比较大。和上面的计算复杂、请求量少正好相反。

```py
# performance02.py
from socket import *
import time
from threading import Thread

sock = socket(AF_INET, SOCK_STREAM)
sock.connect(('localhost', 9999))

n = 0

def monitor():
    global n
    while True:
        time.sleep(1)
        print(n, 'reqests/sec')
        n = 0

Thread(target=monitor).start()

while True:
    sock.send(b'1')
    resp = sock.recv(100)
    n += 1
```

测试效果如下：

![rec](2018-11-14T09-40-16_❖ (动图长文) 一个案例了解Python多进程、多线程、协程、高并发处理：自己实现一个最简单的Web Server [_files/img_05.gif)


在测试多线程时候，我们看到，当我们重新开一个新的连接并计算`fib(40)`时候，因为所需计算量增大，`每秒处理请求数`极速下降。同样的，这是由`GIL`锁的机制导致的。


## 「GIL」理解线程锁

GIL进程锁是Python独有的一直**保护进程安全**的机制。
但什么是“线程安全”呢？其实很简单：
只有在多条线程同时修改一个公共变量时会产生“不安全”。

假设有个全局变量`Var=1`，然后两个线程T1, T2同时修改变量`Var += 1`这个操作。
由于是同时执行，前后顺序不确定：
T1刚把Var变量下载下来变成`本地变量`，然后计算`+1`操作，然后再“上传“，覆盖原公共变量；
T2同时也在执行这个操作，但有可能在T1把Var下载下来还没来得及上传呢，T2就也执行了一个`Var = 2`。
这样一来Var变量原本应该执行2次+1，变成`Var == 3`的，结果现在`Var == 2`。
这就是Bug了，这就是“不安全”了，这也就是`线程不安全`。

下图为Computerphile解释两个线程同时修改头上的同一个变量的过程：

![image](2018-11-14T09-40-16_❖ (动图长文) 一个案例了解Python多进程、多线程、协程、高并发处理：自己实现一个最简单的Web Server [_files/img_06.png)

[参考Youtube：Multithreading Code - Computerphile](https://www.youtube.com/watch?v=7ENFeb-J75k)
[参考：Python的全局锁问题](https://python3-cookbook.readthedocs.io/zh_CN/latest/c12/p09_dealing_with_gil_stop_worring_about_it.html)

那么直到了进程不安全特征，Python怎么解决呢？
参考上面视频，我们知道，Python给了每个线程一个Token，也就是一把钥匙🔑。只有手上拿着钥匙的那个进程可以开门，进去修改公用变量，然后再把钥匙给下一个人，再去修改变量。

**这就是GIL锁机制——也就是每个线程要拿着Token去改变量的机制。**

但是很多人都说，怪罪GIL是不应该的。因为GIL机制只会针对CPU计算较大的线程有影响，比如计算斐波纳西数列。普通I/O并行无所谓，因为反正I/O是要等待的。

GIL的特点之一就是：
当多条线程运行时，它怎么选择让谁优先呢？它会选择需要CPU计算量较大的线程优先运行！
这也就是为什么我们用`fib(40)`运算数据时，原有的`performance02.py`的速度极速下降，就是因为优先权被抢了。在performance02中，只是计算`fib(1)`简单的运算而请求量大，但`fib(40)`计算量大请求只有一个。所以CPU优先计算了这个少量请求且计算量大的线程。

**`GIL机制`影响了平行世界中每条线的`公平性`——某条线需要计算量大时，其它线的速度就大幅降低，这不合理。应该是多一条线，大家都降低但大家的速度差不多才对。**

为了对抗`GIL的不公平性`，很多人提出了很多方案，比如利用`Pool`。
`Pool任务池`的具体代码写起来让新人费解。但是的确能做到处理高并发时，不被其它人的新请求影响到当前任务的处理速度。

换个角度，为什么我们要这么费力对抗GIL？也许一开始根本就不需要用`Threads`多线程？



## 「Generator」生成器：yield与Round-Robin循环淘汰赛/轮询调度处理高并发

当我们把yield和`消息列表的轮询调度`这种机制结合起来用，那就是非常高级的高并发运用了。

正式开始之前，我们先了解一下著名的`Round-robin`，也就是体育比赛的`循环淘汰赛制`，英文是`Round-robin tournament`，如果运用在计算机领域，就是如雷贯耳的`轮询调度`，英文是`Round-robin scheduling`。

体育比赛里有一种常用的赛制叫`循环淘汰赛`，比如跳高：
- 每一轮，让10个选手跳同一个高度，如果失败就把他淘汰掉。比如已经淘汰掉了一个
- 下一轮，让剩下来的9个选手再跳另一个高度，谁失败就把谁淘汰掉
- 下一轮，让剩下的5个选手跳更高的高度……
- 最后到剩1个选手时，就只针对他一人来一轮一轮的提高高度，直到他失败为止。

计算机里也经常用这种制度，来作为消息列表的调度方案：
一轮一轮的不断查看某个列表，只要列表里面有task任务，就FIFO按顺序处理每个任务。每处理完一个任务就把它删掉，继续执行下一个，直到列表清空。
列表清空后，程序也是不断的查看这个列表，一旦内容有更新，立马又去处理。

这就是著名的`Round-Robin`轮询调度，原理非常简单。

那么`yield`怎么和`Round-Robin`结合处理高并发呢？

**首先要注意： 传统的代码结构必须要重构，否则没法使用并发任务处理。**

然后我需要添加一个小工具，即`tasks = []`这个列表变量。
也就是说，我们要把`yield + tasks[] + Round-robin`这三个东西放一起才能开始工作。

逻辑是这样的：
- 每次碰到I/O堵塞的地方，我们都





## 「Coroutine」协程：单进程单线程之采用协程处理多请求

[参考：协程 - 廖雪峰Python教程](https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001432090171191d05dae6e129940518d1d6cf6eeaaa969000)

客户数量过大时，即使是`多线程`也扛不住。那么最近开始的`协程方案`就开始被Python引入了。

> `Corotine协程`是Python中`异步IO`中的知识点。

Python中协程的流行方法是，使用第三方库`gevent`来创建。

[参考Youtube：gevent - Why should I care about asyncio](https://youtu.be/b6z2VB1JU3U?t=366)

代码如下：
```py
import requests
from gevent import monkey

# 重要！
monkey.patch_all()

def get_content(url):
    resp = requests.get(url)
    return resp.text
```

![image](2018-11-14T09-40-16_❖ (动图长文) 一个案例了解Python多进程、多线程、协程、高并发处理：自己实现一个最简单的Web Server [_files/img_07.png)

`gevent`好处是，一切并发、异步I/O处理全都在后台，你甚至看不到自己的哪些for循环被变成了异步式。但同时，这也导致了一个黑盒：你不知道后台怎么操作。有些时候甚至一些不想异步的东西也被异步了。


## 「Asyncio」处理高并发

[再次参考David Beazley：Keynote David Beazley - Topics of Interest (Python Asyncio) - Youtube](https://www.youtube.com/watch?v=ZzfHjytDceU)

```py

```


## 「Non-blocking Socket」单进程单线程之采用非堵塞处理多请求

Python中，`socket`都可以设置为`非堵塞`方式，即`accpet()`和`receive()`方法执行时可以不用等待，而直接执行下一步。
这样一来，就可以直接利用LOOP循环完成无限多任务的处理。
唯一要注意的是：
- 当`accpet()`没有接收到任何客户端连接时，就着急去执行下一步，**会产生异常**。
- 当`receive()`没有接收到任何客户端发送数据时，就着急去执行下一步，**会产生异常**。

所以需要采用`try...catch`异常处理来完成这个功能。
代码如下：
```py

```
![image](2018-11-14T09-40-16_❖ (动图长文) 一个案例了解Python多进程、多线程、协程、高并发处理：自己实现一个最简单的Web Server [_files/img_08.png)


