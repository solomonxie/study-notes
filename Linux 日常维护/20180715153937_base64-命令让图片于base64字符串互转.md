# base64 命令让图片于base64字符串互转

base64是绝大多数linux系统自带的程序，可以轻松快速把二进制文件转换成base64字符串，或者反之转换回来。用法极其简单，如下：

```sh
# 把图片转换成base64字符串，且保存为文本文件
$ base64 test111.jpg > string.txt

# 把含有base64字符串的文本转换回图片文件
$ base64 -D string.txt -o test222.jpg
```
