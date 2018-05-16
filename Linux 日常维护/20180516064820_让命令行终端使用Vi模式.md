# 让命令行终端使用Vi模式
> 命令行里输入长命令时，真是个pain。不能跳词，不能用鼠标，只能按左右键一个字母一个字母移动，实在是挺费劲的。

[参考文章。](https://dougblack.io/words/zsh-vi-mode.html)

实际上非常非常简单，完全无需额外下载什么插件，都是内置功能。
如果Bash终端的话，只要在`~/.bash_profile`或`~/.bashrc`中加入这个命令：
```vim
set -o vi
```

如果是Zsh，则在`~/.zshrc`中加入：
```vim
bindkey -v
export KEYTIMEOUT=1
```

[参考视频：TFW You Learn There's a Vim Mode in Bash...](https://www.youtube.com/watch?v=GqoJQft5R2E)

具体使用：

我使用的iTerm2+Zsh终端，已经进入了vi模式。但是屏幕上没有任何显示当前是`Normal`模式还是`Insert`模式。所以经常不知道自己在什么模式，还是有点不习惯。
使用上，完全和vi相同。

