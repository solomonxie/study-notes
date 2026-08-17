# Vim脚本中的动态交互

参考：https://stackoverflow.com/questions/10386363/combine-options-in-inputdialog


## Inputbox 弹出选择框

```vim
nnoremap gb :call JumpToBuffer()<CR>
function! JumpToBuffer()
    let my_grouped_opts = input ( "1.- Search one\n2.- Search two\n3.- Search three\n" )
    let my_list_opts = split( my_grouped_opts, '.\zs' )
    for opt in my_list_opts
        echo "\nOption number " opt " selected"
    endfor
endfunction
```


