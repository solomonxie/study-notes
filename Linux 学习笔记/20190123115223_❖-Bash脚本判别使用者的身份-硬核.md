# ❖ Bash脚本判别使用者的身份 (硬核)

经常要在bash脚本里面或者直接对脚本本身加上`sudo`运行命令，但是这引发了一系列的问题。

比如用sudo的时候，脚本里的`~`或`$HOME`指代用户文件夹的这个变量，到底是应该指向我真正的用户文件夹如`/home/pi`呢，还是指向了超级管理员的用户文件夹`/root/`呢？

实际上它指向了`/root/`文件夹，这是我们绝对不想要的。但是很多命令如安装个程序，都不得不用`sudo`，那怎么办？

首先要说下经验：命令行的权限执行，从表现上来看，可以分为以下5种情况：
- `admin-manual`: 普通用户手敲命令
- `sudo-manual`: 手敲命令加sudo
- `admin-bash`: 以普通用户执行bash脚本
- `sudo-bash`: 以sudo执行bash脚本
- `root-any`: 以root用户登录

很多变量、环境变量在这4中情况下，会经常出现混乱！（混乱指的是我们自己，不是电脑）

> 另外，说个小技巧。
我们都直到`~`变量是指向`当前`用户目录，实际上`~abc`格式的变量可以指向`指定用户的`用户目录，如`~pi`会指向`/home/pi`，或`~ubuntu`指向`/home/ubuntu`.

理清一下思路：
在正常执行脚本如`./test.sh`时是没有任何问题的，即使脚本里面出现了sudo如`sudo apt-get update`这样也是没有问题的。
也就是说，就只有对整个脚本执行sudo的情况下如`sudo ./test.sh`，才会出现严重问题的！

那么假设我的真实用户是`pi`，而HOME目录在`/home/pi`，现在我要在`sudo ./test.sh`这样的执行方式下找出正确的解决方案。
以下为脚本中的各种语句和变量以及显示结果：
```sh
# （不推荐！）
$ whoami
>>> root

# 不同于whoami，能够指出当前有哪些用户登录电脑，包括本机登录和ssh登录的所有人
$ who am i
>>> 有些机器上显示为空
>>> Mac上显示:  pi ttys001  Nov 26 16:57

# 等同于whoami （不推荐！）
$ echo $USER
>>> root

# 用户主目录位置 (不靠谱不推荐！）
echo $HOME
>>> /root

$ 用户主目录位置，等同于$HOME （不推荐！）
$ echo ~
>>> /root

# 直接使用环境变量LOGNAME
$ echo $LOGNAME
>>> root

# 显式调用环境变量LOGNAME 
$ printenv LOGNAME
>>> root


# SUDO_USER是root的ENV中的环境变量，
# 同时普通用户的env是没有的，只有root用户才能显示出来
$ sudo echo $SUDO_USER
>>> pi


# 显示调用环境变量SUDO_USER （不推荐！）
# 从结果中可以看到，即使是sudo身份执行的脚本，脚本里面是否加sudo也会不同！
$ printenv SUDO_USER
>>> pi
$ sudo printenv SUDO_USER
>>> root
```

从上面测试中可以看出，如果我们是用sudo执行bash脚本的话，很多变量都是“不靠谱”的。
Stackoverflow中，比较一致性的倾向就是使用`$SUDO_USER`这个`环境变量`。而测试中也的确，它是最“稳定的”，即在不同的权限、OS系统下，都能始终如一(只限有sudo的系统）。

那么现在我们有了用户名，就可以用`~pi`这样的命令获取主目录`/home/pi`了，但是！
这时候问题又出现了：手敲时候，我们可以获得`~pi`的正确地址，但是脚本中却不识别`~pi`是个什么东西，顶多是个字符串，没法像变量一样。
那既然是这样，我们就不能用`~abc`方法了，改用虽然老套但是绝对不混乱的方法：
从`/etc/passwd`中直接看。

手动的话可以直接打开passwd查看，脚本里面就比较麻烦，最方便的是用系统命令`getent`即Get Entries命令，获得指定用户的信息：
```sh
$ getent passwd pi
>>> pi:x:1000:1000:,,,:/home/pi:/bin/bash
```

那么，剩下的是有把其中的`/home/pi`取出来了，我们用`cut`就轻松取出。
所以全部过程如下：
```sh
me=$SUDO_USER
myhome=`getent passwd $me | cut -d: -f 6`
```
顺利得到`/home/pi`！


再进一步，如果脚本没有以sudo方式运行呢？这时候root用户和普通用户的环境变量下都是没有`SUDO_USER`这个变量的。那么就需要加一步判断了：
```sh
me=${SUDO_USER:-$LOGNAME}
myhome=`getent passwd $me | cut -d: -f 6`
```
即如果SUDO_USER为空，则正常使用$LOGNAME获取当前用户。为什么不用$USER而是用$LOGNAME呢？因为USER不是每个系统都有，但是LOGNAME是*nix系统下都会有的。



## 更新

由于部分OS不能正确获取LOGNAME，所以统一采用uid的方式获取用户路径：

```sh
HOUSE=`getent passwd ${SUDO_UID:-$(id -u)} | cut -d: -f 6`
```


## 再更新

MacOS没有`/etc/passwd`，也不支持`getent passwd <UID>`方式获取用户信息，但是sudo下也能保持$USER和$HOME变量内容不变。
所以更改为下：
```sh
HOUSE=${$(`getent passwd ${SUDO_UID:-$(id -u)} | cut -d: -f 6`):-$HOME}
```

即如果`getent`方式无法获取内容，则直接取$HOME的值。


## 再再更新

因为bash不支持以上嵌套的三元运算表达式，所以要拆开：
```sh
HOUSE="`cat /etc/passwd |grep ${SUDO_UID:-$(id -u)} | cut -d: -f 6`"
HOUSE=${HOUSE:-$HOME}
```


## 再再再更新

如果是root的话，grep uid的时候会匹配到passwd中所有含0的行，所以要改进为以下：
```sh
HOUSE="`cat /etc/passwd |grep ^${SUDO_USER:-$(id -un)}: | cut -d: -f 6`"
HOUSE=${HOUSE:-$HOME}
```
