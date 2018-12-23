# Python获取URL中参数的方法

虽然只是个简单的URL，我们可以随时手动`split()`来获取每个参数。但是，
这太不`pythonic`了，太傻了。

所以我们要做的就是找到一个专门处理的函数，将URL中query部分的参数获取为字典。

Google了一圈，最简单的方法就是：
```py
>>> url = 'https://www.google.com/search?newwindow=1&biw=1091&bih=763'

>>> from urllib import parse
>>> params = parse.parse_qs( parse.urlparse( url ).query )

>>> params['newwindow']
['1']
>>> params['biw']
['1091']
```


还有个最pythonic的方式，需要第三方库`pip install furl`：
```py
>>> from furl import furl
>>> f = furl("/abc?def='ghi'") 
>>> f.args['def']
```
