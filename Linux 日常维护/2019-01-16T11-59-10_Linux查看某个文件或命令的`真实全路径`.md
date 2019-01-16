# Linux查看某个文件或命令的`真实全路径`

简单的使用*nix内置命令：`realpath`

文件／文件夹／链接：
```sh
# FILE
$ realpath README.md
/home/pi/project/README.md

# SYMLINK
$ realpath ~/.vimrc
/home/pi/dotfiles/vim/vimrc-mini
```

命令：
```sh
$ which vim
vim: aliased to vim8
$ which vim8
/usr/bin/vim8

$ realpath $(which vim)
/opt/vim-8.1/bin/vim
```

我们可以看到，在查看命令的位置上，`which`是不太可靠的，因为它只会显示出`链接`或`别名`，而不显示真实地址。
