#  ❖ VIM式的查找与替换

一般要说VIM里面怎么查找替换，肯定会得到一堆`:%s /x/x/g`这样的说法。
我只能说：这是`不够vim`的，甚至`Anti-intuitive`反直觉的。

带提示的查找替换：
```vim
:% s/old/new/gc
```

我们可以映射为一个键：
```vim
noremap <leader>ra y:% s/<C-r>0/<C-r>0/gc<Left><Left><Left>
```

但是，这还不够。怎么才能达到Sublime那种直观的多选并替换的效果呢？
直白点说，没有！所有VIM中模拟`Multi-select`的插件都不够好，因为VIM原生就不支持这种操作。VIM有自己的操作。

说一个更VIM的方案：
```
/old<CR>cwnew<ESC>n.n.n.n.n.
```
其实这个操作是最直观也最自由的：
- `/old`按回车，进入查找old的模式
- `cw`删除这个词，并输入新词new
- 按`n`选中下个搜索结构，
- 按`.`自动重复上一步的`替换`操作。
