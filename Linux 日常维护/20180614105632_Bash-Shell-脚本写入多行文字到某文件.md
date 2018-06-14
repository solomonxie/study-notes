# Bash Shell 脚本写入多行文字到某文件

主要语法是`cat>文件名<<EOF`，然后把多行文字放在下面，并以`EOF`结束。

示例` test.sh`：
```sh
cat>~/text.txt<<EOF
第一行文字
第二行文字
第三行文字
EOF
```

如果需要追加文本，那就变成`cat>>`：
```sh
cat>>~/text.txt<<EOF
第一行文字
第二行文字
第三行文字
EOF
```

执行bash脚本:
```sh
$ bash test.sh

# 查看生成到脚本
$ cat ~/text.txt
```
