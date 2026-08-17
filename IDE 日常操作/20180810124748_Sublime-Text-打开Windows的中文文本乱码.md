# Sublime Text 打开Windows的中文文本乱码

众所周知的Windows默认中文编码和Linux/Mac不同，所以所有的Windows上的中文txt文件都会出现乱码。

亲测在Mac上用Sublime/VsCode/Pages/TextEdit/Typora等等，全都不行。

所以在Sublime中试了下，需要安装3个插件才能解决乱码：
- `ConvertToUTF8`
- `GBK`
- `Codecs33`

安装好这三个插件后，重启Sublime，然后打开文本——依然乱码。
需要打开快速面板，输入convert或chiense或gbk等找到相应的命令（忘了-_-)，就转换过来了。
