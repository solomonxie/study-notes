# ❖ SQLAlchemy的类继承、抽象类

Python中的类继承是相当容易的，但是在SQLAlchemy中却不能直接用Python类继承完成，还要多加一些设置。

网上关于这个东西，东说西说的非常多，甚至官网都没有把最简单的解决方案po出来，取而代之的是非常复杂的`Inheritance Configuration`。

首先说最简单的方案，来自Stackoverflow，亲测完美有效，最符合Python类继承。

[参考：Sqlalchemy: avoiding multiple inheritance and having abstract base class](https://stackoverflow.com/questions/9606551/sqlalchemy-avoiding-multiple-inheritance-and-having-abstract-base-class?answertab=votes#tab-top)

## 正解 

在这里，我们称这个方法为`__abstract__`方法：
```py
Base = declarative_base()

class CommonRoutines(Base):
    __abstract__ = True

    id = Column(Integer, primary_key=True)

    def __init__(self):
        # ...

class Foo(CommonRoutines):
    __tablename__ = 'foo'

    name = Column(...)

    def __init__(self, name):
        super().__init__()
        self.name = name
        # ...
```

也就是说，抽象类中只要用`__abstract__ = True`代替`__tablename__`即可完成一切工作，其它一切都和Python内置的类继承一摸一样了。


## 继承中的类方法和静态方法

SQLAlchemy的ORM继承，在`classmethod`和`staticmethod`继承是和Python OOP面向对象的继承方案一致的。

也就是说：
- 被冠之`@staticmethod`的静态方法，会被继承，但是在子类调用的时候，却是调用的父类同名方法。
- 被冠之`@classmethod`的类方法，会被继承，子类调用的时候就是调用子类的这个方法。


## 继承中的外键

**奇怪的是，SQLAlchemy定义的ORM，在继承父级ORM时候，`Foreign Key`外键是不能继承的，它强制要求在子类中重新定义。**
[参考官方文档：Mapping Class Inheritance Hierarchies](https://sqlalchemy-html.readthedocs.io/en/rel_1_0_6/orm/inheritance.html) 建议直接用`Ctrl-f`搜索"foreign`关键字，就能看到官方在继承时，也都要重新定义一遍外键。

[再参考：SQLAlchemy Inheritance](https://stackoverflow.com/questions/1337095/sqlalchemy-inheritance)

```py
class Parent(Base):
    __abstract__ = True

    id = Column('id', Integer, primary_key=True)
    name = Column('name', String)
    age = Column('age', String)
    fk = Column('fk', Integer, ForeignKey('anotherTable.id'), primary_key=True)

class Son(Parent):
    __tablename__ = 'son'

    fk = Column('fk', Integer, ForeignKey('anotherTable.id'), primary_key=True)
```


## 其它继承方案

如果参考别人的方案、官网的方案，会让你晕头转向。
为了避免重复参考别人的东西，这里贴上一些**不是解决方案的解决方案**。

`declarative_base(cls=XX)`方法：
```py
class CommonBase(object):
    @classmethod
    def somecommonaction(cls):
        # body here

Base = declarative_base(cls=CommonBase)

class Table1(Base):
    # __tablename__ & Table1 specific fields here

class Table2(Base):
     # __tablename__ & Table2 specific fields here
```
这样的缺点是，很难看清继承关系。


官方的`__mapper_args__`方法：
```py
class Person(Base):
    __tablename__ = 'people'
    id = Column(Integer, primary_key=True)
    discriminator = Column('type', String(50))
    __mapper_args__ = {'polymorphic_on': discriminator}

class Engineer(Person):
    __tablename__ = 'engineers'
    __mapper_args__ = {'polymorphic_identity': 'engineer'}
    id = Column(Integer, ForeignKey('people.id'), primary_key=True)
    primary_language = Column(String(50))
```
可以看出，这个必须在父子类都中分别定义难懂的`__mapper_args__`属性。这还不算完，官网中还说各种映射需要不同的复杂设置。有兴趣可参考官网：https://docs.sqlalchemy.org/en/latest/orm/extensions/declarative/inheritance.html
