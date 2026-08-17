# ❖ 深究cp拷贝文件夹时“／”的用法

假设现有一个source文件夹:
```
source
    sub
        a.jpg
    b.jpg
    c.jpg
```


### 目标文件夹「不存在」的情况

```sh
$ cp -r source target
$ cp -r source/ target
$ cp -r source/ target/

▲ 结果：「source = target」以上三句话一样，都是创建一个source的同级克隆，只不过名字不同：
target
    ......
source
    ......

$ cp -r source/* target
▲ 结果：「命令错误」
```

### 目标文件夹「已存在」且为空

```sh
$ cp  -r source target

▲ 结果：「source ≠ target」无论是否有内容，都在target目录下存放source目录：
source
    ......
target
    source
        ......

$ cp  -r source/ target
$ cp  -r source/ target/
$ cp -r source/* target
$ cp  -r source/* target/
▲ 结果：「source = target」以上几句话一样，会正确的把source下的内容拷贝到target下
target
    ......
source
    ......
```

### 目标文件夹「已存在」且不为空，且无同名文件

```sh
$ cp  -r source target
$ cp  -r source target/

▲ 结果：「source ≠ target」无论是否有内容，都在target目录下存放source目录：
source
    ......
target
    source
        ......

$ cp  -r source/ target
$ cp  -r source/ target/
$ cp  -r source/* target
$ cp  -r source/* target/
▲ 结果：「target ∋ source」会把source下的内容全部拷贝到targe之中
source
    ......
target
    ......
    ......
```

### 目标文件夹「已存在」且有冲突文件

```sh
▲结果：「默认覆盖有冲突的目标文件」无论怎么拷贝都默认覆盖
```


