# 树莓派安装python的lxml库失败问题

参考：https://kinegratii.github.io/2017/05/14/install-lxml-on-respberry-pi/

需要先安装开发依赖才能正确的通过pip编译安装：
```sh
sudo apt-get install libxml2-dev libxslt-dev python-dev -y
pip3 install lxml --user
```
