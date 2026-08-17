# Python Sort a list of dictionaries

Refer to: https://stackoverflow.com/a/73050/9172013

Best practice:
```py
A = [{'name':'Homer', 'age':39}, {'name':'Bart', 'age':10}]

# This returns a new list (a is not modified)
sorted(a, key=lambda k : k['name']) 

# This changes the list a
a.sort(key=lambda k : k['name'])
```
