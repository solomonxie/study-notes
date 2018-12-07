# Sqlite 使用


## Sqlite 命令行客户端

只需下载官方提供的压缩包，**无需编译**，解压后直接用里面的二进制文件`sqlite3`即可进入shell：
```sh
# Download
mkdir -p ~/bin/sqlite
cd ~/bin/sqlite
wget https://www.sqlite.org/2018/sqlite-tools-osx-x86-3260000.zip && \
unzip sqlite-tools-osx-x86-3260000.zip

# Make symlink
sudo ln -s ~/bin/sqlite/sqlite-tools-osx-x86-3260000/sqlite3 /usr/local/bin/sqlite3
```

[参考官方命令参考：Command Line Shell For SQLite](https://www.sqlite.org/cli.html)

常用命令：
```sh
# 创建／进入 一个数据库
$ sqlite3 DB_Test

# 显示当前数据库中的所有表
sqlite> .tables

# 显示所有schemas
sqlite> .schema

# 显示某个表的schema
sqlite> .schema tb_Users
sqlite> .schema tb_*

# 显示当前的客户端偏好设定
sqllite> .show
        echo: off
         eqp: off
     explain: auto
     headers: off
        mode: list
   nullvalue: ""
      output: stdout
colseparator: "|"
rowseparator: "\n"
       stats: off
       width:
    filename: test.sqlite


# 导入csv数据 (记得把.mode改回默认的list）
sqlite> .mode csv
sqlite> .import /home/pi/data.csv tb_Users

# 导出为csv数据
sqlite> .header on
sqlite> .mode csv
sqlite> .once /home/pi/OUT.csv
sqlite> SELECT * FROM tb_Users;
sqlite> .system /home/pi/OUT.csv
```

