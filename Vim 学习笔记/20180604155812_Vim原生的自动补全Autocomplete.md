# Vim原生的自动补全Autocomplete

在Insert编辑模式时，输入某个词，然后：
- 按`Ctrl+x`再按`Ctrl+l`，就会显示出一个提示列表。
- 按`Ctrl+n`或`Ctrl+p`上下选择。

当然，这样按键太麻烦，我们要做键盘映射了：
```vim
" 按Ctrl+d显示自动补全
inoremap <C-d> <C-x><C-l>
```
