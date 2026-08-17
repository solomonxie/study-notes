# Python修改URL端口

```sh
import urllib
obj = urllib.parse.urlparse(url)
url = obj._replace(netloc=f'{obj.hostname}:8888').geturl()
```
