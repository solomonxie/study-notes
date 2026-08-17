# PostgreSQL 基础


## 命令行客户端psql操作

登陆数据库：
```sh
# -U 用户，-h 主机，-p 端口，结尾 DB名
psql -U postgres -h 127.0.0.1 -p 5432 mydb

数据库级别操作：
```sh
# 列出所有数据库
(psql) \l

# 连接指定数据库
(psql) use mydb

# 创建数据库


# 删除数据库
```


