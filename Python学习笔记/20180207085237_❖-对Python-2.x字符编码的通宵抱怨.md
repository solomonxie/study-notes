# ❖ 对Python 2.x字符编码的通宵抱怨

`首作时间：Dec 8, 2015`

**总之对于这个我唯一认定的事就是：Python里要是弄不明白编码，那这个语言就放弃吧！**

下面是目前收获到的一些内容，没写完，再议吧。。。

首先要在文件第一行写上`编码声明`

```
#coding:utf-8
```

编码声明的格式其实很随意的，coding=utf-8, -_\- Coding:Utf-8 -_\- 等等都行，  
Python只识别关键的字。  
如果不写编码声明，那么文件中出现的任何中文都会报错：  
`SyntaxError: Non-ASCII character '\xe5' in file xx.py on line 2, 
    but no encoding declared; see http://python.org/dev/peps/pep-0263/ for details`

Python 2.x 系列对中文真是弱爆了，查了巨多的文献，还是不那么明了。  
本来想要练习开发个什么小程序，结果全都被扼杀在编码的坑里了。  
随便搜一搜"Python 编码"就知道，所有作者们都遇到了一毛一样的问题。。。  
据说，

```
除非把整个编码系统从古至今的历史熟透，各编码的原理通透，
相互之间的转换了熟于胸，Python的这个坑是跨不过去的。小看了这小玩意儿！  
```

下面开始正式研究下吧，争取能做到practical。

这是原始汉字数据：

```
chinese = '你好' # 普通中文字符串
uni = u'你好' # 字符串前加u代表转换为unicode变量类型
```
# 研究一个原始的中文字符串

在IDLE命令行中执行一下试试

```
>>> chinese
'\xc4\xe3\xba\xc3'
>>> print chinese
你好
>>> type(chinese)
<type 'str'>
```

这是什么鬼！为什么直接输变量名和打印变量名会不一样呢？！
静悄悄的理解一下，应该是：
chinese变量在内存中存储的就是`\xc4`这种编码，是给机器看的
而print打印出来的是给人看的，所以python要处理一下让人能看懂。
再来说，`\xc4`这是个什么码？而且`你好`是两个字，为什么编码里有4个`\x$$`这种？
所以推理到，python对每个汉字是用2个编码来存储的。
首先能确定的是，`\x$$`这种格式是ASCII编码，因为百科到如下：

> ASCII(American Standard Code forInformation Interchange)，是一种单字节的编码。计算机世界里一开始只有英文，而单字节可以表示256个不同的字符，可以表示所有的英文字符和许多的控制符号。不过ASCII只用到了其中的一半（\x80以下）

也就是说，英文字母用`\x01`到`\x80`之间的数表示，数字不用编码，
那么汉字这种国外字就全部都是从`\x80`往后排了。因为字太多，肯定不够用，所以:
1. 格式变成了'\x字母数字'这种东西
2. 而且还用两个字节码来表示一个中国汉字。
## 用chardet检测字符串编码

那么来检验一下我的推理吧？用个第三方模块`chardet`  

``` python
import chardet
print chardet.detect('你好')
# [结果]: {'confidence': 0.3598212120361634, 'encoding': 'TIS-620'}
```

这什么鬼！！为什么检测出来有35%的`TIS-620编码`？
不能放弃，我再来试一试：

``` python
import chardet
print chardet.detect(str('你好'))
# [结果]: {'confidence': 0.3598212120361634, 'encoding': 'TIS-620'}
print chardet.detect(repr('你好'))
# [结果]: {'confidence': 1.0, 'encoding': 'ascii'}
```

真是受够了。。。
为什么检测`str()`出来的就是`TIS-620`，而检测`repr()`出来的就是`ASCII`呢？
Python世界中，str和repr到底谁才更接近本源、谁才是出来捣乱的呢？
唉算了吧，不用这个了。
## str 和 repr 在存储和print打印上的对比

我又想起了一个实验，我们再来一下：

```
>>> repr('你好')
"'\\xc4\\xe3\\xba\\xc3'"
>>> print repr('你好')
'\xc4\xe3\xba\xc3'
>>> str('你好')
'\xc4\xe3\xba\xc3'
>>> print str('你好')
你好
```

什么毛病！据说`repr()`和`str()`是一样的啊！怎么会这样呢？
实验里，`repr()`和`str()`的内存数据的确是一样的，但是一print就不一样了：
只有print `str()`才会显示出中文！
那可能是print的问题了。那是不是说如果我不print，而是别的操作如存到文件中，那么就不会有中文出现了？试试吧：

``` python
f = open('test.txt', 'w')
f.write(str('你好'))
f.write(repr('你好'))
# [结果]：你好 '\xe4\xbd\xa0\xe5\xa5\xbd'
```

也就是说不是print的问题了，`str()`和`repr()`在本质上就是有区别的。
只有`str()`会把中文显示出来，而`repr()`不但会把中文显示成`ASCII码`，
还会异常搞笑的把在print里显示4位字节码变成6位字节码！！！这是什么毛病？！
好吧，这个先留着，来看看转成了unicode的中文吧。
# 研究已变成unicode类型的中文字符串

