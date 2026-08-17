# 用pdftohtml将PDF转成HTML
`pdftohtml`同样是超强命令行工具集`poppler`的一个子集，和`pdfimages`等优秀的子集一样。用好了是非常便利的。

需要理解的是，`pdftohtml`对`扫描版PDF`是没什么用对。它的主要功能是把pdf中元素全部提取出来，然后按照布局生成HTML。但是扫描版的相当于是一张图片，没有任何元素信息。

Mac上，直接homebrew：
```sh
$ brew install poppler
```
安装好`poppler`工具集后，就可以用`pdftohtml`命令了。

常用命令：
```sh
# 默认输出 (生成多个互相嵌套的html文件，以及多个图片
$ pdftohtml sample.pdf sample.html

# 生成"复杂"排版，其实就是更精确排版的意思 --complex
$ pdftohtml -c sample.pdf sample.html

# 指定第一页至最后一页区间：first-last
$ pdftohtml -f 1 -l 2 sample.pdf sample.html
```

效果：
效果还好，即使是中文的，排版也没有偏离很远。
程序会自动生成很多很多很多的html和图片文件，全都在一个文件夹里面不分类。

