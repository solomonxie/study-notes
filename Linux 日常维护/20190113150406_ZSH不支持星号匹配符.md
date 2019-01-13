# ZSH不支持`*`星号匹配符

Bash中，我们经常会用这些语句：
```sh
find . -name *.txt

apt-get remove mysql*

rm /tmp/*.jpg
```

然后在zsh中，经常会无法解析`*`通配符，产生这个错误：
```
zsh: no matches found
```

解决方法很简单，在`~/.zshrc`中加入`setopt no_nomatch`即可。