好吧，再来试一试uni：

```
>>> uni
u'\u4f60\u597d'
>>> print uni
你好
>>> type(uni)
<type 'unicode'>
```

这又是什么鬼！我原先的想象是，
print一个unicode对象，肯定出来的是unicode码，但两种方法的结果完全反了。。。
再静悄悄的理解下，uni肯定也是在内存中存储的是unicode编码。
在python中unicode的格式是：u'\u$$$$'，其中$$$$代表4位的字符编码。
然后又试了一下这个：
## str(unicode类型) 和 repr(unicode类型) 结果的对比

```
>>> str(uni)
.......
UnicodeEncodeError: 'ascii' codec can't encode characters in position 0-1 ......
>>> repr(uni)
"u'\\u4f60\\u597d'"
```
## str()和repr()的对比

这个好理解，用`help(str)`命令可以看到：
str(`basestring`)是将某个object变成一个漂亮的易观看的字符串。
并且，它需要的是basestring类型变量作为参数。
而`help(repr)`只是简单说，repr(`object`)会返回这个object的规范化字符串。
它对参数并没有什么要求。
这样对比来看的话，str和repr在**in**和**out**上都不一样。
str 对谁进来有限定，出去要漂亮要好看；
repr对谁进来无所谓，出去也够标准就行。
# 原始中文字符串和unicode格式的中文字符串对比

暂时写不下去了，再议吧。。。。。。。。


## 这些事我目前为止收集到的Python 编码相关文章，还没解决问题。

### 都是PDF的~~~ 最近养成了“好习惯”，看过的网页都一键转成PDF，一边做笔记，一边存档。这样以后也容易翻了。不像以前看过了，解决了，就丢到脑后了，然后过一阵子不用，又重新查一遍。

[【整理】Python中实际上已经得到了正确的Unicode或某种编码的字符，但是看起来或打印出来却是乱码 _ 在路上.pdf](https://github.com/solomonxie/solomonxie.github.io/files/55250/Python.Unicode._.pdf)
[【整理】Python中用encoding声明的文件编码和文件的实际编码之间的关系 _ 在路上.pdf](https://github.com/solomonxie/solomonxie.github.io/files/55251/Python.encoding._.pdf)
[【整理】关于Python脚本开头两行的：#!_usr_bin_python和# -_\- coding_ utf-8 -_-的作用 – 指定文件编码类型 _ 在路上.pdf](https://github.com/solomonxie/solomonxie.github.io/files/55254/Python._usr_bin_python.-_-.coding_.utf-8.-_-._.pdf)
[【总结】Python 2.x中常见字符编码和解码方面的错误及.pdf](https://github.com/solomonxie/solomonxie.github.io/files/55252/Python.2.x.pdf)
[ITArticles_Python的中文显示方法.pdf](https://github.com/solomonxie/solomonxie.github.io/files/55253/ITArticles_Python.pdf)
[Python - 编码转换 - 生命不息，学习不止！ - 博客频道 - CSDN.pdf](https://github.com/solomonxie/solomonxie.github.io/files/55255/Python.-.-.-.-.CSDN.pdf)
[Python repr() 或str() 函数 - mingaixin - 博客园.pdf](https://github.com/solomonxie/solomonxie.github.io/files/55256/Python.repr.str.-.mingaixin.-.pdf)
[python 编码转换 [Python俱乐部].pdf](https://github.com/solomonxie/solomonxie.github.io/files/55257/python.Python.pdf)
[Python2.x的编码问题.pdf](https://github.com/solomonxie/solomonxie.github.io/files/55258/Python2.x.pdf)
[Python编码和Unicode - 博客 - 伯乐在线.pdf](https://github.com/solomonxie/solomonxie.github.io/files/55259/Python.Unicode.-.-.pdf)
[Python的中文编码问题 - WuXianglong - SegmentFault.pdf](https://github.com/solomonxie/solomonxie.github.io/files/55260/Python.-.WuXianglong.-.SegmentFault.pdf)
[python读写文件，和设置文件的字符编码比如utf-8 - 为程序员服务.pdf](https://github.com/solomonxie/solomonxie.github.io/files/55261/python.utf-8.-.pdf)
[Python语言十分钟快速入门.pdf](https://github.com/solomonxie/solomonxie.github.io/files/55262/Python.pdf)
[python中文编码详解 - Cody的笔记本 - 博客频道 - CSDN.pdf](https://github.com/solomonxie/solomonxie.github.io/files/55263/python.-.Cody.-.-.CSDN.pdf)
[初探python编码 - LX - 博客频道 - CSDN.pdf](https://github.com/solomonxie/solomonxie.github.io/files/55264/python.-.LX.-.-.CSDN.pdf)
[中文字符编码标准+Unicode+Code Page _ 在路上.pdf](https://github.com/solomonxie/solomonxie.github.io/files/55265/Unicode.Code.Page._.pdf)
[字符串，那些你不知道的事 _ Keep Writing Codes.pdf](https://github.com/solomonxie/solomonxie.github.io/files/55266/_.Keep.Writing.Codes.pdf)

