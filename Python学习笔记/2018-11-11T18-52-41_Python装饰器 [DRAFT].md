# Python装饰器 [DRAFT]


## 理解装饰器

Refer to: https://stackoverflow.com/a/309000

> "When you use a decorator, you're replacing one function with another. In other words, if you have a decorator."

When you're doing:
```
@new_func
def func(x):
    ...
```

What you did at the sign `@` is:
```py
func = new_func
```

You could get this result by:
```py
>>> func.__name__
new_func
```
Not only that, but also the `func.__doc__` and all other informations are lost.
The direct changing of function will cause a big problem, which is losing of metadata.

That's where `functools.wraps` takes into place: the `@wraps(func)` will copy all metadata from `old_func`:
```py
def tell_me_when(old_func):
    """Decorator for the purpose of passing a value to the target function"""

    @wraps(old_func)
    def new_func(*args, **kwargs):
        kwargs['when'] = '8:30 AM'  # important !
        ret = old_func(*args, **kwargs)
        return ret
    return new_func
```




## 示例

极简样式：
```py
# Define a decorator
def outter(func):
    def alternative():
        # ...Some code here...
        result = func()
        # ...Some code here...
        return result

    return alternative

# Apply a decorator
@outter
def stable_method():
    pass
```

标准样式：
```py
# Define a decorator
def outter(func):
    def alternative(*args, **kargs):
        # ...Some code here...
        result = func(*args, **kargs)
        # ...Some code here...
        return result

    return alternative

# Apply a decorator
@outter
def stable_method():
    pass
```

装饰器带参数样式：
```py
# Define a decorator
def outter(name):
    def inner(func):
        def alternative(*args, **kargs):
            print('I can use name={} here'.format(name))
            # ...Some code here...
            result = func(*args, **kargs)
            # ...Some code here...
            return result

        return alternative
    return inner

# Apply a decorator
@outter(name='Jason')
def stable_method():
    pass
```


## 类中定义装饰器

[参考：Decorator inside Python class](https://medium.com/@vadimpushtaev/decorator-inside-python-class-1e74d23107f6)



## 目的是给被装饰方法传参数的装饰器

假设我有一个功能方法，叫`do_something(what, how=None)`，第一个参数我肯定会给，但是第二个参数我想从装饰器里给，也就是在不改变代码的情况下做到这个情况。Python需要用到装饰器来达到。

假设目的是这样使用：
```py
@tell_me_when
def do_something(what, when):
    print('I am doing {} at {}'.format(what, when))

do_something("jogging")

[out]: I am doing jogging at 8:30 AM
```

那么这个传参数的装饰器怎么写呢？
```py
def tell_me_when(old_func):
    """Decorator for the purpose of passing a value to the target function"""

    def new_func(*args, **kwargs):
        kwargs['when'] = '8:30 AM'  # important !
        ret = old_func(*args, **kwargs)
        return ret
    return new_func
```


## 一个函数多个装饰器

```py
class TestCase():
    """ A simple test case. """

    @classmethod
    @with_session
    def setup_class(cls, session):
        print(cls, session)
```

期待的效果是执行`TestCase.setup_class()`时候，不需要手写任何参数，直接执行`setup_class`里的print。

