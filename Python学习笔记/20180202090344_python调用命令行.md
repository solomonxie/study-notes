# python调用命令行
参考[这篇文章](https://www.jianshu.com/p/5d999a668e79)

```python
import os

#只返回结果
os.system(command)

#或者，返回结果与终端显示信息
with os.popen(command, mode) as f: 
    print(f.read())

```
