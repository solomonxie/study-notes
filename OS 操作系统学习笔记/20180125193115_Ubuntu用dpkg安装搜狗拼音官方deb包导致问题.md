## Ubuntu用dpkg安装搜狗拼音官方deb包导致问题

在搜狗拼音for linux官网上，下载deb包后正常`dpkg -i xx.deb`后，
基本上都会出现安装错误，尤其是elementaryOS等ubuntu based系统
这个时候非常尴尬，安装包无法删掉， 而且导致连apt-get大多数功能都无法用。
网上居多方法都没用。
才找到简单的方法：在试过正常删除后，删掉`sogoupinyin`相关一切文件就ok了

```
sudo rm -rf /var/lib/dpkg/info/sogou*
sudo apt-get -f install
sudo apt-get update
```
