# ❖ SQLAlchemy Core: 执行原生SQL语句

## 查询：执行固定SQL语句

```py
engine = create_engine('........')
conn = engine.connect()
records = con.execute('SELECT title, author FROM book')
for title, author in records:
    print(title, author)
conn.close()
```

### 关于fetchone()和fetchall()

我们可以执行`conn.execute('..').fetchone()`或`.fetchall()`。
前者只返回数据库中第一条，后者一次性从数据库中取出所有条目（效率较低）。

建议不要用`fetchall()`，取而代之的是iterate迭代式：`for r in con.execute('..'):`这种方法。



## 查询：指针查询

```py
engine = create_engine('.......')
conn = engine.raw_connection()
cur = conn.cursor()
cur.execute('SELECT word, weight FROM sensitive_word')
for word, weight in cur:
    print(word, weight)
cur.close()
conn.close()
```



## 查询：执行带parameters参数的SQL语句

为了防止SQL-Injection注入，最好不要直接把外部获取的参数加入到SQL字符串中。

SQLAlchemy有一些专门的方法向SQL加入参数：
- `text()`方法
- `con.execute(sql, values)`方法

`text()`方法：
```py
from sqlalchemy import text

sql = "SELECT id, name FROM users WHERE id=:id"
tsql = text(sql)

with engine.connect() as conn:
    records = conn.execute(tsql, id=123)

    for r in records:
        print( r )
```

## 更新：执行原生的SQL语句


```py
session.execute(
    "UPDATE client SET musicVol = :mv, messageVol = :ml",
    {'mv': music_volume, 'ml': message_volume}
)
```


## 插入：字典方法

```py
conn.execute(
    table.insert(),
    {"id":1, "value":"v1"},
    {"id":2, "value":"v2"}
)
```

```py
conn.execute(
    "INSERT INTO table (id, value) VALUES (?, ?)",
    (1, "v1"), (2, "v2")
)
```

