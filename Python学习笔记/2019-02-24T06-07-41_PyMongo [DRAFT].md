# PyMongo [DRAFT]


更新（如果不存在，则创建）：
```py
data = {'username':'jason01', 'age':18}
DB.Collection01.update_one(
    {'username': 'jason01'}, {"$set":data}, upsert=True
)
````
这个操作主要是`upsert=True`与`$set`的组合使用才能做到。
