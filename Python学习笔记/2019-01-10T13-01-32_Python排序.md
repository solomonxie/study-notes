# Python排序


## 自定义对象的排序

假设我有一个列表的自定义对象：`people = [<Person age=24>, <Person age=45>, <Person age=33> ...]`
如何针对每个`<Person>`对象的`age`属性排序呢？

Python内置的`sorted()`方法：
```py
>>> newlist = sorted(people, key=lambda o: o.age, reverse=True)
>>> newlist
[<Person age=24>, <Person age=33>, <Person age=45>, ...]
```
