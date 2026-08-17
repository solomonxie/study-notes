# Python字典获取值的正确方式

假设有一个Python dict：
```py
>>> d = {'a':1, 'b':2, 'c':{'name':'jason', 'age':18} }
```

获取值的一般做法是：
```py
>>> d['a']
1

>>> d['c']['name']
jason
```

但是这种问题非常大：当我们数据是来自网络或不确定位置时，我们不确定它是不是有某些key。
这种时候就会报错且验证影响程序运行。

正确做法是：
```py
>>> d.get('a')
1

>>> d.get('asdfa')
None
```
这样的话，如果遇到不存在的值，会返回None，而不是报错。

问题又来了：How to safely get value from nested dict?

如果是这样`d.get('XXXXXXXX').get('name')`前面的key获取不到内容怎么办？这个时候第一个get返回None，后面还是会报错。

没问题，Python dict的get还可以设置default默认值！
```py
>>> d.get('XXXX', {}).get('name')
None
```

所以，如果我们要严格控制的话，最好每个都这么处理。这种地方不要图省事。
