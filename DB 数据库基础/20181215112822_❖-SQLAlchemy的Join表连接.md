# ❖ SQLAlchemy的Join表连接

[参考Stackoverflow：sqlalchemy: how to join several tables by one query?](https://stackoverflow.com/questions/6044309/sqlalchemy-how-to-join-several-tables-by-one-query)



## 直接条件查询

假设我们要用`直接条件查询`的方式连接三个表：
```sql
SELECT
    user.email,
    user.name,
    document.name,
    documents_permissions.readAllowed,
    documents_permissions.writeAllowed
FROM
    user, document, documents_permissions
WHERE
    user.email = "user@email.com";
```

对应的SQLAlchemy的查询语句为：
```py
session.query(
    User, 
    Document, 
    DocumentsPermissions
).filter(
    User.email == Document.author
).filter(
    Document.name == DocumentsPermissions.document
).filter(
    User.email == "user@email.com"
).all()
```


## Join

```sql
SELECT 'all the columns'
FROM user
JOIN document ON document.author_id = user.id AND document.author == User.email
JOIN document_permissions ON document_permissions.document_id = document.id 
    AND document_permissions.document = document.name
```

Then you should do something along the lines of:
```py
session.query(
    User
).join(
    Document
).join(
    DocumentsPermissions
).filter(
    User.email == "user@email.com"
).all()
```

One note about that...
```py
query.join(Address, User.id==Address.user_id) # explicit condition
query.join(User.addresses)                    # specify relationship from left to right
query.join(Address, User.addresses)           # same, with explicit target
query.join('addresses')                       # same, using a string
```
For more information, visit the docs.


## Inner Join 内连接

如果我们需要定义一个Many-to-Many多对多的关系，我们知道定义这种关系，必须在两表之间设计一个Mapper中间表来保存所有的映射关系。
假设这里的关系是`Person <-> Course`

```py
from myORMs import Person, Course, Mapper

# Define A Many-to-Many relationship
query = session.query(
    Person
).join(
    Mapper, Mapper.child_id == Person.id
).join(
    Course, Mapper.parent_id == Course.id
).filter(
    Person.name == 'Jason'
)
```


## Join same table multiple times

[参考官方：ORM-Specific Query Constructs - sqlalchemy.orm.aliased](https://docs.sqlalchemy.org/en/latest/orm/query.html?highlight=aliased#sqlalchemy.orm.aliased)

正常情况下我们不需要，如果我们想把这三个表全部一起查询、达到同时显示某个Person的School信息和City信息怎么办？

如果我们有多种Many-to-Many多对多关联的表，所以我们必须要在每一对关联表中间加设一个Mapper作为映射多对多关系。
因为用来用去都是一样，我们完全可以用一个mapper包括所有的映射关系，只是多加一个字段予以区分即可。
如果要这样做的话，就免不了要设置别名，在SQL中我们可以通过`.. AS ..`轻松做到，SQLAlchemy其实也不复杂，只需要用一个`aliased()`方法即可轻松达到同样的目的，而且不会影响效率。

> 注意区分`alias()`和`aliased()`不同


假设我们有4个表、2对多对多的关系，`Person <-> Course`, `Person <-> Major`。然后我们用Mapper统一进行关系映射。



```py
from sqlalchemy.orm import aliased

from myORMs import Person, Course, Major, Mapper

PersonCourse = aliased( Mapper )
PersonMajor   = aliased( Mapper )

query = session.query(
    Person
).join(
    PersonCourse, PersonCourse.child_id == Person.id
).join(
    Course, PersonCourse.parent_id == Course.id
).join(
    PersonMajor, PersonMajor.child_id == Person.id
).join(
    Major, PersonMajor.parent_id == Major.id
).filter(
    Person.name == 'Jason'
)
```





