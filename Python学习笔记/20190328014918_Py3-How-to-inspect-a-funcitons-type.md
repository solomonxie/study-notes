# (Py3) How to inspect a funciton's type

Types:
- Normal function
- ClassMethod
- InstanceMethod
- StaticMethod
- Method in Subclass


Cases:
```py
def ff():
    pass

class A:
    @staticmethod
    def sm():
        pass
    @classmethod
    def cm(cls):
        pass
    def im(self):
        pass

class B:
    class C:
        def im(self):
            pass
        @classmethod
        def cm(cls):
            pass
        @staticmethod
        def sm():
            pass
    @classmethod
    def cm(cls):
        def f_():
            pass
        return f_
    def im():
        def f_():
            def f__():
                pass
            return f__
        return f_
```

Facts:
```py
>>> cm.__qualname__, sm.__qualname__, im.__qualname__, ff.__qualname__
 ('A.cm', 'A.sm', 'A.im', 'ff')

>>> str(A.cm), str(A.sm), str(A.im), str(ff)
("<bound method cls.cm of <class '__main__.cls'>>",  '<function cls.sm at 0x113977378>',
 '<function cls.im at 0x114367950>', '<function ff at 0x113977158>')

>>> from inspect import *
>>> ismethod(A.cm), ismethod(A.sm), ismethod(A.im), ismethod(ff)
 (True, False, False, False)
>>> isfunction(cm),  isfunction(sm), isfunction(im),  isfunction(ff)
(False, True, True, True)

>>> getmembers(A, ismethod)
[('cm', <bound method A.cm of <class '__main__.A'>>),
 ('xm', <bound method A.xm of <class '__main__.A'>>),
 ('xxm', <bound method A.xxm of <class '__main__.A'>>)]
>>> getmembers(A, isfunction)
[('im', <function __main__.A.im(self)>), ('sm', <function __main__.A.sm()>)]

>>> from types import *
>>> isinstance(A.cm, MethodType), isinstance(A.sm, MethodType),isinstance(A.im, MethodType),isinstance(ff, MethodType)
 (True, False, False, False)
>>>  isinstance(A.cm, FunctionType), isinstance(A.sm, FunctionType),isinstance(A.im, FunctionType),isinstance(ff, FunctionType)
(False, True, True, True)
```


Tests:
```py
# Class methods
assert inspect_type(A.sm) == ('staticmethod', A)
assert inspect_type(A.cm) == ('classmethod', A)
assert inspect_type(A.im) == ('instancemethod', A)
# Function
assert inspect_type(ff) == ('function', None)
# Sub classes
# assert B.cm().__qualname__ == 'B.cm.<locals>.f_'
assert inspect_type(B.im()) == ('function', None)
assert inspect_type(B.C.im) == ('instancemethod', B.C)
assert inspect_type(B.C.cm) == ('classmethod', B.C)
assert inspect_type(B.C.sm) == ('staticmethod', B.C)

print('OK.')
```





## Solution 1:

```py
import inspect
import sys

def inspect_type(func):
    ftype = None
    if '.' not in func.__qualname__:
        ftype = 'function'
        print('Normal function')
    else
        # __qualname__: 'className.functioNname'
        cls_name = func.__qualname__.rsplit('.', 1)[0]
        # Get the class by name
        cls = getattr(sys.modules[func.__module__], cls_name)
        # cls.__dict__[func.__name__] should return like <class 'staticmethod'>
        ftype = cls.__dict__[func.__name__].__class__.__name__
        if ftype == 'staticmethod':
            print('staticmethod')
        elif ftype == 'classmethod':
            print('classmethod')
        elif ftype == 'function':
            print('instance-method')
        else:
            raise TypeError('Unknown Type %s, Please check input is method or function' % func)
    return ftype

inspect_type(A.sm)
inspect_type(A.cm)
inspect_type(A.im)
inspect_type(ff)
```

Drawback:
This solution WON'T work for methods in SUBCLASS.




## Solution 2

```py
import sys

def get_func_class(func):
    classes = []
    parent = sys.modules[func.__module__]
    names = func.__qualname__.split('.')[:-1]
    for n in names:
        parent = parent.__dict__[n]
        if isinstance(parent, type):
            classes.append(parent)
    return classes[-1] if classes else None

def inspect_type(func):
    ftype = None
    if func.__name__ == func.__qualname__:
        return 'function', None
    elif '.<locals>' in func.__qualname__:
        return 'function', None
    cls = get_func_class(func)
    ftype = cls.__dict__.get(func.__name__)

    if type(ftype) == staticmethod:
        return 'staticmethod', cls
    elif type(ftype) == classmethod:
        return 'classmethod', cls
    elif ftype.__class__.__name__ == 'function':
        return 'instancemethod', cls
    else:
        raise TypeError('Unknown Type %s, Please check input is method or function' % func)
```
