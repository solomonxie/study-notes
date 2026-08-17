# ❖ Python高级语法之：一篇文章了解yield与Generator生成器

Python高级语法中，由一个`yield`关键词生成的`generator`生成器，是精髓中的精髓。它虽然比装饰器、魔法方法更难懂，但是它强大到我们难以想象的地步：小到简单的for loop循环，大到代替多线程做服务器的高并发处理，都可以基于`yield`来实现。


## 理解yield：代替return的yield

简单来说，`yield`是代替`return`的另一种方案:
- `return`就像人只有一辈子，一个函数一旦return，它的生命就结束了
- `yield`就像有“第二人生”、“第三人生”甚至轮回转世一样，函数不但能返回值，“重生”以后还能再接着“上辈子”的记忆继续返回值

**我的定义：`yield`在循环中代替`return`，每次循环返回一次值，而不是全部循环完了才返回值。**

yield怎么念？
> return我们念“返回xx值”，我建议：yield可以更形象的念为"呕吐出xx值“，每次呕一点。

一般我们进行循环迭代的时候，都必须等待循环结束后才return结果。
数量小的时候还行，但是如果循环次数上百万？上亿？我们要等多久？
如果循环中不涉及I/O还行，但是如果涉及I/O堵塞，一个堵几秒，后边几百万个客户等着呢，银行柜台还能不能下班了？

所以这里肯定是要`并行处理`的。除了传统的多线程多进程外，我们还可以选择Generator生成器，也就是由`yield`代替return，每次循环都返回值，而不是全部循环完了才返回结果。

这样做的好处就是——极大的节省了内存。如果用return，那么循环中的所有数据都要不断累计到内存里直到循环结束，这个不友好。
**而yield则是一次一次的返回结果，就不会在内存里累加了。所以数据量越大，优势就越明显。**

**有多明显？如果做一百万的简单数字计算，普通的for loop return会增加300MB+的内存占用！而用yield一次一次返回，增加的内存占用几乎为0MB！**


### yield的位置

既然`yield`不是全部循环完了再返回，而是循环中每次都返回，所以位置自然不是在for loop之后，而是在loop之中。

先来看一般的for loop返回：
```py
def square(numbers):
    result = []
    for n in numbers:
        result.append( n**2 )
    return result    #在for之外
```

再来看看yield怎么做：
```py
def square(numbers):
    for n in numbers:
        yield n**2    #在for之中
```
可以看到，yield在for loop之中，且函数完全不需要写return返回。

这时候如果你`print( square([1,2,3]) )`得到的就不是直接的结果，而是一个`<generator object>`。
如果要使用，就必须一次一次的`next(...)`来获取下一个值：
```py
>>> results = square( [1,2,3] )
>>> next( result )
1
>>> next( result )
4
>>> next( result )
9
>>> next( result )
ERROR: StopIteration
```

这个时候更简单的做法是：
```py
for r in results:
    print( r )
```
因为`in`这个关键词自动在后台为我们调用生成器的`next(..)`函数


什么是generator生成器？
只要我们在一个函数中用了`yield`关键字，函数就会返回一个`<generator object>`生成器对象，两者是相辅相成的。有了这个对象后，我们就可以使用一系列的操作来控制这个循环结果了，比如`next(..)`获取下一个迭代的结果。

`yield`和`generator`的关系，简单来说就是一个起因一个结果：只要写上yield, 其所在的函数就立马变成一个`<generator object>`对象。



## xrange：用生成器实现的range

Python中我们使用`range()`函数生成数列非常常用。而`xrange()`的使用方法、效果几乎一模一样，唯一不同的就是——`xrange()`返回的是生成器，而不是直接的结果。
如果数据量大时，`xrange()`能极大的减小内存占用，带来卓越的性能提升。

当然，几百、几千的数量级，就直接用range好了。




## 多重yield

有时候我们可能会在一个函数中、或者一个for loop中看到多个`yield`，这有点不太好理解。
但其实很简单！

