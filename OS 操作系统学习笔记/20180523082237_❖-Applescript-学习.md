# ❖ Applescript 学习

> 之前说到了Automator的局限性，仅限于单一流程简单操作，完全没有条件控制、循环和错误控制等。所以如果希望加入一些控制，那就要掌握applescript。这也是一个很有意思的领域，稍有编程基础的话大概看几眼就能掌握，就算不懂的话大概一天之内就能学明白。

## Applescript特点
- 语法偏原生英语，简单好理解
- 支持对象、函数、条件控制、循环、错误控制等
- 能够操作大量系统底层API，可以运用自如
- 可以直接在Sublime Text里面编辑和运行（需要安装插件）
- 可以直接生成.app应用程序

## 常用语句
### 显示对话框
```applescript
tell current application
    display dialog "Hello World."
end tell
```

### 设置变量
```applescript
set str to "MacOS"
tell current application
    display dialog "Hello " & str
end tell
```

### 清空回收站
```applescript
tell application "Finder"
    empty the trash
end tell
```

### 显示通知框
```applescript
display notification "All graphics have been converted." with title "My Graphic Processing Script" subtitle "Processing is complete." sound name "Frog"
```

### 朗读文字
```applescript
say "Sheet sheel bore"

say "Just what do you think you're doing Dave?" using "Alex" speaking rate 140 pitch 42 modulation 60
```

### 显示剪切板文字
```applescript
display dialog (the clipboard)
```

### 运行shell脚本
```applescript
do shell script "ls -la"
```
