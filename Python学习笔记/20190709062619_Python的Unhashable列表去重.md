# Python的Unhashable列表去重

Refer to: https://stackoverflow.com/a/9427216

```py
def remove_duplicate_from_list(alist):
    return [dict(t) for t in {tuple(d.items()) for d in alist}]
```
