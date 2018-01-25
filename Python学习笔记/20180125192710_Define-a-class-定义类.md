# Define a class 定义类

```
class Person:
    self.name = ''
    self.id = 0
    self.father = 1
    self.mother = 2 

    def __init__(self, name):
        self.name = name
	self.born()
    
    def born(self):
        self.id = self.father + self.mother

me = Person('Solomon')
print(me.id)
```
