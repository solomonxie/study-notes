#  ❖ 理解Vim Buffer缓冲区：多文件编辑方案

> Buffer听起来很高大尚，实际上的功能和Tab、window是一模一样的。只是这些东西的内在实现不一样而已了。

Buffer是Vim自带的多文件编辑方式，有了它其实你不用单装Nerdtree插件来实现多标签编辑。
这是看个人习惯吧。
虽然我已经习惯了用Nerdtree做多文件多标签编辑，但是学习一下Vim自带的buffer方式也不错。

[参考：Vim 多文件编辑：缓冲区](https://harttle.land/2015/11/17/vim-buffer.html)

注意：默认来讲，如果你修改了文件但还没保存，是不能切换buffer的。但是这样会很不方便，不像切换tab一样。我们可以在vimrc中设置来取消这个限制：
```vim
set hidden
```
但是要知道，没有保存的话，是不能关闭buffer的。

怎样开启buffer？
实际上，buffer一直在开启着。这是你每次用`:e file`切换文件，或者在Nerdtree上按`o`打开文件，都是把当前的画面切换成了新文件你没有注意到而已。
实际上背后的buffer一直都在，你只要打开过一次的，都可以切换回去。

其实在没有安装`vim-airline`状态栏之前是没有注意到的，但是airline好心的有功能在最上方显示buffer，才让我觉得其实buffer有时候可能会比tab标签更好用。

## 常用命令
```vim
" List Buffers 查看当前所有的buffer 
:ls b

" Buffer Next 下一个buffer
:bn

" Buffer Previous 上一个buffer
:bp

" Buffer Down 关闭当前buffer
:bd

" Buffer number 指定第二个buffer
:b 2


```

## 快捷键设计
如果要保证buffer的切换像tab一样方便，肯定是要设置快捷键的，要不然总输入命令太慢了。
```vim
"按Ctrl+h 向左移动一个buffer
nnoremap <C-h> :bp<CR>
"按Ctrl+l 向右移动一个buffer
nnoremap <C-l> :bn<CR>
"按Ctrl+^ 关闭当前buffer
nnoremap <C-^> :bd<CR>
```
