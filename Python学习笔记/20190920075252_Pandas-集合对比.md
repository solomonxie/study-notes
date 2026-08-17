# Pandas 集合对比

```py
In [161]: df1=pd.DataFrame({'Date':['2013-11-24','2013-11-24','2013-11-24','2013-11-24'],
     ...:     'Fruit':['Banana','Orange','Apple','Celery'],
     ...:     'Num':[22.1,8.6,7.6,10.2],
     ...:     'Color':['Yellow','Orange','Green','Green']})
     ...: df2=pd.DataFrame({'Date':['2013-11-24','2013-11-24','2013-11-24','2013-11-24','2013-11-25','2013-11-25'],
     ...:     'Fruit':['Banana','Orange','Apple','Celery','Apple','Orange'],
     ...:     'Num':[22.1,8.6,7.6,1000,22.1,8.6],
     ...:     'Color':['Yellow','Orange','Green','Green','Red','Orange']})

In [255]: df1
Out[255]:
    Color        Date   Fruit   Num
0  Yellow  2013-11-24  Banana  22.1
1  Orange  2013-11-24  Orange   8.6
2   Green  2013-11-24   Apple   7.6
3   Green  2013-11-24  Celery  10.2

In [256]: df2
Out[256]:
    Color        Date   Fruit     Num
0  Yellow  2013-11-24  Banana    22.1
1  Orange  2013-11-24  Orange     8.6
2   Green  2013-11-24   Apple     7.6
3   Green  2013-11-24  Celery  1000.0
4     Red  2013-11-25   Apple    22.1
5  Orange  2013-11-25  Orange     8.6

In [257]: not_in = pd.concat([df2, df1, df1]).drop_duplicates(keep=False)

In [258]: pd.concat([df2, df1, df1]).drop_duplicates(keep=False).to_dict('index')
Out[258]:
{3: {'Color': 'Green', 'Date': '2013-11-24', 'Fruit': 'Celery', 'Num': 1000.0},
 4: {'Color': 'Red', 'Date': '2013-11-25', 'Fruit': 'Apple', 'Num': 22.1},
 5: {'Color': 'Orange', 'Date': '2013-11-25', 'Fruit': 'Orange', 'Num': 8.6}}
```
