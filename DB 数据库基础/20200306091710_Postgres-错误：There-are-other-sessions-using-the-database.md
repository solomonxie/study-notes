# Postgres 错误：There are other sessions using the database

因为有其它session没有正常关闭，所以在删除数据库过程中会报错。
过多的连接sessin会导致PG无法正常查询数据，所以有时候必须断开所有连接。

参考：http://www.leeladharan.com/drop-a-postgresql-database-if-there-are-active-connections-to-it

```sh
# 查看所有正在连接的session
(psql) SELECT * FROM pg_stat_activity WHERE datname = 'MYDB';

(psql) SELECT pg_terminate_backend(pg_stat_activity.pid) FROM pg_stat_activity WHERE pg_stat_activity.datname = 'MYDB'  AND pid <> pg_backend_pid();
```
上面这句话是调用`pg_terminate_backend()`函数来删除所有active连接。
