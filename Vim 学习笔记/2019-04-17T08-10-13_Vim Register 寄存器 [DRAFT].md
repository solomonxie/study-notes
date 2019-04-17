# Vim Register 寄存器 [DRAFT]

Vim用好Register，会有很大的帮助。


## 常用的特殊寄存器 Special Registers

以下为常用Registers:
- 系统剪切板：`+`
- Vim Yank 板： `"` (双引号)


## 自由设置寄存器 Set Register

Refer to: https://stackoverflow.com/a/1502258/9172013

```vim
let @a = 'hello, world!'

let @a = getreg('"')

:let @a=@b

:let @a=@"
```


## 在脚本中使用Register

```vim
:let @1 = 'world!'
:echo "hello, " @1
hello, world!
```
