# Bash的数值运算

## 整数运算

如果是bash，则：
```sh
if (( a > b )); then
    ...
fi
```

如果是POSIX shell那么可能会不支持`((...))`，那么就要用`-gt`:
```sh
if [ "$a" -gt "$b" ]; then
    ...
fi
```


## 非整数运算

Bash原生不支持浮点运算，只支持整数。如果运算中输入的数字不是整数，它会报错告诉你需要整数输入。
所以我们要用第三方工具，还好*nix都配了计算工具。


（推荐）使用bc命令，即`basic calculator`。
```sh
$ num1=3.17648E-22
$ num2=1.5
$ echo $num1'>'$num2 | bc -l
>>> 0

$echo $num2'>'$num1 | bc -l
>>> 1
```
