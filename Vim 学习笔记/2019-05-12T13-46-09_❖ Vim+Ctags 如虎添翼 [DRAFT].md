# ❖ Vim+Ctags 如虎添翼 [DRAFT]

代码库中利用ctags最主要的就是函数定义的跳转了，更明确的说：是跨文件的函数定义跳转。



## 理解Ctags


### Ctags的几个实现


## Python的tags跳转

Python中的函数如果是import进来的，那么当你尝试用ctags进行跳转时，你没法跳转到另一个文件的定义出，而只是跳转到代码最上面的import地方。

解决方案就是在生成ctags的时候添加一个参数：`--python-kinds=-i`

在Vim中，无论是使用`gutentags`插件还是别的ctags管理插件，都允许在`vimrc`中添加自定义的ctags生成参数，如：
```vim
let g:gutentags_ctags_extra_args += ['--python-kinds=-i']
```

这样，当下次打开项目后自动生成ctags时，就能正常的跨文件跳转了。
