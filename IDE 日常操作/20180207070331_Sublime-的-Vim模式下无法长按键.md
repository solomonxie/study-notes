# Sublime 的 Vim模式下无法长按键
vim上下移动，经常要长按某一个键，但是Sublime默认不支持vim下的长按，按多久也只生效一次。
解决很简单，
1. 必须先关闭Sublime
2. 在系统终端里输入修改Sublime的代码：
```
# Sublime 3的话是这个
defaults write com.sublimetext.3 ApplePressAndHoldEnabled -bool false

# Sublime 2的话是这个
defaults write com.sublimetext.2 ApplePressAndHoldEnabled -bool false
```

参考这个系统设置的其它设置，看[这篇文章](https://zhuanlan.zhihu.com/p/20234659)。
