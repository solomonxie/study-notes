# VIM Navigation (Advanced) [DRAFT]

## Method Jump (Python)

[Refer to Stackoverflow: More efficient movements editing python files in vim](https://stackoverflow.com/questions/896145/more-efficient-movements-editing-python-files-in-vim)
[Refer to `$VIMRUNTIME/ftplugin/python.vim`](https://github.com/vim/vim/blob/master/runtime/ftplugin/python.vim)

```vim
]] Jump forward to begin of next toplevel
[[ Jump backwards to begin of current toplevel (if already there, previous toplevel)
]m Jump forward to begin of next method/scope
[m Jump backwords to begin of previous method/scope

][ Jump forward to end of current toplevel
[] Jump backward to end of previous of toplevel
]M Jump forward to end of current method/scope
[M Jump backward to end of previous method/scope
```
