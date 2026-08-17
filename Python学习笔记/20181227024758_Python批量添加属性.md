# Python批量添加属性

有时候需要从JSON文件中导入很多数据，对应到某个class中的一些属性上。但是一个一个写很麻烦，所以研究了下Pythonic式的批量添加属性方法。


`setattr`方法：
```py
class A:
    d = '444'
    e = '555'

jsondata = {'a':'111', 'b':'222', 'c':'333'}
obj = A()
for k,v in jsondata:
    setattr( obj, k,v)
```
这种方法是利用了python内置函数`setattr`。如果不仅想给instance赋值，而是给整个类赋值(动态数据不太应该给类赋值)，那么就在class中定义相关的方法即可。


