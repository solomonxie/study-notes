# Python 异常捕获 [DRAFT]

**Python的异常，会直接导致`进程`的死亡。**

常用配置是这样的：
```
try:
    do_something()
except BaseException as e:
    print 'Failed to do something: ' + str(e)
```

