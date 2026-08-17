# Homebrew 备份所有brew安装过的程序

为什么需要备份？
- 重装系统
- 因为卸载了Homebrew而丢掉了所有程序

新版Homebrew已经可以很方便的备份所有用Homebrew安装过的程序了。
需要用到`Homebrew/homebrew-bundle`这个程序。

[参考：`Homebrew/homebrew-bundle`](https://github.com/Homebrew/homebrew-bundle)
[参考：Restore, Clone or Backup your Homebrew Setup](https://tomlankhorst.nl/brew-bundle-restore-backup/)

备份：
```sh
# 先安装
brew bundle dump

# 再运行一遍执行
brew bundle dump
```

这时候，会在当前目录生产一个`Brewfile`的文件，记录了所有已安装的程序。

大概内容如下：
```
tap "homebrew/bundle"
tap "homebrew/core", "https://github.com/Homebrew/homebrew-core.git"
brew "autojump"
brew "axel"
brew "ctags"
brew "git"
brew "neovim", link: false
brew "pngpaste"
brew "python"
brew "python@2"
brew "ranger"
brew "reattach-to-user-namespace"
brew "tmux"
brew "w3m"
```

把它保存在自己备份文件的地方。

恢复安装的时候，只需要进入`Brewfile`所在文件夹，执行：
```sh
$ brew bundle
```
