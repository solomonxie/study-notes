# Sublime text 记住上次打开的文件
有些人希望每次关闭Sublime text都自动消除记忆，下次打开时什么都不显示。
但我觉得那样不太方便，尤其在做常用项目都时候。
默认是不显示的，所以我需要让它每次打开都显示上次打开的文件或文件夹。

在菜单里找到`preferences -> Settings-User`，或者mac上直接`cmd+,`，打开用户设置的JSON文件，
加入以下变量内容：
```json
"hot_exit": true
```
保存后即生效。
