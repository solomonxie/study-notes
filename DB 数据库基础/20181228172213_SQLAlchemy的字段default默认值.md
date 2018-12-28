# SQLAlchemy的字段default默认值

我们都知道：
```py
age = Column('age', Integer, default=18)
```
这样的字段定义方式，即字段age默认值为18。

但是SQLAlchemy中，这个定义会出现一个问题：即默认值只有插入到数据库中才能生效。同样在运行中时，我们如果不用`session.query(..)`的方法，是无法获得这个值的，也即是说`obj.age`返回None。
即使`session.commit()`或`session.flush()`也没用。有人说的`ColumnDefault()`, `server_default=..`也都没用。

因为，default只会影响数据库，而不存留在ORM对象里。
所以，除了一些比较麻烦的hack外，还是建议直接给ORM对象的这个column字段显式赋值，比如`obj = MyORM(age=18)`，这样就能获取`obj.age`了。

[参考：Default Objects API](https://docs.sqlalchemy.org/en/rel_0_9/core/defaults.html#sqlalchemy.schema.ColumnDefault)
[参考：How to apply Column defaults before a commit in sqlalchemy](https://stackoverflow.com/questions/13791487/how-to-apply-column-defaults-before-a-commit-in-sqlalchemy)
