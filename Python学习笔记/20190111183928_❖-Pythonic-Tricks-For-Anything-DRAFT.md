# ❖ Pythonic Tricks For Anything [DRAFT]


## STRING

### Convert a character to number

```py
>>> char2num = lambda c: ord(c)-64

>>> char2num('A')
1
```

### Convert a number to a character

```py
>>> num2char = lambda n: chr(n+64)

>>> num2char(2)
'B'
```





## LIST

### Deep copy a list
```py
>>> a = [1,2,3,4]
>>> b = a[:]

>>> b
[1,2,3,4]
>>> b is a
False
```

### Add multiple elements to list

Add to the head:
```py
>>> a = [1,2,3,4]
>>> a[:0] = [-2,-1,0]  # same with a[0:0] = ...
>>> a
[-2,-1,0,1,2,3,4]
```

Add to the last:
```py
>>> a = [1,2,3,4]
>>> a[-1:] = [ a[-1], 5,6,7 ]   # same with a[-1:0] = ...
>>> a
[1,2,3,4,5,6,7]
```

Add to any position:
```py
>>> a = [1,2,3,4]
>>> a[2:2] = [9,9,9]
>>> a
[1,2,9,9,9,3,4]
```


### Reverse a list
```py
>>> a = [1,2,3,4]
>>> a[::-1]
[4,3,2,1]
```


### Easiest way to print a list
```py
>>> myList = [1, 2, 3, 4]
>>> print(*myList, sep='; ')
1; 2; 3; 4
```

### Filter a list with only unique items
```py
>>> new = list( set(myList) )
```

### Sort customized objects in a list
```py
>>> people
[<Person age=24>, <Person age=45>, <Person age=33> ...]

>>> newlist = sorted(people, key=lambda o: o.age, reverse=True)
>>> newlist
[<Person age=24>, <Person age=33>, <Person age=45>, ...]
```


### Make a range of numbers into a list
```py
>>> list( range(10) )
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```

### Convert a string to a list of each character
```py
>>> list('ABCDE')
['A', 'B', 'C', 'D', 'E']

>>> list('54321')
 ['5', '4', '3', '2', '1']
```


### Extract each digit into a list

Method1 (intuitive):
```py
>>> N = 492
>>> list( str(N) )
['4', '9', '2']
```

Method2 (faster):
```py
>>> N = 492
>>> digits = []
>>> while N > 0:
            digits.append( N % 10 )
            N = N // 10
>>> digits
[2, 9, 4]
```


## DICT

### Get an item from dict safely
```py
>>> d.get('name')
'Jason'

>>> d.get('XXXX')
None

>>> d.get('XXXX', {}).get('name')
None

>>> for a in d.get('XXXX', []):
>>>     print( a )
```






## FUNCTION

### Pass uncertain function parameters
```py
def func1(**kwargs):
    for k,v in kwargs.items:
        print( k, v )

def func2(**kwargs):
    func1(**kwargs)
```





## CLASS | OBJECT


### Adding multiple properties to an object
```py
class A:
    d = '444'
    e = '555'

jsondata = {'a':'111', 'b':'222', 'c':'333'}
obj = A()
for k,v in jsondata:
    setattr( obj, k,v)
```


### set() method for custom objects

The class could be implemented a pair of Magic Methods:
- `__hash__`: pick unique properties on your own choice (instead of builtin choice on all properties)
- `__eq__`: customized "equal" statement

```py
class A:
 
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __hash__(self):
        return hash((self.id, self.name))

    def __eq__(self, other):
        if not isinstance(other, type(self)): return NotImplemented
        return self.id == other.id and self.name == other.name

>>> persons = [A(111, 'Jason', A(222, 'Saul', A(111, 'Jason']
>>> set( persons )
# [out]: {<__main__.A object at 0x106dee518>, <__main__.A object at 0x106dee4e0>}
```

