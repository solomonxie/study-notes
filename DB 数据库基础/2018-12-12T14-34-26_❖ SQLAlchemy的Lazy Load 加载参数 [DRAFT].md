# ❖ SQLAlchemy的Lazy Load 加载参数 [DRAFT]

[参考：flask-sqlalchemy中的lazy的解释](https://shomy.top/2016/08/11/flask-sqlalchemy-relation-lazy/)

SQLAlchemy的`relationship( ..., lazy='??' )`方法中的`lazy`参数一直是初学最容易困扰的地方。

`Lazy Load Methods`是SQLAlchemy为多表关联而定义的一系列加载方法。为lazy参数选择什么值，决定了 SQLAlchemy 什么时候从数据库中加载数据。每种方法的对应着SQL语句中多表关联的一种写法，所以优缺点、效率高低各有不同。

`lazy`参数的可选方法有：
- `select` - (默认) 后台会用select语句一次性加载所有数据，即访问到属性的时候，就会全部加载该属性的数据。
- `joined` - 数据会被JOIN语句加载，即对关联的两个表进行join操作，从而获取到所有相关的对象。
- `subquery` - 数据被用subquery子查询SQL语句加载
- `dynamic` - 在访问属性的时候，并不在内存中加载数据，而是返回一个query对象, 需要执行相应方法才可以获取对象。适用于数据量大的时候。 
- `immediate` - items should be loaded as the parents are loaded, using a separate SELECT statement, or identity map fetch for simple many-to-one references.
- `noload` - no loading should occur at any time. This is to support “write-only” attributes, or attributes which are populated in some manner specific to the application.
- `True` - 即 'select'方法
- `False` - 即 'joined'方法
- `None` - 即'noload'方法


下面用`School`和`Students`的实例来看各种方法的不同。

假设定义两个ORM类：
```py
class School(..):
    id = Column(..)
    students = relationship( 'Student', backref='school' )

class Student(..):
    id = Column(..)
    school_id = Column(.., ForeignKey('school.id') )
```

上例中我们建立了一个普通的两表关联：`students = relationship( 'Student', backref='school' )`。
默认情况下，参数`lazy`为select，我们不写也可以）。
也就是说，如果定义`lazy='select'`，那么当我们要进行搜索引用时（假设表中已有数据）：
```py
>>> school_01 = School.query.first()  # 随便获取一个数据库中已有的school
>>> school_01.students
[ <Student: u'test'>, <Student: u'test2'>, <Student: u'test3'> ]
```
可以看到，`lazy='select'`会简单直接的返回所有相关联的数据。
但是，如果数据量非常大：比如百万级，这种全部返回就不理智了，因为会大量侵占内存。
所以我们可以选择`lazy='dynamic'`，即只返回一个`query`查询对象，供你手动加条件查询，比如`query.all()`或`query.filter()`等。

假设我们将之前的定义改为：`students = db.relationship('Student', backref='_class', lazy="dynamic")`。那么：
```py
>>> school_01.students
<sqlalchemy.orm.dynamic.AppenderBaseQuery object at 0x7f007d2e8ed0>

>>> print( school_01.students )
SELECT students.id AS students_id, students.name AS students_name
FROM students, registrations
WHERE :param_1 = registrations.class_id AND students.id = registrations.student_id

>>> school_01.students.all()
[ <Student: u'test'>, <Student: u'test2'>, <Student: u'test3'> ]
```
可以看到, 执行`school_01.students`返回的只是一个`query`对象，甚至说只是返回了一条SQL
语句，就是没有具体数据。可以想像这个消耗的时间相当于0了。
而如果`lazy=select 或者 joined`均是直接返回结果。　

需要注意的是，
**`lazy="dynamic"`只可以用在一对多和多对对关系中，不可以用在一对一和多对一中。**

这样也合理：如果返回结果很少的话，就没必要延迟加载数据了。 

### backref(..., lazy=...) 反向引用的lazy加载

直接给`relationship(.., lazy='??')`，只是给`正向引用`设置加载方法。
实际上`反向引用`也是可以设置lazy加载方法的。
做法就是：使用`backref(..)`函数：
```py
    students = relationship(..., lazy='..', backref=backref('Student, lazy='dynamic') )
```
可以看到，`backref(..)`函数返回的是一个`backref`参数专用的值，在这里面可以指定反向引用的加载方法。


