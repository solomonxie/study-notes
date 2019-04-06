# VIM 同时显示「绝对行号」和「相对行号」

由于是原生功能，所以无需任何插件即可完成。

```vim
" <Line Number>
" turn hybrid line numbers on
set number relativenumber
set nu rnu
" Automatic toggling between line number modes
augroup numbertoggle
  autocmd!
  autocmd BufEnter,FocusGained,InsertLeave * set relativenumber
  autocmd BufLeave,FocusLost,InsertEnter   * set norelativenumber
augroup END
```


## 相对行号的缺点

虽然`相对行号`方便我们navigation跳转，但是对于Debugging来说是个不怎么方便的功能，即使在焦点行显示绝对行号也一样。
比如我们在Debugging时候收到提示说233行出错，虽然可以`:233`跳转过去，但这是很不直观的。
而且对于所处绝对位置的那种信息来说，相对行号所提供的便利并不足够让我们去掩盖那么重要的信息。
所以用了一阵相对号后，我果断的关闭了这个功能。
