# ❖ Python深拷贝、浅拷贝

Python中有三种拷贝：
- `=`：完全不拷贝，指针指向同一块内存数据
- `copy.copy()`：浅拷贝，为新变量开创内存空间，但是如果变量里面有子变量，则子变量只是指向原先对应的内存空间。
- `copy.deepcopy()`：深拷贝，为新变量重新开创内存空间，变量里面如果有子变量也全都重新开内存来存储。

拷贝让人混淆的，一般有这几种情况：
- 变量有子变量的情况，如`v = [ [1,2], [3,4] ]`, 甚至`v = [ [[1,2], [3,4]], [[5,6], [7,8]] ]`
- 向列表或字典插入元素的情况，如`v.append(123)`且时候，v的复制品是否也会变化？
- 向列表或字典的子变量插入元素时候，复制品是否也会变化？


当变量有子变量的情况下：
```py
import copy

original = [ [1,2], [3,4] ]

reference  = original
shallow = copy.copy(original) 
deep = copy.deepcopy(original) 

# -----RESULTS ------
# Reference >>> id(reference) == id(original)
# Shallow copy >>> id(shallow) != id(original)
# Deep copy >>> id(deep) != id(original)
#         but >>> id(deep[0]) == id(original[0])
```


向列表插入元素的情况下：
```py
import copy

original = [ [1,2], [3,4] ]
reference  = original
shallow = copy.copy(original) 
deep = copy.deepcopy(original) 

original.append( [5,6] )

# -----RESULTS ------
# Original >>> original == [ [1,2], [3,4], [5,6] ]
# Reference >>> reference == [ [1,2], [3,4], [5,6] ]
# Shallow copy >>> shallow == [ [1,2], [3,4] ]
# Deep copy >>> deep == [ [1,2], [3,4] ]
```

为什么浅拷贝没有变化呢？
因为浅拷贝，只是拷贝了原变量的子变量的`引用`，也就是说，原变量增加的一个子变量，不会使浅拷贝增加一个引用。
在浅拷贝后，实际上新变量shallow中存储的内容如下：
```py
shallow == [ address_of_[1,2], address_of_[3,4] ]
```
也就是说这里的逻辑关系是：只有当之前的子变量`[1,2]`和`[3,4]`发生变动时，变量shallow才会变化。
但是原变量original本身的扩充变化，完全和它无关了。


使用列表和字典自带的`.copy()`方法：
list和dict所自带的`.copy()`方法，实际上是`浅拷贝`。即如果`new = original.copy()`，那么这个new变量是浅拷贝出来的。
