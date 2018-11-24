# ❖ MySQL存储过程 (即函数)

[参考：mysql存储过程详细教程](https://www.jianshu.com/p/7b2d74701ccd)

SQL的`Stored Procedure`存储过程，指的其实就是一个`函数`。
既然是函数，那么就会涉及这几个要点：定义函数、使用函数、变量、参数、返回值等。

> 为了方便理解，以下就不再叫它存储过程，而直接叫函数了。

在MySQL中，这几个要点的语法如下：
- 定义函数：`CREATE PROCEDURE 函数名(参数列表) BEGIN ...具体的SQL语句... END`
- 使用函数：`CALL  函数名(参数列表);`
- 参数类型：
    - `IN`: 参数被拷贝为函数内局部变量，不影响原本的变量值。`func(IN age INT)...`
    - `OUT`: 参数只是传了个引用，函数内修改的话外部变量也会变。
    - `INOUT`: 函数内修改的话外部变量也会变。
- 声明变量：`DECLARE 变量名 类型 DEFAULT 默认值;`
- 设置变量：`SET @变量名="Jason"`
- 使用变量：调用时用`@变量名`，print显示时用`SELECT @变量名;`

## 函数定义即调用

单行函数:
```sql
CREATE PROCEDURE 函数名(参数) 一句SQL语句;

-- 如：
CREATE PROCEDURE GreetWorld(@whom) SELECT CONCAT('Hello', @whom); 
```

多行函数:
```sql
-- 
DELIMITER //   -- 分隔符
CREATE PROCEDURE 函数名(参数类型 参数名 数据类型)
BEGIN
    具体的SQL语句
    具体的SQL语句
END //
DELIMITER ;   -- 分隔符

-- 示例：
DELIMITER //  
CREATE PROCEDURE funcName(IN p_in int)  
BEGIN   
    SELECT p_in;   
    SET p_in=2;   
    SELECT p_in;   
END //  
DELIMITER ;
```

调用函数：
```sql
-- 变量赋值
SET @p_in=1;  

-- 调用函数
CALL funcName(@p_in);
```

函数（存储过程）的其它操作：
```sql
-- 修改函数
ALTER PROCEDURE .....

-- 删除函数
DROPPROCEDURE 函数名 ;
```

## 变量操作

```sql
-- 声明一个函数内的新变量（必须放在函数最上方）
DECLARE 变量名 数据类型 DEFAULT 默认值; 

-- 设置变量值
SET @x = 'Goodbye Cruel World';  
-- 或
SELECT 'Hello World' into @x; 
```



## 条件控制 IF-ELSE / CASE

IF-ELSE结构：
```sql
IF param=0 THEN
    update t set s1=s1+
ELSE 
    update t set s1=s1+
END IF ;
```

CASE结构：
```sql
CASE var  
    WHEN 0 THEN
        insert into t values(17);  
    WHEN 1 THEN
        insert into t values(18);  
    ELSE   
        insert into t values(19);  
END CASE ;
```


## 循环语句 WHILE / REPEAT / LOOP / ITERATE

WHILE-DO方式
```sql
WHILE var < 100 DO
    具体的SQL语句。
ENDWHILE ;
```

REPEAT方式：
```sql
REPEAT
    具体SQL语句。
UNTIL var <= 100
ENDREPEAT ;
```

LOOP方式：
```sql
label: 
LOOP
    具体SQL语句。
    LEAVE label ;
END LOOP
```
其中，采用循环标签`标签名：`的方式可以加在While / Repeat / Loop前，这样就可以使用`leave`语句退出循环，相当于break的意思。


ITERATE迭代方式：
```sql
label:
LOOP
    IF var = 3 THEN
        ITERATE label ;
    END IF ;

    IF var >= 5 THEN
        LEAVE label ;
    END iF ;
END LOOP ;
```


## MySQL常用内置函数

[参考：Mysql常用函数总结](https://my.oschina.net/zimingforever/blog/287629)

```sql

```
