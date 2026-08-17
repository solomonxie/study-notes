#  ❖ Vim根据文件类型设置不同的快捷键 [DRAFT]

在vim中，

查看当前的文件类型：
```
:echo &filetype
```

一般会是：c, cpp, python等，记住这些名字。
然后在`~/.vimrc`中设置：
```vim
" C Compiler:
autocmd FileType c nnoremap <buffer> <C-i> :!gcc % && ./a.out <CR>

" C++ Compiler
autocmd FileType cpp nnoremap <buffer> <C-i> :!g++ % && ./a.out <CR>

" Python Interpreter
autocmd FileType python nnoremap <buffer> <C-i> :!python % <CR>
```

这样就能完成，针对不同的文件，用相同的快捷键`Ctrl+i`。

一般这样方便不同文件的编译和执行。
