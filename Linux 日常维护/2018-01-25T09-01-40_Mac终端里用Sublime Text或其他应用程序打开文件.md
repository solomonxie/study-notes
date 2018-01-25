# Mac终端里用Sublime Text或其他应用程序打开文件

Mac下的Sublime Text的位置是`/Applications/Sublime\ Text.app/Contents/SharedSupport/bin/subl`
所以我们直接用alias别名引用它就好了。
Bash的话在`~/.bash_profile`里，zsh的话在`~/.zshrc`里，直接加入这句话：
```
alias subl="/Applications/Sublime\ Text.app/Contents/SharedSupport/bin/subl"
```
然后就可以直接命令行里打开编辑器了：
```
subl ~/readme.txt
```
执行后会弹出Sublime Text编辑器，并打开readme.txt文件。

**同理，换成其它编辑器，或在其它系统里，也是这样修改流程**

