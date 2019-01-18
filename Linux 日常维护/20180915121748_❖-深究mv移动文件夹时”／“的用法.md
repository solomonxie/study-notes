# ❖ 深究mv移动文件夹时”／“的用法

### 目标文件夹「不存在」的情况

```sh
$ mv source target

▲结果：把source文件夹「更名」为target
```

### 目标文件夹「已存在」且为空

```sh
$ mv source/ target
$ mv source/ target/
$ mv source target/
$ mv source/ target/
▲结果：将source移动到target下，成为子文件夹
target
    source
        ......

$ mv source/* target
$ mv source/* target/

▲结果：将source的所有内容移动到target下
source
target
        ......

```


### 目标文件夹「已存在」且有冲突文件
这就比较复杂了。
如果有冲突文件，则会不询问直接覆盖。
如果有冲突文件夹，则会把文件先全都移动过去，对于有冲突的文件夹，则无论如何都无法移动或覆盖。这时候要用`cp -r`命令先复制，在`rm -r`命令删除源文件夹。
