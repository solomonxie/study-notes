# What is Cascading in Computer Science

The confusing word `Cascading` in programming varies in different context.

We have found that word in different scopes:
- CSS
- C++
- Object-Oriented Programming (OOP)
- Database

In simple terms, `Cascading` refers to the process of performing multiple operations/tasks in a single line of programming code.


## In C++

```c++
cout<<”Enter your name”;
cout<<endl;
cout<<”Where do u live?”;
```

The above 3 lined code can be written in a single line…
```c++
cout<<Enter your name”<<endl<<”Where do u live?”;
```


## In OOP: Method Cascading

Refer to: https://www.wikiwand.com/en/Method_cascading

> " In object-oriented programming, method cascading is syntax which allows multiple methods to be called on the same object."



## In CSS

`Cascading styles` means that if we write CSS for the <body>, all the branches and leaves below will automatically inherit that CSS too.

For example, if you set the background of `<body>` as _red_, then all the elements within _body_ has a red background, unless you set the background of each element specifically.



## In Database

In the context of Database, `Cascading` means to run a sequence of actions.
Simply saying, an action will run after an event if you write `CASCADE` expression to specify it.

[Refer to: SQL Server: Foreign Keys with cascade delete](https://www.techonthenet.com/sql_server/foreign_keys/foreign_delete.php)

That `CASCADE` keyword is specified when you define a table:
```sql
CREATE TABLE inventory
( inventory_id INT PRIMARY KEY,
  product_id INT NOT NULL,
  quantity INT,
  min_level INT,
  max_level INT,
  CONSTRAINT fk_inv_product_id
    FOREIGN KEY (product_id)
    REFERENCES products (product_id)
    ON DELETE CASCADE
);
```

The `ON DELETE CASCADE` means that: **when you delete the table, its related table with its foreign key will be deleted as well, ** so that we don't need to delete related tables one by one but only to delete **one** main table.

