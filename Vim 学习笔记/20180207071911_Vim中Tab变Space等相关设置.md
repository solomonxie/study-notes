# Vim中Tab变Space等相关设置
Tab和Space之争和Vim于Emacs是一样等，我是Vim和Space派。但是我和大多数人一样喜欢按Tab出Space。
在`~/.vimrc`中设置如下，重启vim就会生效：
```
set autoindent "换行时自动缩排 同时对应的还有其它两种模式 smartindent, cindent
set tabstop=4 "设定tab宽度为4个字符
set shiftwidth=4 "设定自动缩进为4个字符
set expandtab "用space替代tab的输入 取消的话 就用set noexpandtab "不用space替代tab的输入
retab "打开文件时自动转换所有tab为空格
```
