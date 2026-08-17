# ❖ Python函数式编程 [DRAFT]

> 简而言之，Python函数式编程就是`一行代码的函数`。

Python中所谓的函数式编程，其实不是把OOP都扔掉，而只是指运用一些方便的“小函数”而已。
这些方便的小函数包括：
- `lambda`
- `Map`
- `Reduce`
- `Filter`

[参考：Python Tips - Map, Filter and Reduce](http://book.pythontips.com/en/latest/map_filter.html)

## lambda

Python关键字`lambda`是函数式编程的基础：`lambda`能生成一行代码的函数。


## Map


## Reduce


## Filter

```py
>>> number_list = range(-5, 5)
>>> less_than_zero = list(filter(lambda x: x < 0, number_list))
>>> print(less_than_zero)
[-5, -4, -3, -2, -1]
```
