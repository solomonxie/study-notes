# Python正则表达式Regular Expression

```py
import re
s = '<h3>下一个你需要输入的数字是83105. </h3>'

pattern = re.compile(r'<h3>\D+(\d{5})\D*</h3>')
result = pattern.findall(s)

print(result)
#out>>>  ['83105']
```
