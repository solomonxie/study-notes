# ❖ Exiftool 命令行操作图片元信息(Megadata)

> Exiftool 是命令行操作exif最强大的工具。

[官方网址。](https://www.sno.phy.queensu.ca/~phil/exiftool/)

[参考：图片EXIF信息查看与Exiftool使用](https://www.jianshu.com/p/d76457799de1)
[参考：如何批量将图片文件名中的时间写入 EXIF 信息？ 知乎](https://www.zhihu.com/question/23692967/answer/25385331)

安装：
```shell
# Mac上安装
$ brew install exiftool

# 或Linux上安装
$ sudo apt-get install exiftool

# 查看图片全部exif信息
$ exiftool 图片位置

# 查看图片某个tag信息
$ exiftool -tag
```

## 语法
每种格式的图片都有自己不同的一堆Tags，比如时间、日期、地理位置等，jpg和png都很不一样。
所以到官网参考每种图片的不同tags，才能确定自己要怎么改这个信息。

[ExifTool Tag Names](https://www.sno.phy.queensu.ca/~phil/exiftool/TagNames/index.html)

注意，引用tag时，要用小写。

基本语法是一样的：
- 设置某tag的值：`-tag=VALUE` 
- 增减某tag值(如果是数字的话)：`-tag+=VALUE` 或`-tag-=VALUE`
- 清空: `-tag=`

```sh
$ exiftool -artist=solomon
```

但是有一点一定要注意：每种tag所接受的值的格式是很严格的：
- 日期
- 时长

## 常用操作
```sh
$ exiftool photo.jpg #查看所有信息
$ exiftool -a -u -g1 photo.jpg #查看所有元信息，包括重复和未知标签，并按小组排列
$ exiftool -s -ImageSize -ExposureTime photo.jpg #查看图片尺寸
$ exiftool -common dir  #查看dir目录文件信息（不仅仅是图片）
$ exiftool -l  c.jpg d.jpg  #从两个图像文件打印所有信息。
$ exiftool -l -canon c.jpg d.jpg  #从两个图像文件打印标准的佳能信息。
```

更改创建和修改时间：
```sh
$ exiftool -gps:all="" photo.jpg  #有些相机会记录拍照时的GPS定位信息。如果你不希望别人看到使用该命令删除gps信息
$ exiftool -all="" photo.jpg  #删除所有信息
$ exiftool -all="" --exif:all photo.jpg  #删除EXIF以外的所有信息
```

写入标签：
```sh
$ exiftool -artist=标签名称 photo.jpg            #写入艺术家标签
$ exiftool -artist=标签名称 a.jpg b.jpg c.jpg   #写多个文件
$ exiftool -artist=标签名称  /exiftoolTest      #写在一个目录的所有文件 exiftoolTest为文件夹
```

转移标签「<」（将某一个标签值赋予另一个标签）：
```sh
# 将文件名（带日期的）设置到图片日期中（程序会自动识别日期格式）
$ exiftool "-DateTimeOriginal<filename" "2009-09-30 15-28-16.jpg"

# 将文件名设置为文件大小（带格式）
$ exiftool "-filename<%f_$imagesize.%e" IMG_0894.JPG
```

其它：
```sh
$ exiftool -Comment='这是一个新的评论'dst.jpg
    向JPG图片写入新评论（取代任何现有评论）。
$ exiftool -comment='' -o newdir -ext jpg
    删除当前目录中所有JPG图像的评论，
    将修改后的图像写入新目录。
$ exiftool -keywords=EXIF -keywords=编辑器 dst.jpg
    用两个新的关键字（“EXIF”和。）替换现有的关键字列表
    “编辑”）。
$ exiftool -Keywords+=单词 -o newfile.jpg src.jpg
    将源图像复制到新文件，然后添加关键字（“单词”）
    当前关键字列表。            
$ exiftool -credit=xxx dir
    从一个目录中的所有文件中删除信用信息，信用值是“xxx”。
$ exiftool -all='' dst.jpg
    从图像中删除所有元信息。注意：你不应该
    对RAW图像（DNG除外）进行处理，因为它是专有的RAW图像
    格式通常包含制造注释中的信息
    转换图像所必需的。
$ exiftool -all='' -comment ='寂寞' dst.jpg
    删除图像中的所有元信息并添加评论
    （注意顺序很重要：“-comment ='lonely'-all =”
    也会删除新评论。）
$ exiftool -all = --jfif：全部dst.jpg
    从图像中删除除JFIF组以外的所有元信息。
$ exiftool -Photoshop：全部= dst.jpg
    从图像中删除Photoshop元信息（注意
    Photoshop信息还包括IPTC）。
$ exiftool -r -XMP-crss：all = DIR
    递归删除a中的图像中的所有XMP-crss信息
    目录。
$ exiftool'-ThumbnailImage <= thumb.jpg'dst.jpg
    从指定的文件中设置缩略图（注意：引号是
    以防止外壳重定向）。
$ exiftool'-JpgFromRaw <=％d％f_JFR.JPG'-ext NEF -r。
    递归地写入以“_JFR.JPG”结尾的文件名的JPEG图像
    添加到扩展名为“.NEF”的类似文件的JpgFromRaw标记中
    当前目录。 （这是“-JpgFromRaw”的倒数
    上面的“READING EXAMPLES”部分的命令）。
$ exiftool -DateTimeOriginal - ='0：0：0 1：30：0'dir
    调整目录“dir”中所有图像的原始日期/时间
    减去1小时30分钟。 （这相当于
    “-DateTimeOriginal- = 1.5”。请参阅Image :: ExifTool :: Shift.pl
    细节。）
$ exiftool -createdate + = 3 -modifydate + = 3 a.jpg b.jpg
    向两个CreateDate和ModifyDate时间戳添加3个小时
    图片。
$ exiftool -AllDates + = 1：30 -if'$ make eq“Canon”'dir
    移动DateTimeOriginal，CreateDate和ModifyDate的值
    将所有佳能影像转换1小时30分钟
    目录。 （AllDates标签作为这些的快捷方式提供
    三个标签，允许他们通过一个标签访问。）
$ exiftool -xmp：city = Kingston image1.jpg image2.nef
    将标签写入两个图像的XMP组。 （没有“xmp：”
    自从“City”存在以后，该标签将被写入IPTC组
    在这两种情况下，IPTC默认是首选。）
$ exiftool -LightSource - ='未知（0）'dst.tiff
    只有在值为0时才删除“LightSource”标签。
$ exiftool -whitebalance- = auto -WhiteBalance = tung dst.jpg
    只有之前为“自动”时，才将“WhiteBalance”设置为“Tungsten”。
$ exiftool -comment- = -comment ='新评论'a.jpg
    只有当图片还没有时才写新评论。
$ exiftool -o％d％f.xmp目录
    为“dir”中的所有图像创建XMP元信息数据文件。
$ exiftool -o test.xmp -owner = Phil -title ='XMP File'
    仅从命令中定义的标签创建XMP数据文件
    线。
```

## 常用标签名(Tags)
> 因为编辑exif信息需要知道图片里内置的各种标签名才能修改，所以下面为标签名参考。

### JPEG
- `Comment`: 描述，无字数限制。

### PNG
- `Comment`: 描述，无字数限制。
- `Description`：描述，无字数限制。


