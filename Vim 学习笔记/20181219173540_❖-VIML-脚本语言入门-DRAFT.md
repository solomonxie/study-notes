#  ❖ VIML 脚本语言入门 [DRAFT]

[参考：Learn Vimscript the Hard Way](http://learnvimscriptthehardway.stevelosh.com/)


## 变量

```vim
"设置变量
let myVariable = 1
let myString = 'Hello'
```


## 逻辑控制

[参考：Comparisons  - Learn Vimscript the Hard Way](http://learnvimscriptthehardway.stevelosh.com/chapters/22.html)

if-else:
```vim
if 3 >= 1
    echo 'True'
elseif 3 < 4
    echo 'True again'
elseif 3 == 3
    echo 'True true'
else
    echo 'False'
endif
```

VIM中的字符串和数字是可以直接比较的，如`:echo '3' >= 3`，返回1.


## Functions 函数

[参考：Functions - Learn Vimscript the Hard Way](http://learnvimscriptthehardway.stevelosh.com/chapters/23.html)

> 函数名必须大写开头。

```vim
function MyFunction()
    :wq
endfunction
```

但是如果重载当前vimrc的话，会遇到`function already exists`警告。
所以最好在将函数定义为可重写的函数，即变为`function!`：


```vim
function! MyFunction()
    :wq
endfunction
```


## 内置函数

### has(..)

- has('程序语言')
- has('硬件架构')
- has('xxx')


### system(...)

- system('rm /tmp/*')

### buffer

- bufnr('%'): 返回当前VIM中的buffer数量



## autocmd 事件触发器

参考非常棒的VIM官方文档（中文翻译）：http://vimcdoc.sourceforge.net/doc/autocmd.html

格式为：`:au[tocmd] [group] {event} {pat} [nested] {cmd}`
中文的话就是：`:au[tocmd] [组] {事件} {文件名规则} [nested] {命令}`



如果命令比较复杂的话，建议创建function，然后在autocmd中`call func()`。

## 常用技巧


## 获取当前buffer的文件名、路径、扩展名

[参考：How can I see the full path of the current file?](https://vi.stackexchange.com/questions/104/how-can-i-see-the-full-path-of-the-current-file)
[参考：How do I get the name and extension of the current file?](https://vi.stackexchange.com/questions/2429/how-do-i-get-the-name-and-extension-of-the-current-file)

都知道，VIM中`%`代表当前buffer，我们可以增加`filename-modifiers`来操作`%`得到buffer关联的文件的相关信息。

Register `%`返回当前文件的名字。所以我们才可以用`!python %`这样的命令来运行当前脚本。
VIM中，`%`还能做到很多的扩展：
```vim
:echo @%                |" directory/name of file
:echo expand('%:p')     |" full path "PATH"
:echo expand('%:p:h')   |" directory containing file "HEAD"
:echo expand('%:t')     |" full name of file "TAIL"
:echo expand('%:t:r')     |" Only name of file "ROOT"
:echo expand('%:e')     |" Only extension of file "EXTENSION"
```

我们在vimrc中使用的时候，可以省略echo和expand。比如：
`nnoremap <C-g> :!CMD %:p:h<CR>`，这样可以在按`Ctrl-g`时候，在当前文件所在的目录执行`CMD`命令

```vim
“获取路径
echo expand('%:p')    "/home/mool/vim/src/version.c

"获取文件全名
echo expand('%:t')   "version.c

"获取文件名，不包括扩展名
echo expand('%:t:r')   "version

"获取扩展名
echo expand('%:e')   "c
```

## Multiple lines 换行

以`\`开头，`|`结尾，即可连接多行为一行。
```vim
au Filetype ruby
            \ setlocal ts=2  |
            \ setlocal sts=2 |
            \ ...
```


