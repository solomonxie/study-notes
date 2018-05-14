# Vim 文件操作
[参考：在 Vim 中进行文件目录操作](https://harttle.land/2016/10/14/vim-file-and-directory.html)

```vim
# 新建文件/打开文件
: e [FILE-NAME]

# 新建文件 （只打开半个窗口 另半个窗口保留之前的文件）
:new [FILE-NAME]

# 退出 (如果文件更改则保存)
:x 
```

## 打开目录
```vim
:e FOLDER-PATH    " 编辑该目录
:Explore .      " 浏览该目录
:Sexplore .     " 在水平分割窗口中浏览该目录
:Vexplore .     " 在垂直分割窗口中浏览该目录
```

## 调用bash命令
```vim
# 列出文件
:!ls

# 删除文件
:!rm foo.txt
```
