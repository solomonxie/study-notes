# ❖ Python OOP 面向对象编程

[参考：黑马程序员教程 - Python基础 面向对象](http://yun.itheima.com/course/273.html)

OOP三大特性，且三个特性是有顺序的：
- 封装
- 继承
- 多态


## 封装
指的就是把现实世界的事务，封装、抽象成编程里的对象，包括各种属性和方法。
这个一般都很简单，不需要多讲。

> 唯一要注意的就是：推荐从小往大开始封装、开发类。比如`手枪，子弹`这两个类，我们需要先定义和开发子弹的所有属性和方法，然后再去开发上一层的手枪。这样的话会很方便。反过来开发手枪的适合，发现写到一半写不下去要到子弹那里写，就很乱了。

## 继承
子类可以继承父类和父父类的所有属性、方法。

继承格式：
```py
class Parent:
    def func1(self):
        pass

class Son(Parent):
    def func2(self):
        func1()
```

方法改写：
子类在不满意时，也可以进行自己的改写父类的属性、方法。
其中有两种情况：
- Overwrite 覆盖重写父类方法：只需要写一个同名函数即可覆盖。
- Extend 扩展父类函数：
    - 第一种方式(主要）：写一个同名函数，并在其中通过`super().func()`引用父类方法。其中`super`是一个python builtin 特殊类，而`super()`即生成一个super的实例。在子类中生成super实例，会得到父类的引用。
    - 第二种方式（python 2.x以前使用）：写一个同名函数，再通过`ParentName.func(self)`引用父类方法。但是不推荐，因为父类名称改变的话所有的子类都要改。

私有不继承：
子类能够继承的只是父类的公开内容，但是**不包括**父类的私有内容。
如果要访问的话也可以，但是需要间接的调用父类再用方法调用私有内容。


### 多继承
Python中，子类是可以同时有多个父类的：也就是能够同时继承多个父类的所有属性、方法。

继承格式：
```py
class Father:
    def func1(self):
        pass

class Mother:
    def func2(self):
        pass

class Son(Father, Mother):
    def func3(self):
        func1()
        func2()
```

注意：
如果多个父类间存在有同名的方法，那么会继承**第一个**父类的方法。


### `MRO, Method Resolution Order`
查看继承顺序：
通过类自带的`.__mro__`属性（`MRO, Method Resolution Order`)，可以查看这个类的继承顺序。

子类可以直接写`FatherName.func()`来调用父级函数。
但是当子类用`super().func()`时候，python就会根据`MRO`顺序，由近到远逐次寻找，找到最近的上级则返回。

用上例，如果是多继承的话，那么寻找顺序是：`SON -> Father -> Mother -> object`。

### 查看类的内置属性和方法：
`dir(className)`可以查看内置所有属性方法。


### Python内置的object基础类
Python3开始使用新式的类定义，即默认让所有定义的类都自动继承一个叫`object`的内置基础类。`object`基础类定义了很多方便的属性。包括18项之多。
而旧式的Python2.x时代，不继承object基础类，自己定义的类就只有`__doc__`和`__module__`两样内置属性而已。2.x时代，如果需要手动继承，如：
```py
class MyClass(object):
    pass
```


## 多态

多态是指，不同的子类对象调用相同的父类方法，会产生多态多样结果的编程特性。
多态的前提是能够继承父类的方法，且能够重写改写父类的方法。

多态的特点：
- 是调用方法的技巧，而不影响类的内部设计
- 可以增加代码灵活度

```py
def Father():
    def work(self):
        do_job()
     
    def do_job(self):
        print('Farming on the field...')


def Son(Father):
    def do_job(self):
        print('Programming at an office...')

# ---- Now let's work ----
Jason = Son()
Jason.work()
```
以上代码中，同样是`work()`函数，且要`do_work()`。但是，不同的人调用的是不同的`do_work`。
Father调用自己的do_work，儿子因为自己重写了do_work，所以调用自己的方法。
这就是多态——所继承的方法，不需要再特殊指定谁用什么方法，而对象会自动调用适合自己的方法。


## 类与实例

Python中，实例是一个对象，类也是一个对象，一切皆对象。但这也是Python OOP中引起很多麻烦的原因。

实例对象非常好理解，也好用，直接用，就不说了。但是`类对象`就不那么好理解了。

简单说，`类对象`也是一个标准的对象，有自己的属性和方法，只不过能够像`模版`一样生成多个实例对象而已。
类对象有这两大研究点：
- 类属性：就是能让所有实例访问和操作的公用厕所
    - 定义类属性：位于class的所有方法之外
    - 访问类属性：className.propertyName
- 类方法：比较难理解，必须用到名为`@classmethod`的装饰器，函数的第一个参数必须是关键字`cls`，如同`self`。
    - `@classmethod`装饰器：用来告诉解释器这是一个`类方法`，而不是实例方法。
    - `cls`参数：

### 类属性与实例属性

这是Python OOP中困扰很多人的特点。但是其实不难理解，总结如下：
```py
class MyClass:
    # 在这个位置定义的，叫类属性。==等同于其它语言的“静态属性”
    # 这是每个实例共有的公用属性，相当于宿舍的公用洗澡间
    count = 0
    
    def __init__(self):
        # 用self.定义的，叫实例属性，是每个实例只自己所有的属性，selfish
        self.name = "Jason"
```

访问类属性的方法有两种：
- `ClassName.propertyName`：推荐，直接用类名访问类属性。
- `Instance.propertyName`：不推荐用实例名访问类属性，因为如果需要写入操作，那么这种方法只会给自己**添加一个实例属性**，而不会影响类属性。


### 动态添加类属性

方法一：
```py
>>> MyClass.newAttribute = 'I am a class attribute'
>>> print( MyClass.newAttribute )
'I am a class attribute'
```

方法二：装饰器
```py
# Customized decorator for classproperty
class classproperty(object):
    def __init__(self, getter):
        self.getter= getter
    def __get__(self, instance, owner):
        return self.getter(owner)

class MyClass:
    @classproperty
    def newAttribute(cls):
        return 'I am a class attribute.'

>>> print( MyClass.newAttribute )
'I am a class attribute'
```
之所以把方法封装为一个类属性，是因为我们有时候需要根据其它类属性来定制这个类属性。
而一般情况下，我们没法在类属性定义的时候获得当前的类或类中其它的属性。


### 类方法
类方法如同类属性，是属于全类的方法，但是（推荐）只用来访问类属性。

类方法：比较难理解，必须用到名为`@classmethod`的装饰器，函数的第一个参数必须是关键字`cls`，如同`self`。
- `@classmethod`装饰器：用来告诉解释器这是一个`类方法`，而不是实例方法。
- `cls`参数：如同`self`，用来指代当前的类。

注意：`@classmethod`和`cls`都是关键字，不能改。

代码：
```py
class MyClass:
    # 定义一个“类属性”
    count = 0
    
    # 这里开始定义“类方法”
    @classmethod
    def func(cls):
        print(cls.count)
```


### 类静态方法

类中的`staticmethod`装饰器同样是python基础类object的一个用于包装、装饰的方法。一旦在类方法前放上装饰器`@staticmethod`，方法就会转换为一个`静态方法`。
静态方法就是一个非常独立的方法：既不访问实例的信息，也不访问类的信息。

代码：
```py
class MyClass:
    # 定义一个“类属性”
    count = 0
    
    # 这里开始定义“类方法”
    @staticmethod
    def func():
        pass
```

### Property属性

类中的`property`装饰器，也是python基础类object的一个用于包装、装饰的方法。一旦类方法前放上装饰器`@property`，方法就会转换为一个`类属性`。很多时候把方法伪装成属性，是非常方便的。

```py
class MyClass:
    # 这里开始定义由方法转换为“类属性”
    @property
    def name(self):
        return "Jason"

c = MyClass()
print( c.name )
```


在继承object基础类的情况下，python给出了三种类属性装饰，对应三种操作：
- 读取：`@property`
- 写入：`@name.setter`
- 删除：`@name.deleter`

也就是说，当你读取类属性`my_name`的时候，会调用被`@property`修饰的方法；当你修改`my_name`当时候，会调用被`@my_name.setter`修饰的方法；当你删除这个属性时，会调用被`@my_name.deleter`修饰的方法。

注意：
- 其中`@property`, `@*.setter`, `@*.deleter`，这是固定的名字，不能改。
- 三种操作所修饰的三个函数，必须都是**同一个名字**：即“类属性”名。

代码：
```py
class MyClass:
    # 这里开始定义由方法转换为“类属性”
    @property
    def name(self):
        return "Jason"

    @name.setter
    def name(self, value):
        self.name = value

    @name.deleter
    def name(self):
        del "Jason"

c = MyClass()

print( c.name )  # READ
c.name = "Brown"  # SET
del c.name  # DELETE
```

#### property属性的应用

很多OOP语言，针对`property属性`，一般操作是：**一个私有属性，配合两个公有方法**。
如：
```py
class MyClass:
    def __init__(self):
        self.__name = "Jason"

    def get_name(self):
        return self.__name

    def set_name(self, value):
        self.__name = value

c = MyClass()

# 开始调用
c.set_name("Brownee")
print( c.get_name() )
```

在Python下，可以利用装饰器改为以下代码，极大方便调用的过程：
```py
class MyClass:
    def __init__(self):
        self.__name = "Jason"

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

c = MyClass()

# 开始调用
c.name = "Brownee"
print( c.name )
```
