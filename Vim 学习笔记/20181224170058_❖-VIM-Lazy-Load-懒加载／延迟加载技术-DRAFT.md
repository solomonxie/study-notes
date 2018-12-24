#  ❖ VIM Lazy Load 懒加载／延迟加载技术 [DRAFT]

很多重量级插件在启动时是非常耗时的，动不动400ms以上，比如YCM，效果很明显。但是我们实际上没必要一开始就加载所有的插件，而是有些文件才用得上，或者Insert模式才用得上。
所以，我们可以按需加载，这样就省了很多时间。

[参考：延迟加载ycm以加快vim的启动速度](https://blog.csdn.net/tenghui0425/article/details/70201929)

配合`vim-plug`插件管理器的`On`功能（On-Demand），和`autocmd`命令，我们可以简单做到这点：
```vim
" 插件定义处：
Plug 'Valloric/YouCompleteMe', { 'on': [] }

" 配置：
augroup load_ycm
    autocmd!
    autocmd InsertEnter * call plug#load('YouCompleteMe') | autocmd! load_ycm
augroup END
```


如果在Plug后面加上了`on`或`for`选项，那么意味着启动时候这个插件会禁止加载。而加载的时间，需要我们后面手动指定一个autocmd自动命令或命令组来实现。
而手动加载插件的命令为：`call plug#load('插件名')`

具体on和for的用法，
[参考官网：on-demand-loading-of-plugins](https://github.com/junegunn/vim-plug#on-demand-loading-of-plugins)
