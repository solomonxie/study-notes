# Vim里Insert模式下不能按Backspace删除前面的内容

因为默认当前插入只能创建新内容，不允许改动别的东西。如果要变成Insert mode下随便编辑的模式，在`~/.vimrc`中加上：
```
set backspace=indent,eol,start
```
或者更简单的`set backspace=2`，效果一样。
