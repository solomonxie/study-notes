# Python2 处理含中文特殊字符的CSV

## 使用第三方库轻松解决

https://github.com/jdunck/python-unicodecsv

```py
>>> import unicodecsv as csv
>>> from io import BytesIO
>>> f = BytesIO()
>>> w = csv.writer(f, encoding='utf-8')
>>> _ = w.writerow((u'é', u'ñ'))
>>> _ = f.seek(0)
>>> r = csv.reader(f, encoding='utf-8')
>>> next(r) == [u'é', u'ñ']
True
```



## YAML

https://stackoverflow.com/questions/956867/how-to-get-string-objects-instead-of-unicode-from-json

```py
>>> import json
>>> import yaml
>>> list_org = ['a', 'b']
>>> list_dump = json.dumps(list_org)
>>> list_dump
'["a", "b"]'
>>> json.loads(list_dump)
[u'a', u'b']
>>> yaml.safe_load(list_dump)
['a', 'b']
```
