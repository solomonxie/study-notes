# Python模块 [DRAFT]

[参考：Python 的 Import 陷阱](https://medium.com/pyladies-taiwan/python-%E7%9A%84-import-%E9%99%B7%E9%98%B1-3538e74f57e3)

## if __name__ == "__main__"
一般如果是个可以独立运行的模块(.py)文件，则可以定义一个入口：
```py
def main():
    # Only to call functions, 
    # NO code for implementation should be written here
    pass

if __name__ == "__main__":
    main()
```

## 导入模块方式

```py
# @1: Import all methods, 
#     NEED to specify module's name when use methods
#     etc., MOD.FUNC(), MOD.SUBMOD.FUNC()
import MOD
import MOD.SUBMOD

# @2: Declare methods to import, 
#     NO need to specify module's name when use methods
#     etc., FUNC()
from MOD import *
from MOD import METHODS
from MOD.SUBMOD import METHODS

# @3: Import local package
```

## 被导入模块中的公用变量

如果在一个`common.py`中定义一个全局变量`PUBLIC_VARIABLE`，那么在别的模块中import时，也能够使用这个公用变量。
但是，
这两种方法导入公用变量后情况会有不同：
- `import MOD`: 这种引入方法，由于调用时是用`MOD.PUBLIC_VARIABLE`来使用，所以这个公用变量在一处被修改后，其它所有引用它的文件中，变量都会变动。
- `from MOD import PUBLIC_VARIABLE`：由于调用时是用`PUBLIC_VARIABLE`，只相当于生成了一个本地的`global variable`，那么无论怎么修改，也不会影响其它文件所引用的这个变量。




