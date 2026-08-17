# ❖ Python clipboard/pasteboard image 处理剪切板图像问题

目前python对剪切板的原生支持几乎是没有，必须下载第三发模块。
目前比较流行的是跨平台最好的`pyperclip`和比较强大的`gtk`。
但是pyperclip虽然简单易用，但是只支持文字，不支持图片等。
gtk支持剪切板中的图像，但是代码较复杂，因为它原本是为了做桌面程序的库。

再深入调查，python专门处理的图像的`PIL`库以及其升华版`Pillow`库，也并不能完好支持剪切板图像的读取。Pillow只能支持windows平台上的剪切板图像读取。

看到这么麻烦，我试图转换思路：
看看能不能用外部程序如命令行等先把剪切板图片保存为本地图片然后再让python来处理。
但是，linux和mac都原生对剪切板图像的支持也不是很好，即使是第三方应用xclip、xsel等建立在x window基础上的应用也很难做到这个简单的东西。
目前在Mac平台上比较好用的相关命令行应用，只有`pngpaste`。方便好用，只是不支持gif和在文件上直接复制来的数据。

还是不够满意，于是再深度搜索和阅读大量的文章、大量的尝试，最后得到Mac上处理剪切板图像的python方案：`PyObjC`库。
`Pyobjc`库是用python实现与Mac电脑基层api连接操作的库，在操作Mac OS底层问题上十分强大。
`pyobjc`中有一个AppKit模块，而Appkit模块中有一个NSPasteboard类，有非常全面的支持剪切板操作的方法支持。
我的Mac系统是Sierra，10.12，在以前安装过xcode的基础上，直接用`pip install pyobjc`即可完成整个库的安装，非常简单。注意：为了怕库太复杂影响系统其他程序操作，所以我打开virtualenv环境，安装在项目里而不是系统里。
安装好后就可以直接在python里面编码了。以下代码改编自[这篇简书文章](https://www.jianshu.com/p/7bd4e6ed99be)：
```python
# pasteboard.py

import os
import time

# 从PyObjC库的AppKit模块引用NSPasteboard主类，和PNG、TIFF的格式类
from AppKit import NSPasteboard, NSPasteboardTypePNG, NSPasteboardTypeTIFF

def get_paste_img_file():
    """
    将剪切板数据保存到本地文件并返回文件路径
    """
    pb = NSPasteboard.generalPasteboard()  # 获取当前系统剪切板数据
    data_type = pb.types()  # 获取剪切板数据的格式类型

    # 根据剪切板数据类型进行处理
    if NSPasteboardTypePNG in data_type:          # PNG处理
        data = pb.dataForType_(NSPasteboardTypePNG)
        filename = 'HELLO_PNG.png'
        filepath = '/tmp/%s' % filename            # 保存文件的路径
        ret = data.writeToFile_atomically_(filepath, False)    # 将剪切板数据保存为文件
        if ret:   # 判断文件写入是否成功
            return filepath
    elif NSPasteboardTypeTIFF in data_type:         #TIFF处理： 一般剪切板里都是这种
        # tiff
        data = pb.dataForType_(NSPasteboardTypeTIFF)
        filename = 'HELLO_TIFF.tiff'
        filepath = '/tmp/%s' % filename
        ret = data.writeToFile_atomically_(filepath, False)
        if ret:
            return filepath
    elif NSPasteboardTypeString in data_type:
        # string todo, recognise url of png & jpg
        pass

if __name__ == '__main__':
    print get_paste_img_file()

```
