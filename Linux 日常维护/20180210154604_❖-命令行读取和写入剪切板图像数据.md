# ❖ 命令行读取和写入剪切板图像数据

目前剪切板的操作原生支持还不是很完善，windows/mac/linux的工具都不一样，而且如果不是自己写脚本的话很难原生支持剪切板里的图片读取和写入。

## Mac 自带pbcopy和pbpaste
```shell
# 写入剪切板
$ echo 'hihihi' | pbcopy
#或
$ pbcopy < echo 'hello'

# 读取剪切板
$ pbpaste
# 保存剪切板内容到文件
$ pbpaste > ~/test.txt
```

## Mac处理剪切板图像

目前没有原生支持剪切板的文字之外的类型。所以必须要下载第三方应用。


## "pngpaste" 最简单的剪切板图像转文件工具

[参考`pngpaste`](https://github.com/jcsalterego/pngpaste)

mac上直接`brew install pngpaste`，完成后一句`pngpaste path-to-img.png`即可在指定位置生成图片文件。没有特别option选项，仅此一句。
经过测试，能支持截图软件、浏览器、mac图片预览等的右键点击copy得来的常用图像。
官方的图像类型支持说明：
Supported input formats are `PNG, PDF, GIF, TIF, JPEG`.
Supported output formats are `PNG, GIF, JPEG, TIFF`.
Output formats are determined by the provided filename extension, falling back to PNG.
It's unclear if EXIF data in JPEG sources are preserved. There's an issue with pasting into JPEG format from a GIF source.

但是：
- 不支持直接在文件上`ctrl+c`这样拷贝来的图片
- 不支持gif，实测

## Linux上的"xclip"

原本是在linux常用的剪切板操控工具，后来可能流行起来在mac也支持了。但是mac上安装要麻烦点，必须要先安装依赖工具：`X11`即`XQuartz`，200M的安装文件，装完了还要重启mac电脑才行。不过为了剪切板的事，忍了。[安装地址在这](https://www.xquartz.org/)。下载好dmg文件安装就行了。
安装好后，用`brew install xclip`即可轻松装好。
但是！！！
装好才发现，xclip并没有和系统剪切板沟通，而只是在自己程序里的一些缓存。而且而且而且！每次在命令行里用xclip，还都会在桌面启动`XQuartz`这个app，还不会自动关闭。实在太不爽了这种设置。
另外，所有这些x开头的剪切板程序，都是建立在`X Windows`基础上的，即刚刚安装的XQuartz。[wiki这里有一个列表](https://en.wikipedia.org/wiki/X_Window_selection#Programs)，所有xsel、xclip等等都是这样的。。。
难道mac和linux的小小剪切板就这么难操作吗？

