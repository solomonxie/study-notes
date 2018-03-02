# python将某个目录打包为`zip`文件
比较古老的方法是用`zipfile`库创建zip包，但是要写各种循环迭代需要很多行代码。
还有另一种[python自带库`shutil`](http://python.usyiyi.cn/translate/python_278/library/shutil.html),可以一句话打包为zip文件。
```
import shutil
shutil.make_archive(base_name, format, root_dir, base_dir)
```
很快就打包好了！
唯一注意的是，怎样把它安装自己想象的结构打包。
- base_name，是加上完整路径（不能缩写）的文件或文件夹名
- format一般是zip，其它tar之类也行
- root_dir是要压缩的目录或文件
- base_dir是压缩包里的文件层级。如你写`a/b/c`，这样所有文件都会塞到最底层的c文件夹中。

