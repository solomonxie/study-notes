# 修复pip2

即使机器同时安装了Pytho2和Python3，且能够执行`python2`和`python3`命令，但是可能会发现只有`pip3`，而没有`pip2`。

Mac上修复的话，最简单的方法就是如下两句话：
```sh
brew install python@2
brew reinstall python@2
```

[参考：Installing Python 2 on Mac OS X](https://docs.python-guide.org/starting/install/osx/)


Ubuntu上修复则是：
```sh
sudo apt-get install -y python-pip python3-pip
```
