# ❖ Linux上利用Find 查找文件

`find`命令可以在指定目录及里面所有子文件夹的文件里搜索。不光可以按文件名搜索，还可以结合根据内容搜索。

[参考：[linux命令] find使用梳理](https://juejin.im/entry/59abc4436fb9a0249a414cc3)

## 单纯查找
```sh
# 「文件名模糊搜索」
$ find . -name '*.jpg'

# 「类型为文件」
$ find . -type f

# 「类型为目录」
$ find . -type d

# 「空目录」
$ find . -empty

# 「包含文件」查找包含某个文件的目录 (利用test命令)
$ find . -type d -exec test -e "{}/index.html" \;

# 「包含文件」查找同时包含某几个文件的目录 （利用test命令的组合参数）
$ find .type -d -exec test -e "{}/a.jpg" -a -e "{}/b.jpg" \;

# 从指定目录里查找
$ find . -path "*folder*"

# 限制查找深度
$ find ./ -name "*.txt" -maxdepth 2

# 按文件大小查找 (b, k, M, G）
$ find . -size +1M
$ find . -size -100k

# OR / AND条件判断组合查找 (-a是AND，-o是OR，然后用括号扩起来）
$ find . -name "fileA" -o \( -name "fileB" \)

```


根据文件内容搜索：
[参考：Linux查找目录下的所有文件中是否含有某个字符串](https://ifhw.github.io/2016/03/25/find-the-file-contains-certain-strings/)

```sh
# 「内容中包含关键字的文件」
$ find . -name '*.txt' | xargs grep -ri 'KEYWORD'
```


## 对查找结果执行操作

```sh
# 「批量压缩」查找所有包含指定文件的文件夹，并压缩该文件夹
$ find . -type d -exec test -e '{}/index.html' \; -exec zip -r {}.zip {} \;

# 「批量移动」移动找到的内容
$ find . -name "*.mp4" -exec mv {} /path/to/destination/ \;

# 「批量重命名」重命名找到的内容
$ find . -name "*.mp4" -exec ......
```

## 排除查找

```sh
$ find . -not \( -path ./exclude/ -prune \)
```

注意：`-not \( -path ./exclude/ -prune \)`不能和`-delete`结合使用，如果要删除，需要用`-exec rm {} \;`
