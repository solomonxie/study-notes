# Github API v3 分页问题 [DRAFT]

分页主要是在url后加`page`和`per_page`参数。
格式是?page=页数&per_page=每页包含数量。
如：
```
https://api.github.com/users/solomonxie/repos?page=2&per_page=3
```

如果没有传送任何分页数字，那么默认为`per_page=0`。大概30条数据。
做程序时不要忽视分页，否则漏掉数据很难发现。


## Python动态获取分页数据

```py

```
