# Mac Homebrew 更换中国源

Homebrew安装主要靠git仓库，切换源实际上就是切换相关git repo的remote url.

具体做法：
- 找到`brew.git`和`homebrew-core.git`的本地repo
- 切换两个repo的remote url

切换USTC源：https://lug.ustc.edu.cn/wiki/mirrors/help/brew.git
```sh
# 更换brew.git的源
cd "$(brew --repo)"
git remote set-url origin https://mirrors.ustc.edu.cn/brew.git
# 更换homebrew-core.git的源
cd "$(brew --repo)/Library/Taps/homebrew/homebrew-core"
git remote set-url origin https://mirrors.ustc.edu.cn/homebrew-core.git

brew update
```
另外，还需要更换`Homebrew Bottle`源，这个只要在shell配置文件里加上（或更改）一个变量即可。
如zsh就是编辑`~/.zshrc`文件, bash就是`~/.bash_profile`文件：
```sh
export HOMEBREW_BOTTLE_DOMAIN=https://mirrors.ustc.edu.cn/homebrew-bottles
```


切换清华源：https://mirror.tuna.tsinghua.edu.cn/help/homebrew/
```sh
cd "$(brew --repo)"
git remote set-url origin https://mirrors.tuna.tsinghua.edu.cn/git/homebrew/brew.git
cd "$(brew --repo)/Library/Taps/homebrew/homebrew-core"
git remote set-url origin https://mirrors.tuna.tsinghua.edu.cn/git/homebrew/homebrew-core.git
cd "$(brew --repo)/Library/Taps/homebrew/homebrew-science"
git remote set-url origin https://mirrors.tuna.tsinghua.edu.cn/git/homebrew/homebrew-science.git
cd "$(brew --repo)/Library/Taps/homebrew/homebrew-python"
git remote set-url origin https://mirrors.tuna.tsinghua.edu.cn/git/homebrew/homebrew-python.git

brew update
```

重置官方源：
```sh
# 重置brew.git:
cd "$(brew --repo)"
git remote set-url origin https://github.com/Homebrew/brew.git

# 重置homebrew-core.git:
cd "$(brew --repo)/Library/Taps/homebrew/homebrew-core"
git remote set-url origin https://github.com/Homebrew/homebrew-core.git
```