一般情况下，我们写的：
```py
for n in [1,2,3]:
    yield n**2
```

实际上它的本质是生成了这个东西：
```py
yield 1**2
yield 2**2
yield 3**2
```

**也就是说，不用for loop，我们自己手写一个一个的yield，效果也是一样的。**

你每次调用一次`next(..)`，就得到一个yield后面的值。然后三个yield的第一个就会被划掉，剩两个。再调用一次，再划掉一个，就剩一个。直到一个都不剩，`next(..)`就返回异常。
一旦了解这个本质，我们就能理解一个函数里写多个yield是什么意思了。

## 更深入理解yield：作为暂停符的yield

从多重yield延伸，我们可以开始更进一步了解yield到底做了些什么了。

现在，我们不把yield看作是return的替代品了，而是把它看作是一个`suspense`暂停符。
即每次程序遇到yield，都会暂停。当你调用`next(..)`时候，它再`resume`继续。

比如我们改一下上面的程序：
```py
def func():
    yield 1**2
    print('Hi, Im A!')

    yield 2**2
    print('Hi, Im B!')

    yield 3**2
    print('Hi, Im C!')
```

然后我们调用这个小函数，来看看yield产生的实际效果是什么：
```py
>>> f = func()
>>> f
<generator object func at 0x10d36c840>

>>> next( f )
1

>>> next( f )
Hi, Im A!
4

>>> next( f )
Hi, Im B!
9

>>> next( f )
Hi, Im C!
ERROR: StopIteration
```

从这里我们可以看到：
- 第一次调用生成器的时候，yield之后的打印没有执行。因为程序yield这里暂停了
- 第二次调用生成器的时候，第一个yield之后的语句执行了，并且再次暂停在第二个yield
- 第三次调用生成器的时候，卡在了第三个yield。
- 第四次调用生成器的时候，最后一个yield以下的内容还是执行了，但是因为没有找到第四个yield，所以报错。


**所以到了这里，如果我们能理解yield作为`暂停符`的作用，就可以非常灵活的用起来了。**


## `yield from`与`sub-generator`子生成器

`yield from`是Python 3.3开始引入的新特性。
它主要作用就是：当我需要在一个`生成器函数`中使用另一个生成器时，可以用`yield from`来简化语句。

举例，正常情况下我们可能有这么两个生成器，第二个调用第一个：
```py
def gen1():
    yield 11
    yield 22
    yield 33

def gen2():
    for g in gen1():
        yield g
    yield 44
    yield 55
    yield 66
```
可以看到，我们在`gen2()`这个生成器中调用了`gen1()`的结果，并把每次获取到的结果yield**转发**出去，**当成自己的yield出来的值**。

我们把这种`一个生成器中调用的另一个生成器`叫做`sub-generator`子生成器，而这个子生成器由`yield from`关键字生成。

由于`sub-generator`子生成器很常用，所以Python引入了新的语法来简化这个代码：`yield from`。

上面`gen2()`的代码可以简化为：
```py
def gen2():
    yield from gen1()
    yield 44
    yield 55
    yield 66
```
这样看起来是不是更"pythonic"了呢？:)

**所以只要记住：`yield from`只是把别人呕吐出来的值，直接当成自己的值呕吐出去。**


## 递归+yield能产生什么？

一般我们只是二选一：要不然递归，要不然for循环中yield。有时候yield就可以解决递归的问题，但是有时候光用yield并不能解决，还是要用递归。
那么怎么既用到递归，又用到yield生成器呢？

[参考：Recursion using yield](https://stackoverflow.com/questions/8991840/recursion-using-yield)

```py
def func(n):
    result = n**2
    yield result
    if n < 100:
        yield from func( result )

for x in func(100):
    print( x )
```

上面代码的逻辑是：如果n小于100，那么每次调用`next(..)`的时候，都得到n的乘方。下次next，会继续对之前的结果进行乘方，直到结果超过100为止。

我们看到代码里利用了`yield from`子生成器。因为yield出的值不是直接由变量来，而是由“另一个”函数得来了。




