# Vim的自动缓存文件`.swp`
Vim不会帮你自动保存当前文件，但是它会帮你创建一个缓存文件，一旦不正常退出或掉线，你能通过这个文件快速recover恢复过去。

恢复文件的命令：
```shell
# 如果是在vim内
:rec

# 如果是在vim外
vim -r FILENAME
```

[参考：VIM不正常退出产生的swp文件](https://blog.csdn.net/pwiling/article/details/51830781)

找到`~/.vimrc`加入这些内容可以设置缓存文件：
```vim
" ---- Swap files (for recovery) ----
set swapfile    "enable swap file
set updatetime=23000   "save swap file every amount of ms
set updatecount=20     "save swp file every amount of characters
set directory=/tmp    "set swp file directory. 
```
