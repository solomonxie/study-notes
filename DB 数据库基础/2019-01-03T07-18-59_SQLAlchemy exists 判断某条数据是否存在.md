# SQLAlchemy exists 判断某条数据是否存在

参考：https://stackoverflow.com/questions/6587879/how-to-elegantly-check-the-existence-of-an-object-instance-variable-and-simultan

```py
from sqlalchemy import exists

it_exists = Session.query(
    exists().where( SomeObject.field==value )
).scalar()
```

然后会返回True或False。


多选择条件的较复杂判断：
```py
query = session.query(Users).filter(
    Users.name.in_( ['Jack', 'Bob', 'Sandy'] ),
    Users.age == 18
)

# Below will return True or False
at_least_one_user_exists = session.query(
    query.exists()
).scalar()
```

[参考：Calling exists() in sqlalchemy with multiple values in python](https://stackoverflow.com/questions/39089153/calling-exists-in-sqlalchemy-with-multiple-values-in-python)
