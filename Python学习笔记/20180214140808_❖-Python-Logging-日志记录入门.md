# ❖  Python Logging 日志记录入门

> `Python Logging`原来真的远比我想象的要复杂很多很多，学习路线堪比git。但是又绕不过去，alternatives又少，所以必须要予以重视，踏踏实实认认真真的来好好学学才行。

学习Logging的目的：
简单脚本还好，print足够。
但是稍微复杂点，哪怕是三四个文件加起来两三百行代码，调试也开始变复杂起来了。
再加上如果是后台长期运行的那种脚本，运行信息的调查更是复杂起来。
一开始我还在各种查`crontab`的日志查看，或者是`python后台运行查看`，或者是`python stdout的获取`等等，全都找错了方向。
真正的解决方案在于正确的logging。
记录好了的话，我不需要去找python的控制台输出`stdout`，也不需要找`crontab`的日志，只需要查看log文件即可。
下面是python的logging学习记录。

### 最简单的日志输出（无文件记录）
```python
import logging
 
logging.error("出现了错误")
logging.info("打印信息")
logging.warning("警告信息")
```

## 首先，忘掉logging.info()! 忘掉logging.basicConfig()!
网上各种关于python logging的文章实在是太不体谅新手了，logging这么复杂的东西竟然想表现得很简单，还用各种简单的东西做假象。
实际上我们真正要用起来的日志，绝对是不会直接用`logging.info()`和`logging.basicConfig()`这样的，这是此模块的官方推出来迷惑人的——看似让你一键上手，快速看到结果，但是跟实际真的不搭！
所以为了后面解释起来轻松，必须先警告这点：忘记它们俩！
记住，唯一要用到`logging.`什么的，就只有`logging.getLogger()`这一次。

## 了解logging的工作流
不想上流程图一类的东西，那样反而更迷糊。
简单说吧：
`logging`模块是会自动将你自定制的logger对象`全局化`的，
也就是说，
你在自己的模块里只要定义了一次某个logger，比如叫`log`，那么只要是在同一个模块中运行的其他文件都能读取到它。
比如说，你在主文件`main.py`中自定义了一个logger，可能设置了什么输出文件、输出格式什么的，然后你在`main.py`中会引用一些别的文件或模块，比如`sub.py`，那么在这个`sub.py`中你什么都不用设置，只要用一句`logger = logging.getLogger('之前在main.py定义的日志名')`即可获得之前的一切自定义设置。

当然，被调用的文件（先称为子模块）中，用`logging.getLogger('日志名')`时，最好在日志名后加一个`.子名称`这样的，比如`main.sub`。这样输出的时候就会显示出来某条日志记录是来自于这个文件里了。当然，`.`前面的父级logger必须名字一致，是会被识别出来的！
然后，子日志还可以再子日志，甚至一个子模块可以再让所有函数各又一个子子日志，比如`main.sub.func1`这样的。logging都会根据`.`识别出来上下级关系的。

这样一说，实际上也就是class类继承的那种机制了。你按照父级名称继承，然后还可以改写自己的新设置等。

了解了这些概念以后，才能来谈代码。实际上也就好理解多了。

## 设置logger的方法
看来看去，这篇文章说得比较全面也最清楚，以下很多都参考到它的内容：[Python 101: An Intro to logging](https://www.blog.pythonlibrary.org/2012/08/02/python-101-an-intro-to-logging/)

一般想要自定义一个logger，比如让它输出信息时按照什么格式显示，输出到哪个文件，要不要输出到屏幕一类，有三种方法可以达到设置：
- 直接在python代码里设置
- 用外部的config.ini文件配置
- 用python的dict字典配置

三种达到的目的都是一样的，字典用的人很少也不方便，配置文件比较好用只是`.ini`的语法不是很方便读，且不容易做到变量的动态设置，所以一般直接在python代码里写就好。

## 常用设置语句

以下是程序主入口文件的通用写法，注意，一定要在主入口定义好logger，这样其他所有的子模块才能够继承到。
```python
#   main.py
import logging
import otherMod2   # 等下会调用到的子模块

def main():
    """
    这个文件是程序的主入口
    """

    define_logger()

    log = logging.getLogger('exampleApp')

    # 输出信息测试
    logger.info("Program started")
    result = otherMod2.add(7, 8)     # 这个是来自别的模块的方法
    logger.info("Done!")

def define_logger():
    logger = logging.getLogger("exampleApp")
    logger.setLevel(logging.INFO)

    # 设置输出格式
    formatter = logging.Formatter('\n%(asctime)s - %(name)s - %(levelname)s :\n\n\t %(message)s')
 
    # 设置日志文件处理器
    fh = logging.FileHandler("new_snake.log")
    fh.setFormatter(formatter)    # 为这个处理器添加格式

    # 设置屏幕stdout输出处理器
    sh  = logging.StreamHandler(stream=None)
    sh.setFormatter(formatter)
 
    # 把处理器加到logger上
    logger.addHandler(fh)
    logger.addHandler(sh)
 
if __name__ == "__main__":
    main()
```

下面是子模块中的调用方法（很简单）：
```python
# otherMod2.py
import logging
 
module_logger = logging.getLogger("exampleApp.otherMod2")

def add(x, y):
    # 这里一句`getLogger`就继承到父级的logger了
    logger = logging.getLogger("exampleApp.otherMod2.add")

    # 输出测试
    logger.info("added %s and %s to get %s" % (x, y, x+y))
    return x+y
```

注意，`主文件`中，在什么地方定义logger都可以，可以在`main()`里也可以在任何单独的函数或类里，无所谓。只要在调用子模块之前定义好了就可以了。一旦定义过，`日志名`就会被记下来，然后子模块就可以轻松继承到。
