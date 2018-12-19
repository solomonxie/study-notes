# Python的Circular Import 循环引用的问题 [DRAFT]

[参考：Python 的 Import 陷阱](https://medium.com/pyladies-taiwan/python-%E7%9A%84-import-%E9%99%B7%E9%98%B1-3538e74f57e3)

## 解决逻辑问题

很大比例下，循环引用／循环导入都不是技术问题，而是逻辑问题，即都可以通过逻辑拆分文件而避免循环引用的怪圈。

以下为示例：
```py

```

## 硬要循环引用

也有很多情况不可避免的要循环导入，以下为搜集到的解决方案。

```py

```
