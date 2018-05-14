# Python2 乱码解决方案(Anti-TLDR)

```py
# 首先把所有相关字符串变量检查一遍
print type(s1)
print type(s2)
print type(s3)

# 然后把所有"unicode"格式的字符串转换成"str"格式
s1 = str(s1)
```
完成！
