# 对象排序的诀窍：operator & sorted

多维列表：
```py
a = []
a.append(["Nick", 30, "Doctor"])
a.append(["John",  8, "Student"])
a.append(["Paul", 22, "Car Dealer"])
a.append(["Mark", 66, "Retired"])

# Access
print(b[0][1])
```

列表中各项为字典：
```py
b = []
b.append({'name':'nick', 'age':30})
b.append({'name':'John', 'age':8})
b.append({'name':'Paul', 'age':22})
b.append({'name':'Mark', 'age':66})

# Access
print(b[0]['age'])
```

列表中各项为对象：
```py
class User:
    def __init__(self, name, age, job):
        self.name = name
        self.age = age
        self.job = job

c = []
c.append(User("Nick", 30, "Doctor"))
c.append(User("John",  8, "Student"))
c.append(User("Paul", 22, "Car Dealer"))
c.append(User("Mark", 66, "Retired"))

# Access
print(b[0].age)
```


怎么对这些特殊列表排序？


首先要确定，这个案例中我们要针对`age`排序，这只能对它排序。那么如何访问每种列表的元素的`age`呢？
```py
>>> a[0][1], b[0]['age'], c[0].age
30, 30, 30
```

要对这各种列表排序很简单，只要利用内置函数`sorted()`的`key`参数即可：
```py
>>> sorted(a, key=lambda x: x[1])
[['John', 8, 'Student'],
 ['Paul', 22, 'Car Dealer'],
 ['Nick', 30, 'Doctor'],
 ['Mark', 66, 'Retired']]

>>> sorted(b, key=lambda x: x['age'])
[{'name': 'John', 'age': 8},
 {'name': 'Paul', 'age': 22},
 {'name': 'nick', 'age': 30},
 {'name': 'Mark', 'age': 66}]

>>> sorted(c, key=lambda x: x.age)
[<__main__.User at 0x10c2c12b0>,
 <__main__.User at 0x10c2c1f28>,
 <__main__.User at 0x10c2c1278>,
 <__main__.User at 0x10c2c1e80>]
```

但是，如果我们想要这些`age`的名字、位置动态变化怎么办？
那就要利用到Python的内置工具`operator`来动态获取了，非常方便：
```py
>>> import operator
>>> operator.itemgetter(1)( a[0] )  # 获取列表项
30
>>> operator.itemgetter('age')( b[0] )  # 获取字典项
30
>>> operator.attrgetter('age')( c[0] )  # 获取自定义对象属性
30
```

其中，`operator.itemgetter(..)`返回的不是一个值，而是一个`callable`，也就是一个特殊的函数。它让你可以这样做：
```py
>>> func = operator.attrgetter('age')
>>> func(obj)
30
```

理解了`operator`的用法，我们就可以改变上面"hard coded"写法来重新写`sorted()`了：
```py
>>> sorted(a, key=lambda x: operator.itemgetter(1)(x))
>>> sorted(b, key=lambda x: operator.itemgetter('age')(x))
>>> sorted(c, key=lambda x: operator.attrgetter('age')(x))
```
以上排序出来的结果是和前面完全一样的。



## Sort List of Objects with Multiple Keys

Refer to: https://gist.github.com/malero/418204

Improved a bit:

```py
from functools import cmp_to_key
import operator

def cmp(a, b): return (a > b) - (a < b)

def multikeysort(items, columns, functions={}, getter=operator.itemgetter):
    comparers = []
    for col in columns:
        column = col[1:] if col.startswith('-') else col
        if column not in functions:
            functions[column] = getter(column)
        comparers.append((functions[column], 1 if column == col else -1))

    def comparer(left, right):
        for func, polarity in comparers:
            result = cmp(func(left), func(right))
            if result:
                return polarity * result
        else:
            return 0
    return sorted(items, key=cmp_to_key(comparer))


myList = [{'name': 'nick', 'age': 30}, {'name': 'John', 'age': 8},
        {'name': 'Mark', 'age': 66}, {'name': 'Paul', 'age': 22}]

expected = [{'name': 'John', 'age': 8}, {'name': 'Paul', 'age': 22},
            {'name': 'nick', 'age': 30}, {'name': 'Mark', 'age': 66}]

assert multikeysort(myList, ['age']) == expected
print('ok.')
```
