# ❖ SQLAlchemy 中的Group By用法

这里我们要用到的`query`对象的方法：
- `.filter_by(..)`
- `.group_by(..)`
- `.having(..)`

我们需要额外导入的方法：
`from sqlalchemy import func`

`func`方法主要用来做统计，映射到sql语句中具体的统计方法，如：
- `func.count(..)`
- `func.sum(..)`

func方法的格式为：`func('字段名').label('显示名')`


SQL语句的用法如下：
```sql
SELECT school, COUNT(*) AS c FROM persons WHERE gender="male" GROUP BY age
```

SQLAlchemy中如下：
```py
from sqlalchemy import func

results = sessin.query( Person.school, func.count('*').label('c') ).filter(
    Person.gender=='male'
).group_by( Person.age )
```

## 筛选

SQL中针对Group By还可以再进一步筛选，但是要用另一个关键词`Having`。

SQL语句的用法如下：
```sql
SELECT school, COUNT(*) AS c FROM persons WHERE gender="male" GROUP BY age HAVING c >1
```

SQLAlchemy中如下：
```py
nums = func.count('*').label('c')

results = sessin.query( Person.school, nums ).filter(
    Person.gender=='male'
).group_by(
    Person.age
).having(
    nums > 10
)
```
