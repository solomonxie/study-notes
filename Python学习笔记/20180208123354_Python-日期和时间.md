# Python 日期和时间

获取当前日期：
```py
from datetime import date
d = str(date.today())
print(d)
```

字符串转日期：
转换`YYYY-MM-DDTHH:mm:sZ`格式日期，如`2015-12-07T22:31:28Z`
```py
from datetime import datetime

# 根据给定日期，制作一个相应的格式
date_format = "%Y-%m-%dT%H:%M:%SZ" 

# 用给定日期格式来解码转换
d = datetime.strptime('2015-12-07T22:31:28Z', date_format)

print(d)
#[out]: 2015-12-07 22:31:28
```

日期转字符串（给定格式）：
```py
from datetime import datetime

format  = '%Y-%m-%d'
today  = datetime.today()

print( today.strftime(format) )
#[out]: '2018-07-31'
```

日期加减：
```py
import datetime

today = datetime.date.today()

oneday = datetime.timedelta(days=1)

yesterday = today - oneday

tommorrow = today + oneday

print(yesterday, today, tommorrow)
#[out]: 2011-06-02      2011-06-03      2011-06-04
```
