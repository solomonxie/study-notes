# NeoVim 报错`nvim E117: Unknown function: plug#begin`

这是因为我们都忽略了一个事实：nvim的目录`~/.config/nvim/`下不光是要有一个`init.vim`配置，还需要和`~/.vim/`一样的完整目录，包括`autoload/`这个加载插件管理器用的目录。

所以，最简单的方法就是直接创建软链接：
```sh
$ mv ~/.config/nvim ~/.config/nvim-old
$ ln -s ~/.vim/ ~/.config/nvim/
```
