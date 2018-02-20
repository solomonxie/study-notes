# Python图片转化为Base64编码
常用github api上传文件或图片，必须要将文件转化为base64编码才能上传。所以这里总结了下：
```python
import base64

with open('PATH-TO-IMAGE', 'rb') as f:
    pic = f.read()

print base64.b64encode(pic)
```
