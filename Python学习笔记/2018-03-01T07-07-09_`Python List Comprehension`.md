# `Python List Comprehension`
指的Python单行循环:
```python
a = [n for n in alist if n>0]
```

## 进阶
如果在单行循环中，想获得某个item的序号，那么就需要用到python自带的`enumerate()`函数
```python
# Python "List Comprehension" method
old = ['zero', 'one', 'two', 'three', 'four', 'five', 'six']
new = [item for index, item in enumerate(list1) if index < 4]
print new

# Output:
['one', 'two', 'three']
```
注意：使用`enumerate()`时，必须用2个变量承接它的返回值，第一个是index序号，第二个是item本身。


