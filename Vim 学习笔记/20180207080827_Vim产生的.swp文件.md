# Vim产生的`.swp`文件
参考文章：[VIM不正常退出产生的swp文件](http://blog.csdn.net/pwiling/article/details/51830781)
常用关于swp文件的命令或`vimrc`配置：
- 查看当前目录下的所有swp文件: `vim -r`
- 恢复文件：`vim -r filename`，上次意外退出没有保存的修改，就会覆盖文件。
- 停止vim产生交换文件：在`~/.vimrc`中加入`set noswapfile`
- 定时自动保存文件：
```
set updatetime=23000 " 设置每200个字符保存一次
set updatecount=400 " 设置每4秒保存一次
" set updatecount=0 " 不保存交换文件
```
- 设置交换文件默认目录：`set directory=./tmp`
