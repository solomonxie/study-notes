# Read Headlines of a gzip file

```py
>>> with gzip.open('dimension_product_id.csv.gz', 'rb') as f:
>>>     print(f.readline())
category_id,name,unified_category_id,category_path,parent_category_id,market_code
>>>     print(f.readline())
400013,Puzzle,800005,OVERALL > GAME > GAME_PUZZLE,400001,google-play
```


```py
with gzip.open(path, 'rb') as f:
    if not any([f.readline() for i in range(2)]):
        logger.error(f'[EMPTY-FILE]: {path}')
```
