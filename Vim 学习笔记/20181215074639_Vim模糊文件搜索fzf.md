# Vim模糊文件搜索fzf

不同于`Command-T`只能用于VIM，大名鼎鼎的`fzf`是命令行工具，而且只在VIM中使用的话也不需要手动去编译任何依赖，直接用插件管理器安装即可立马使用，通用于VIM和NeoVIM。

[参考官网Github：junegunn/fzf.vim](https://github.com/junegunn/fzf.vim)

[参考：Fuzzy finder(fzf+vim) 使用全指南](https://zhuanlan.zhihu.com/p/41859976)

安装：
直接在vim-plug插件管理器中：
```
Plug 'junegunn/fzf', { 'dir': '~/.fzf', 'do': './install --all' }
Plug 'junegunn/fzf.vim'
```

> 其中, `'dir': '~/.fzf'`会把命令行软件`fzf`安装到本机的`~/.fzf`目录中，然后在shell中就可以直接通过执行`~/.fzf/bin/fzf`来使用fzf命令搜索文件了。


## 使用

最简单的话，直接在VIM中输入命令`:Files`就会弹出当前目录下的所有文件列表，然后可以各种模糊搜索，按`Ctrl+p`和`Ctrl+n`上下选择。

如果为了方便，可以将`:Files`命令映射为自己喜欢的快捷键。

[参考所有内置搜索命令：junegunn/fzf.vim - Commands](https://github.com/junegunn/fzf.vim)
