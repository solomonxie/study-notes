#  ❖ Vim 「Snipmate」 自动补全插件

在`~/.vimrc`的Vundle插件管理函数中添加以下内容(插件本身和所依赖的插件)：
```vim
    Plugin 'MarcWeber/vim-addon-mw-utils'
    Plugin 'tomtom/tlib_vim'
    Plugin 'garbas/vim-snipmate'
    Plugin 'honza/vim-snippets' "massive common snippets
```

然后在Vim中输入命令安装插件：
```
:source %
:PluginInstall
```
完成。

## 使用方法
输入状态下，直接按<Tab>，就会自动打出相关的snippets预设片段。


## 如何自定义snippets
直接在`~/.vim/snippets/`目录下添加`*.snippets`文件即可。

注意以下几点：
- `~/.vim/snippets/`目录是位于所有插件之外的，所以不会因插件更新而被删除。
- 如果你也安装了`vim-snippets`，那么在trigger同名的时候，vim会在状态栏弹出选项让你选择使用哪个snippets。

比如针对所有python文件，那就在`~/.vim/snippets/`目录下创建一个`python.snippets`文件，内容格式如下：
```vim
snippet #!
    #!/usr/bin/env python
    # -*- coding: utf-8 -*-
```
以上片段，只要你在python文件中输入`#!`并按下<Tab>，就会自动输出定义的那段内容。


