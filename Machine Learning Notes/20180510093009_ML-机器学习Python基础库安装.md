# ML 机器学习Python基础库安装
> 强烈建议在Virtualenv虚拟环境下安装所有的包，这样既不会和什么Anaconda冲突，又不会发生装不上、装错了、误删除等乌七八糟的事情。

建议进入Python3的虚拟环境：
```shell
$ source ~/VIRTUALENV-PATH/venv3/bin/activate
```

## 必备库安装


`Numpy`安装:
```sh
$ pip install numpy

# 或使用国内源
$ pip install numpy -i http://pypi.douban.com/simple --trusted-host pypi.douban.com
```

`Pandas`安装:
```sh
$ pip install pandas

# 或使用国内源
$ pip install pandas -i http://pypi.douban.com/simple --trusted-host pypi.douban.com
```

`Scikit-Learn`安装：
```sh
$ pip install scikit-learn

# 或使用国内源
$ pip install scikit-learn -i http://pypi.douban.com/simple --trusted-host pypi.douban.com
```

`matplotlib`安装:
```sh
$ pip install matplotlib

# 或使用国内源
$ pip install matplotlib -i http://pypi.douban.com/simple --trusted-host pypi.douban.com
```

`scipy`和`seaborn`安装：
```sh
$ pip install seaborn scipy

# 或使用国内源
$ pip install seaborn scipy  -i http://pypi.douban.com/simple --trusted-host pypi.douban.com
```
