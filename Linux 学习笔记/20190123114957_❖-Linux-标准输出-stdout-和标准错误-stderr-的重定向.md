# ❖ Linux 标准输出(stdout)和标准错误(stderr)的重定向

> 以前经常会听到这些词，还有标准输入之类，完全不明所以。直到最近需要让python脚本里的print内容打印到日志文件里，才开始研究这到底是什么。


原来，`标准输出(stdout)`指的就是在命令行里，每次你输入指令后，终端上打印出来的那些话，那些反馈。`标准错误(stderr)`跟标准输出差不多，只不过是程序出错时反馈的内容。`标准输入(stdin)`就是程序指示让你输入用户名密码之类的这种，这里不多谈输入。

问题是，我们很常用的会让一些脚本自己在后台24/7运行，这种时候脚本的输出内容到屏幕上（标准输出）也没什么意义，我们看不到也保存不了。所以最好让它把反馈的内容全部直接写如一个文件里，我们叫日志文件，其实就是个txt。然后我们自己可以查看日志来看到底发生了什么。


> 这种把显示到屏幕的程序反馈，变成存到文件里的动作，我们叫做`输出重定向(stdout redirection)`

在命令行里，我们可以用符号直接把程序输出`转向`到某个文件或某个程序，如下：
```shell
$ git push > log.txt
```
然后，理论上我们平常`git push`后的反馈就会保存到`log.txt`这个文件里了，且屏幕上不会显示任何东西。
但其实这个还是有问题的，因为事后我们发现有一些存到了log.txt，还有一些话漏网显示到了屏幕上，没存进去文档里。
其实原来这些显示到屏幕上的反馈有些是`stdout`有些是`stderr`，我们用`>`或`>>`符号重定向，只是默认重定向`stdout`，没有重定向`stderr`，所以会有漏网之鱼。对此，我们需要了解下这个符号的设定，和怎么把`stderr`也包括进来，一起重定向过去。

## 重定向符号和语句
稍微会一点点linux命令的，都会用到`cmd > file`这样的语句，把命令反馈的输出到一个文件里。当然还有`cmd >> file`，这是把内容追加到文件里，而不是重新擦写一遍。`>`这个符号可以念`redirect to`。
实际上，重定向有很多种设置和配合，让你可以分别重定向标准输出和标准错误，或者一起重定向，然后还可以选择是只输出到文件里还是同时输出大显示屏上和文件里。
这里我们就要了解一下设置重定向的基本语法了，如下：

- `>`   以擦写的模式重定向至... 
- `>>` 以追加的模式重定向至...
- `1`  代表`stdout`标准输出
- `2` 代表`stderr`标准错误

所以，`cmd > file`实际上是缩略了的写法，理解起来，应该是`cmd &1> file`，也就是只把标准输出转出去。
那么同理，只把标准错误转出去，就应该是`cmd &2> file`。
其中，`&`符号没任何实际意义，只是以至区分，代表后面的符号是要设置重定向用的，而不是某个文件的名字。

## 关于"2>&1"

每次查重定向问题时，我们总会看到这句话，一般人很难理解这到底是在干嘛。我一开始以为是2要大于1什么的，真是笑话。
其实这是个重定向的设置，设置让2重定向到1，也就是让`stderr`标准错误重定向到`stdout`标准输出，然后两个并在一起再重定向。其中`&`没什么意思只是区分开来1是代表`stdout`而不是代表一个文件名。
用起来的格式是：`cmd > file 2>&1`。
为什么设置要放在后面呢?
具体暂时还不知道，只知道是这么用，放在前面还不行只能放在后面。

比如：
```shell
$ git push > log.txt 2>&1
```
那么这时候，屏幕上就真的不会显示任何东西了，标准输出、标准错误，全部都会存到log.txt文件里了。


## 关于"1>&2"
这个是比较好用的方法：即程序输出到屏幕，也输出到文件。


## 常用重定向及解释

#### 参考文章：[stackoverflow回答](https://askubuntu.com/questions/420981/how-do-i-save-terminal-output-to-a-file)

![image](20190123114957_❖-Linux-标准输出-stdout-和标准错误-stderr-的重定向_files/img_01.png)

- `command > output.txt`

The standard output stream will be redirected to the file only, it will not be visible in the terminal. If the file already exists, it gets overwritten.

- `command >> output.txt`

The standard output stream will be redirected to the file only, it will not be visible in the terminal. If the file already exists, the new data will get appended to the end of the file.

- `command 2> output.txt`

The standard error stream will be redirected to the file only, it will not be visible in the terminal. If the file already exists, it gets overwritten.

- `command 2>> output.txt`

The standard error stream will be redirected to the file only, it will not be visible in the terminal. If the file already exists, the new data will get appended to the end of the file.

- `command &> output.txt`

Both the standard output and standard error stream will be redirected to the file only, nothing will be visible in the terminal. If the file already exists, it gets overwritten.

- `command &>> output.txt`

Both the standard output and standard error stream will be redirected to the file only, nothing will be visible in the terminal. If the file already exists, the new data will get appended to the end of the file..

- `command | tee output.txt`

The standard output stream will be copied to the file, it will still be visible in the terminal. If the file already exists, it gets overwritten.

- `command | tee -a output.txt`

The standard output stream will be copied to the file, it will still be visible in the terminal. If the file already exists, the new data will get appended to the end of the file.

- `(*)`

Bash has no shorthand syntax that allows piping only StdErr to a second command, which would be needed here in combination with tee again to complete the table. If you really need something like that, please look at "How to pipe stderr, and not stdout?" on Stack Overflow for some ways how this can be done e.g. by swapping streams or using process substitution.

- `command |& tee output.txt`

Both the standard output and standard error streams will be copied to the file while still being visible in the terminal. If the file already exists, it gets overwritten.

- `command |& tee -a output.txt`

Both the standard output and standard error streams will be copied to the file while still being visible in the terminal. If the file already exists, the new data will get appended to the end of the file.

