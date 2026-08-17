# `pip 常用操作`
注意：
- 安装过程中尽管很多包需要sudo权限，但是，尽量不要sudo！最好的是在virtualenv下操作
- 一些常见问题，升级pip到10.0就解决了

```shell
## 安装pip
$ curl https://bootstrap.pypa.io/get-pip.py >> get-pip.py
$ python get-pip.py

## 安装包
pip install <package name>

## 删除包
pip uninstall <package name>

## 升级某个包
pip install --upgrade <package name>

## 安装某个版本的包
pip install django==1.9

## 升级自己
pip install --upgrade pip

## 显示模块包的安装路径
pip show <package name>

## 查看已经过期的软件（不是最新版）
pip list --outdated

## 列出已安装的包 (二者皆可)
pip list
pip freeze

## 导出已安装包到requirements.txt
pip freeze > requirements.txt

## 批量安装包
pip install -r requirements.txt

## 搜索包
pip search

## 查询可升级的包
pip list -o
```
