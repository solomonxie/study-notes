# Python Float number formatting

```py
#py2
>>> import json
>>> json.dumps({"x": 0.0000001})
'{"x": 1e-07}'

#py3
>>> import json
>>> json.dumps({"x": 0.0000001})
'{"x": 1e-07}'
```

Solution (Same in both Py2 & Py3):
```py
>>> x = 0.0000001
>>> x
1e-07

>>> format(x, 'f')
0.0000001
```

Or refer to https://stackoverflow.com/questions/36053615/preventing-auto-scientific-form-for-numbers-in-python3:
```py
>>> number
1.1e+23
>>> format(number, 'f')
'110000000000000004194304.000000'
>>> format(number, '.0f')
'110000000000000004194304'
You can also use that with format strings:

>>> 'The number is {:.0f}'.format(number)
'The number is 110000000000000004194304'
```






