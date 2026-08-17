# Python3 编码乱码问题
> 没想到从Python2升级到3，还是有编码问题-_-!

## 小技巧
在txt等文本文件读取时，如果遇到打开文件乱码，那么最简单的方法是把文件拖到Chrome浏览器里，然后在Chrome开发工具的Console里检查文件的编码格式：
```js
>>> document.charset
'UTF-16LE'
```
检查好了，然后再到python里针对其进行解码。

