# 获取pip安装可执行工具的PATH路径

```sh
# 获取安装包的位置
$ python -m site --user-base
/home/appannie/.local

# 把bin可执行路径放大PATH里：
echo "export PATH='$PATH:`python -m site --user-base`/bin'" >> ~/.bashrc
```


