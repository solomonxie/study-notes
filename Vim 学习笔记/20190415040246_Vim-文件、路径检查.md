# Vim 文件、路径检查


判断是否存在某文件夹：
```vim
if isdirectory('.git')

if isdirectory('../.git')

if isdirectory(expand('~/.vim/.git'))
```

判断某文件是否存在：
```vim

```


判断某文件是否可读(是否存在)：
```vim
if filereadable(expand('.git/workspace.vim'))
```
