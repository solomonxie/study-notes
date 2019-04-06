# VIM 编辑历史持久化的最佳实践 [DRAFT]


## Swap 缓存

```
" [  Swap files  ]--------{
    set swapfile    "enable swap file
    set directory=~/.vim/swap//    "set swp file directory.
    " Create folder if not exists
    if !isdirectory(&directory)
       silent! call mkdir(&directory, 'p')
    endif
    set updatecount=20     "save swp file every amount of characters
    " ▼ update also check cursor-holds and other functions, bit expensive one.
    set updatetime=4000   "save swap file every amount of ms
" }
```

### 为什么要关闭Swap？

Swap的缺点是：
- 如果同时编辑两个项目的同名文件，那么也会提示conflict冲突。而解决这个问题并不容易
- 如果已经保存了Undo历史，那么Swap就没有什么必要性了。如果是在Git版本控制下，就更没存在意义了。

如果要取消Swap，可以考虑这些更好的方案：
- 设置Undo
- 设置每次Buffer获得焦点时自动刷新文档内容 （如果同时在多处编辑同一个文件，很方便）


## Undo

基本设置：
```vim
    set undofile "Save UNDO history to local files
    set undodir=~/.vim/undo/
```
这样一来，Vim就会在你每次编辑一个文件时，在本地的`~/.vim/undo/`下为其创建一个**`二进制`**的历史文件，如`test.py`，和你编辑的`test.py`同名。

但是这样会产生一些问题：
- 多个项目的同名文件会互相覆盖
- 如果`~/.vim/undo/`文件夹不存在则不会创建任何文件
- 旧版本的VIM可能不支持这个功能

为了解决这些问题，配置修改为如下：
```vim
" [  Persistent undo  ]--------{
    if has("persistent_undo")
        set undofile "Maintain UNDO history between sessions
        set undodir=~/.vim/undo//
        " Create folder if not exists
        if !isdirectory(&undodir)
           silent! call mkdir(&undodir, 'p')
        endif
    endif
" }
```

上面`set undodir=~/.vim/undo//`中的`//`代表为文件产生一个标志了绝对路径的名称，这样就不存在冲突了。
如你正在编辑的`/tmp/project/test.py`，对应的undo文件名就是`%tmp%project%test.py`。


## Backup

```
" [  Backup Files  ]--------{
    set backupdir=~/.vim/backup//
    " Force backups to be copied from original, not renamed
    set backupcopy=yes
    " Create folder if not exists
    if !isdirectory(&backupdir)
       silent! call mkdir(&backupdir, 'p')
    endif
" }
```

## 如何指向文件的绝对路径

在结尾加`//`。



