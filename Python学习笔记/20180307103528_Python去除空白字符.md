# Python去除空白字符
Python里面不是trim，而是strip.
```
# 去除两边所有空白字符
string.strip()

# 去除两边指定的字符 (不分顺序)
string.strip('\r\t\n')

# 只去除左边、右边，用法同上
string.lstrip(s)
string.rstrip(s)
```
