# Git 更改文件夹名称

因为直接用`mv`更改文件夹名称，会被git识别为删除了旧文件创建了新文件，也就丢失了追踪，所以我们要用`git mv`命令。

如果是想改文件夹名称的大小写，那么就要麻烦一点：
```sh
$ git mv MyName temp && git mv temp myname
```
