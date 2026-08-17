# Scipy Basic Operation [DRAFT]

```py
import scipy.stats  # This is the right way to import
```


### Statistics Module

Generate Truncated Normalized Array with given Max, Min, Mean, STD and size:
```py
>>> norms = scipy.stats.truncnorm.rvs((low-avg)/std, (high-avg)/std, loc=avg, scale=std, size=bsize)
```
