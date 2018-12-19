# VIM动态预览Markdown文章

推荐`JamshedVesuna/vim-markdown-preview`这个插件，依赖非常少，也不需要服务器等，最简单的实现动态预览功能。

依赖请参考： 
https://github.com/JamshedVesuna/vim-markdown-preview#requirements
主要依赖的只是Markdown转HTML的渲染引擎。

二选一：
- daringfireball-Markdown ,或
- (推荐) `joeyespo/grip`，需在vimrc中加入`let vim_markdown_preview_github=1`
    - `pip install grip --user`，或
    - `brew install grip` 不知道为什么只有这个好用

其中`grip`是推荐的引擎，可以在shell命令行中独立使用。功能就是渲染当前文件夹中的所有markdown文件并建立localhost服务器承载html网页。然而显然`JamshedVesuna/vim-markdown-preview`并没有使用它的服务器而只是用它渲染为本地html页面。

在命令行里输入`grip`即可立刻弹出网页，看到效果。



然后只要在VIM插件管理器如vim-plug中加入：
```vim
Plug 'JamshedVesuna/vim-markdown-preview`
```
然后`:PlugInstall`安装即可。

VIM中随便进入一个Markdown文档，按`Ctrl+p`即可弹出浏览器动态预览文档。
修改时，需要保存才能自动渲染。


## 目前问题
自动渲染不生效，保存文档后，还需要再按`Ctrl+p`才能更新预览。和官方介绍不同，不知道是哪里出了问题。

