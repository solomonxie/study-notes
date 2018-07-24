# CSV读取

传统的方法如下：
```py
import csv

with open('sample.csv', 'r') as f:
    reader = csv.reader(f)
    for line in reader:
        print(line)
```

但是CSV的`reader`是**有指针的！**

也就是说，你只能读一遍，第二遍再引用`reader`的话，就**没有任何结果**！

手动读取csv的方法：
```py
with open('sample.csv', 'r') as f:
    csv_reader = [ n.split(',') for n in f.read().split('\n') ]
    for line in csv_reader:
        print(line)
```

然后发现自己解析出来的`csv_reader`也和csv读出来的是一样的列表，没什么太大区别，而且很好用。
不过缺点应该是这种方法的效率可能不够高，读取大文件的话对内存压力会很大。



