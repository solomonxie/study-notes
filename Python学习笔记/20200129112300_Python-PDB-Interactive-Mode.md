# Python PDB Interactive Mode

Refer to: https://stackoverflow.com/questions/24149168/list-comprehension-scope-error-from-python-debugger

```py
(Pdb) x = [1, 2, 3, 3, 4]
(Pdb) [x for _ in range(1)]
*** NameError: name 'x' is not defined
```

Solution:
```py
(Pdb) interact
*interactive*
>>> [x for _ in range(2)]
[4, 4]
```
