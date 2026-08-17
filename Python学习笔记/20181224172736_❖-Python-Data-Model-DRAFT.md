# ❖ Python Data Model [DRAFT]

[Refer to Youtube: James Powell - So you want to be a Python expert?](https://www.youtube.com/watch?v=cKPlPJyQrt4)
[Refer to: Python document - Data model](https://docs.python.org/3/reference/datamodel.html)


## `__repr__` Representation method


```py
class Polynomial:
    def __init__(self, *coeffs):
        self.coeffs = coeffs
    def __repr__(self):
        return 'Polynomial(*{!r})'.format(self.coeffs)
```


## `__new__`

在生成一个新对象时，`__new__`方法会被最先调用
