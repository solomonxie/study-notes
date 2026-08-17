# 利用命令行工具`pdfimages`来提取PDF中的图片
`pdfimages`是一个非常简便好用的PDF图片提取工具，很简单的一个命令就可以提取出PDF指定页面里的所有图片。但是，

注意：
`pdfimages`只能`提取`PDF中的图片，和`imagemagick`的`生成`图片有本质上的不同！也就是说，如果PDF中的内容不是图片的话，那么就提取不出来。

安装：
`pdfimage`是`poppler-utils`工具的一个子集，所以需要安装`poppler-utils`或`poppler`才能使用。Mac上，直接homebrew：
```sh
$ brew install poppler
```

安装好后就可以用`pdfimages`命令了，用法如下：
```sh
# 提取出来的图片保存为默认的. ppm格式文件 (图片文件巨大，会比pdf文件大23倍左右）
$ pdfimages sample.pdf img_name

# 设定提取的图片保存为png格式 (图片大小是3倍左右）
$ pdfimages -png sample.pdf img_name

# 提取某一页的图片 (last one page)
$ pdfimages -l 3 sample.pdf img_name

# 提取前几页的图片(first number of pages)
$ pdfimages -f 2 sample.pdf img_name
```

提取的图片，会按照指定的位置和名字生成如`img_name-000.jpg, img_name-001.jpg, img_name-002.jpg`这样的文件，每一个图片都对应着PDF中原始的图片。

如果没有图片，则不输出。
