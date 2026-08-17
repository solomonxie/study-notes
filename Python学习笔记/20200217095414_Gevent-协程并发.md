# Gevent 协程并发

参考：https://sdiehl.github.io/gevent-tutorial/

```py
import gevent
from gevent.pool import Pool

def a():
    print('\n\n[  START  ] a\n\n')
    __import__('time').sleep(0.5)
    gevent.sleep(1)
    print('\n\n[  END  ] a\n\n')
    return 'aaaaa'

def b():
    print('\n\n[  START  ] b\n\n')
    __import__('time').sleep(0.5)
    print('\n\n[  END  ] b\n\n')
    return 'bbbbb'

print('BEGINNING...')

pool = Pool(4)
tasks = [pool.spawn(a), pool.spawn(b)]
gevent.joinall(tasks)

print([t.value for t in tasks])
print('FINISHED.')

"""
#[OUTPUT]

BEGINNING...

[  START  ] a

[  START  ] b

[  END  ] b

[  END  ] a

['aaaaa', 'bbbbb']
FINISHED.
"""
```
