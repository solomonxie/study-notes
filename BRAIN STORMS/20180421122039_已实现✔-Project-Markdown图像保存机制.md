# (已实现✔) Project: Markdown图像保存机制

1. 在任意地方编辑markdown时，图片保存在哪都是个问题，且分享起来很麻烦
2. 统一将图片保存到github中，直接在markdown中引用地址即可在任何地方分享

技术实现：

- [x] 读取系统剪切板中图片（cmd, python, automator, Alfred)
- [x] 转化为本地图片文件 (cmd, automator, Alfred)
- [x] Python读取该图片，转化为base64，通过github api上传，获取raw地址
- [x] 将图片url连接存到系统剪切板中以供编辑markdown

