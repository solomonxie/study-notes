# Jupyter Notebook改变默认打开的浏览器 [DRAFT]

因为有开双浏览器的习惯，不喜欢Jupyter默认打开Chrome。所以希望它默认打开Opera。

[参考：Jupyter: Os X 下修改默认打开的浏览器](https://n3xtchen.github.io/n3xtchen/data_analytics/2016/12/03/jupyter-default-browser)

以下是Mac上修改默认浏览器方法：
```sh
# 先生成一个本地配置文件，以供修改
$ jupyter notebook --generate-config

# 修改刚刚生成的配置文件(.py文件)
$ vim ~/.jupyter/jupyter_notebook_config.py

# 搜索"browser"找到配置行

```
