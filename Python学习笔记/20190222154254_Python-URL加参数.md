# Python URL加参数

一般requests库可以直接加params参数，但如果不用requests就需要想别的方法了。

参考：https://stackoverflow.com/questions/2506379/add-params-to-given-url-in-python

```py
from urllib.parse import urlparse, urlencode

url = "https://stackoverflow.com/search?q=question"
params = {'lang':'en','tag':'python'}

url += ('&' if urlparse(url).query else '?') + urlencode(params)
```

或者写成函数：
```py
def furl(url, params={}):
    return url + ('&' if urlparse(url).query else '?') + urlencode(params)

>>> furl('https://example.com', {'q':"what is that", "lang":"en"})
https://example.com?q=what is that&lang=en
```
