# ❖ Python Package Import 之痛 [DRAFT]

[参考Python官方：Packages](https://docs.python.org/3/tutorial/modules.html#packages)
[▶参考：Python相对导入一处不解](https://segmentfault.com/q/1010000007114996)
[参考：使用相对路径名导入包中子模块](https://python3-cookbook.readthedocs.io/zh_CN/latest/c10/p03_import_submodules_by_relative_names.html)

## 理解Package

Python里，就像所有的`.py`文件被称为`Module`模块一样，所有的文件夹都被称为`Package`包。前提是，这个文件夹里有一个`__init__.py`文件，可以是空文件也可以有一些方便都内容。

一旦一个文件夹可以被视为`Package`，那么其中的所有文件都会有独立的Namespace命名空间，即变量都不共享，与其它的package完全独立。一个项目里，可以有很多个子文件夹、子子文件夹，一旦变成package，那么它们都能互相独立，方便我们引用。



## 理解sys.path

> Python的目录结构中，“向当前脚本以下的目录import”永远不会出问题，出问题的，总是“向上一层目录import”

在Python的运行一个`.py`脚本的时候，会自动将`sys.path`设置为**脚本所在目录**。然后凡是这个`sys.path`之下的所有的文件模块，都能直接import导入。
但是，很明显的，只有这个`.py`脚本之内的目录才包括在path里，也就是说它之外的所有事情它都一无所知。相当于Linux shell中的PATH。

在Python的导入逻辑里，非常／非常／非常重要的一点必须时时刻刻记在心上：
**启动脚本所在的目录，将持续作为`当前目录`来运行所有导入的模块。**

也就是说，如果你要导入另一文件夹的模块，而那个模块依赖于它同级目录的一个模块，这个时候它是不能直接导入同级目录模块的！因为当前的path已经变了！

比如，目录结构如下：
```sh
Project
├── __init__.py
├── main.py
├── sub1
│   ├── __init__.py
│   ├── common1.py
│   ├── mod1.py *
└── sub2
    ├── __init__.py
    ├── common2.py
    └── mod2.py *
```
假设，我们在`mod1.py`中使用`from common1 import *`来引用同级目录的`sub1/common1.py`。
同时，我们在`mod2.py`中使用`from common2 import *`来引用同级目录的`sub2/common2.py`。
另外，我们在`mod1.py`中需要导入`mod2.py`。（先略过具体实现方法）

那么问题出现了：
当我用`$ python mod1.py`时候，当前的path是`project/sub1/`，导入`mod2.py`后，它在执行`from common2 ...`的时候，理所当然的是找不到的，因为sub1中没有common2.py这个文件！



## 理解Python模块的相对引用和绝对引用

那么现在，我们应该做什么呢？改变`mod2.py`中的导入路径吗？
当然不行！我们不能随便改一个Package的导入逻辑，如果这个package是别的作者写的怎么办？如果改了以后，那个package以自身为`入口`时候运行怎么办？这些全都会乱套。

所以，解决方案是：
> **强制要求从整个项目的顶层用`python -m project.sub1.mod1`来设置端正的PATH路径。** 然后其它所有子模块、子包都用`from project.sub2 import mod2`这样的完整项目引用的语句来导入。

这个做法是PEP官方推荐的，也是合逻辑的，即：
一个完整的项目运行就应当以项目为入口来运行所有的`子module`或`子package`。
如果又想让某个子package被同项目的其它子package引用，又想单独运行，那就应当彻底把它从文件夹里抽离出来变成一个单独的“第三方库”来用。

那么具体应该怎么修改各个文件中的导入语句呢：
- 删除每个文件中的相对引用，如`from common1 import *`。
- 改为项目级别的绝对引用，如：`from project.sub2 import mod2`
- 如果需要运行／测试某个子模块的文件，需要cd切换到项目目录的再上一层中，执行：`python -m project.sub1.mod1`。注意，这里的命名是包／模块式的，不能以`.py`结尾！




## Sibling Package Imports 父目录中的同级目录导入

具体问题来了：怎么导入父级目录中的其它模块或包呢？

再复习一下我们的目录结构：
```sh
Project
├── main.py
├── sub1
│   ├── common.py
│   ├── mod1.py *
└── sub2
    ├── common.py
    └── mod2.py *
```

目的：在`sub1/mod1.py`中，导入`sub2/mod2.py`。同时，`mod2.py`中还需要导入同目录的`common.py`才能工作。

这是一个项目里再正常不过的操作了，可是如果你尝试google一下的话，可能会花费你数小时，结果还是让你自己的大脑Stack-overflow.

目前stackoverflow会有人提供这几种hacks来实现我们的目的：
- 在`mod1.py`中用`sys.path.append('..')`来把父级目录加到path中引用
- 用`from ..sub2 import mod2`来实现相对引用
- 直接`from project.sub2 import mod2`
- 在`__init__.py`进行一些path设定或import导入。

经过不断的实践，发现他们大都没说清楚上下文，甚至没有告诉完整的解决方案。
总结出的经验就是：以上的那些hacks终究是hacks，不是官方推荐的，也不能真正派上用场。

比如`sys.path.append()`方法，一开始似乎走通了不报错。但是真实项目走起来，比不可能给每个文件都加一句`sys.path.append()`。走到最后，你用`print( sys.path )`会发现path中莫名其妙多了很多很多路径。这肯定不行，也没见过任何项目源码里这么写的。

再比如`from ..sub2 import *`这样的相对引用，能这么用的上下文必须是：执行脚本时要是从文件夹顶级入口执行，如果直接从`mod1.py`执行脚本，那么这句话是会报错的。

所以还是用官方推荐的方法和逻辑，丢弃那些hacks吧。

要达到`sibling imports`，在这个例子里，具体做法是：
- 修改所有的模块mod1.py和mod2.py，把导入语句改为`from project.sub? import mod?`这样的。
- 如果要导入具体某个模块中的类或函数，则：`from project.sub?.mod? import MyClass`
- 执行子包中的某个子模块时，cd到project目录再往上一层，输入`python -m project.sub1.mod1`执行
- 执行整个项目的话，就`python -m project`


## `__init__` 和 `__all__` 限制导入模块

[参考Python官方： Importing ✱ From a Package](https://docs.python.org/3/tutorial/modules.html#importing-from-a-package)

Python规定：
如果在一个package包中的`__init__.py`中写上`__all__ = ['模块1', '模块2', '模块3']`的话，
那么在其它模块引用这个package包使用`from PACKAGE import *`这种用法的时候，
就**不会**真的引用包中所有的模块（那样会很耗内存），而只能导入作者在`__all__`里规定的模块。





## `__init__` 和 `__path__` 多层次目录导入

[参考Python官方：Packages in Multiple Directories](https://docs.python.org/3/tutorial/modules.html#packages-in-multiple-directories)

