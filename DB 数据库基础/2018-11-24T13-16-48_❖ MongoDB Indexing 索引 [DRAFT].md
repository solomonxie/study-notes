# ❖ MongoDB Indexing 索引 [DRAFT]

## 速度查询

显示某命令的执行效率：
```js
db.collection1.find().explain('executionStats');
```
然后会返回一个非常详尽的执行信息，其中的`ExecutionTimeMillis`代表语句的执行时间，`Millis`代表`milliseconds`毫秒。

![image](2018-11-24T13-16-48_❖ MongoDB Indexing 索引 [DRAFT]_files/img_01.png)


## 建立索引

MongoDB为某一个集合中的某一列快速建立Index索引：
```js
db.collection1.ensureIndex( {name:1} )
```
其中`1`表示按ASC升序建立索引，`-1`表示按DESC降序建立索引。

> 在测试的包含10万条数据的集合中，正常查询耗费84ms，而建立索引后只花费近似0ms！所以是快了8400%！


查看当前集合中，所有的Indeces索引：`db.collection1.getIndexes()`

删除索引只要`db.collection1.dropIndex( {索引名:1})`

建立索引的更多选项：
```js
# 建立联合索引
db.collection1.ensureIndex( {name:1, age:1, job:1} )

# 建立唯一索引（去除重复）
db.collection1.ensureIndex( {name:1}, {unique: true} )
```


> 唯一索引有什么用呢？—— 爬虫数据去重：建立爬取数据关键字段的索引，如`url`，设置其索引为`unique`。然后在爬到一个新页面时，肯定要检查数据库中是否已经有此页面。那么就可以通过url来查询数据库。这时候，显然使用Index索引来查询能极大加快查询速度，而这个查询中我们不需要重复的url，只要知道有一个url是和新页面相同的，就可以不用下载页面了。
