# Python调试工具`pdb` —— Python Debuger
[参考文章1](https://zhuanlan.zhihu.com/p/25942045)，[参考文章2](https://docs.python.org/2/library/pdb.html)

- 启动方法一：`python -m pdb PATH-TO-SCRIPT.py`
- 启动方法二：代码中写入`import pdb;pdb.set_trace()`，即插入了一个断点。

## 常用命令
```shell
# 退出循环 (指针要指在for语句上才行）
until

# 下一步
next 或 n

# 深入性下一步（进入每次调用的函数里面）
step 或 s

# 移动到上一层／下一层函数
up 或 u
down 或 d

# 执行直至当前函数结束
return 或 r
```
