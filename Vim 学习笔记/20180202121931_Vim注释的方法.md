# Vim注释的方法

> Vim里面注释对初学者真是比较头疼的事情。需要先$跳到行头，i插入模式，输入注释，Esc退出插入模式。如果批量就更麻烦。下面是几种常用方法。

1. 原生方法一
> `Ctrl+v`进入Block选择，向下移动选择待注释行，`Shift+i`批量插入，输入注释符，按两次Esc退出，等几秒实现批量注释。

2. `.vimrc`配置文件法
在`.vimrc`中加入如下语句：
```
" Commenting blocks of code.
autocmd FileType c,cpp,java,scala let b:comment_leader = '// '
autocmd FileType sh,ruby,python   let b:comment_leader = '# '
autocmd FileType conf,fstab       let b:comment_leader = '# '
autocmd FileType tex              let b:comment_leader = '% '
autocmd FileType mail             let b:comment_leader = '> '
autocmd FileType vim              let b:comment_leader = '" '
noremap <silent> ,cc :<C-B>silent <C-E>s/^/<C-R>=escape(b:comment_leader,'\/')<CR>/<CR>:nohlsearch<CR>
noremap <silent> ,cu :<C-B>silent <C-E>s/^\V<C-R>=escape(b:comment_leader,'\/')<CR>//e<CR>:nohlsearch<CR>
```
然后注释的快捷键是`,cc`，取消注释是`,cu`。

3. 插件法
常用插件有NerdCommenter，在`vimrc`的插件位置中加入`Plugin 'scrooloose/nerdcommenter'`，重新打开vim后输入`:PluginInstall`后安装成功。
注释的快捷键是`\cc`，反注释是`\cu`。其实和自己直接在vimrc中写没什么太大区别。
其它注释插件大同小异，就不都说了。
