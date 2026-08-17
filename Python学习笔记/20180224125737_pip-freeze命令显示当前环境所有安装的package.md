# `pip freeze`命令显示当前环境所有安装的package
对于我们经常使用virtualenv虚拟环境来说，经常需要指明需要哪些python package倚赖包。另外由于virtualenv如果和git仓库共存的状况下，我们必须要屏蔽文件夹里所有virtualenv的内容，所以这种情况更需要有一个显示的方法指明项目需要哪些倚赖包。
很简单的一句话就搞定：
```
pip freeze > requirements.txt
```
这样的话，pip就会自动显示出当前环境下已安装的所有package包，并且利用`>`重定向，输出到一个txt文档里。
以后的话，还可以用这个txt文件达到一键安装所有倚赖：
```
pip install -r requirements.txt
```
