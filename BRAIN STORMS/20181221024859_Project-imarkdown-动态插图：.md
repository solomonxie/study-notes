# Project: imarkdown 动态插图：
如果做不到github issues上传过程中多个图片的placeholder都是同名且自动将placeholder换为图片网址、保持多个图片顺序，
那么就简单给placeholder文字中加序号，上传成功后只要在文本框中替换这行文字即可。


vim或其它编辑器插件的沟通流程：
- 假设主要处理上传并返回网络图片地址的脚本为python制作，名为img2github
- 那么触发上传功能时（如输入命令），
- 插件先检查现有文本中是否有其它placeholder，然后决定index，（也是在这一步决定同时上传的上限，超过上限则不进行下一步）
- 插件在文本当前光标处插入一个带index的placeholder，
- 插件触发img2github，并告知index (python -m img2github.py —index 2）
- 脚本自动读取系统剪切板
- 脚本组织内容并上传到github
- 脚本返回上传成功的图片地址和index (2:https://......）
- 插件触发另一个python文字处理脚本，将当前全部文字传给它，
- 第二脚本将文本中，对应index的placeholder替换为图片链接地址
- 第二脚本返回处理后的文字
- 插件将全部文字替换到当前位置


Sublime Text直接用python写插件，无需import导入包，非常方便

vim需要学一下vim plugin流程和vim脚本

windows一般软件的话，简单用AHK脚本记录触发命令时候的文本编辑器，然后触发python脚本，并在上传完成后切换到之前的程序中执行文字替换即可。


Mac上一般app，需要用applescript，触发命令时记住当前app，然后执行python脚本，再切换回之前的app，执行文字替换。
