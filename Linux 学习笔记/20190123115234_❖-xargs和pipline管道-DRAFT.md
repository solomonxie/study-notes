# ❖ xargs和pipline管道 [DRAFT]

## pipline管道


## xargs

经常配合`find`使用，find根本不支持pipline `|`，太不方便了。

xargs做到的是，把`|`前面传过来的stdin信息，分拆成一系列的args，然后再把这些args组成参数传给下一个命令。这样就解决了很多pipline管道做不到的事情了，因为管道不能传参数。

常用操作参考：
```sh
# 查找文本文件，并显示每个文件的行树
$ find . -name "*.txt" | xargs wc -l

# 顺便再排个序
$ find . -name "*.txt" | xargs wc -l | sort

# 把参数传给指定的命令
$ echo '--help' | xargs cat 
>>> cat --help
```

注意：xargs不同的版本会不兼容。Mac上默认版本非常低所以不兼容，需要更新Mac的gnu utils等。

### 参数分割 -d选项

-d 即delimiter，分隔符。

`xargs`既然是处理args的命令，自然少不了args分割。比如"--abc,--bcd,--def"，我们可以把用`,`把字符串分割为三个参数，一起传给下一个命令：
```sh
$ echo "-abc,-bcd,-def" | xargs -d "," echo
>>> echo --abc --bcd --def
```

### 命令打印 -p选项

-p 即print。

xargs可以把组合成功的整个命令打印出来，然后交互让你选择是否执行：
```sh
$ echo "--help" | xargs -p cat
>>> cat --help ?...
```

### 参数组合 -n选项

xargs可以把拆分后的多个参数，分组传递给下个命令，比如`--restart always --name ubuntu`，我们可以把他们用空格分开，然后两个一组传给下个命令：
```sh
$ cat "--restart always --name ubuntu" | xargs -n 2 echo
>>> echo --restart always --name ubuntu
```


### 参数截取 -E选项 
-E 同--eof-str 即End Of File - String.

xargs可以根据一定的条件在多个参数里面搜索，如果搜索到了这个词，就把这个词及以后的全删掉，只保留其之前的。

> 注意：-E只有在xargs不指定-d的时候有效，如果指定了-d则不起作用，而不管-d指定的是什么字符，空格也不行。

```sh
$ echo '11@22@33@44@55' | xargs -E '33'   echo 
>>> 11 22
```
