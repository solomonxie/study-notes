# ❖ SQLAlchemy批量插入数据

SQLalchemy的插入数据不止有`session.add()`然后`session.commit()`而已。
实际上，以上做法是最慢的，尤其是面对批量数据插入的时候。

目前，批量插入的方法有：
- 普通ORM
- 自己设定主键的ORM
- ORM批量插入
- SQlalchemy Core
- 手动操作Sqlite3

[参考：Optimize Inserts Using SQLAlchemy](http://www.devx.com/dbzone/optimize-inserts-using-sqlalchemy.html)


假设插入最简单的数据10万条，花费时间如下：
```
SA ORM - total time: 12.31 seconds
SA ORM with PK - total time: 7.57 seconds
SA ORM Bulk insert - total time: 0.78 seconds
SA Core - total time: 0.09 seconds
Direct sqlite3 - total time: 0.46 seconds
```

明显最快的是Core，和其它选项完全不在一个数量级上。
速度从快到慢依次是：Core > Direct > ORM Bulk insert > ORM with PK > ORM

假设我们定义了一个简单ORM类：
```py
class Person(Base):
    id = Column(....., primary_key=True)
    name = Column(...)
```

## ORM inserts

```py
people = [ Person( name='NAME-{}'.format(i) ) for i in range(100000) ]

for p in people:
    session.add( o )
session.commit()
```


## ORM inserts with pre-computed Primary Key

```py
people = [ Person( id=i, name='NAME-{}'.format(i) ) for i in range(100000) ]

for p in people:
    session.add( p )
session.commit()
```

## ORM Bulk inserts

```py
people_d = [ dict( name='NAME-{}'.format(i) ) for i in range(100000) ]

session.bulk_insert_mappings( Person, people_d )
```


## SQLAlchemy Core

```py
people_d = [ dict( name='NAME-{}'.format(i) ) for i in range(100000) ]

engine.execute( Person.__table__.insert(), people_d )
```


## Sqlite3

(Won't be discussed here.)
