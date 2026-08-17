# Sublime Text Plugin 插件开发

Sublime Text插件是完全基于Python开发的，全部Python开发环境。

插件存储位置：
- Mac：
    - `/Users/YOUR-USER-NAME/Library/Application Support/Sublime Text 3/Installed Packages`
    - `/Users/YOUR-USER-NAME/Library/Application Support/Sublime Text 3/Packages/`
    - `/Users/YOUR-USER-NAME/Library/Application Support/Sublime Text 3/Packages/[YOUR-PACKAGE-NAME]`

你把插件存在以上任意位置，都会被Sublime Text检测到。但是如果在里面嵌套目录的话，就不会被检测到。

> 插件可以是一个单独的`.py`脚本，或者一整个目录。

## Sublime自带的Example
- Select Tools | New Plugin… in the menu.
- Save to Packages/User/hello_world.py.
- Open the Python console (Ctrl+`).
- Type: view.run_command("example") and press enter.

▲ 以上范例，会自动生成一个插件，运行后，就会在当前的文本编辑位置插入一句“hello world”。

标准插件内容：
```py
import sublime, sublime_plugin

# The class name could be ANYTHING.
class ExampleCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        self.view.insert(edit, 0, "Hello, World!")
```
Class名可以是任何名字，只看你调用了。以上`ExampleCommand`，Sublime只会提取`Example`这个词。


## 最简单的的插件架构
```sh
# 打开保存插件的目录：
$ cd /Users/YOUR-USER-NAME/Library/Application Support/Sublime Text 3/Packages/User

# 插件一个插件目录
$ mkdir Hello
$ cd Hello

# 创建插件的默认配置：名字随便起（重要！）
$ touch hello.sublime-commands

# 创建插件脚本（任意名字，只要其中有class定义就会被识别）
$ touch helloworld.py
```

打开`helloworld.py`，我们就可以开始写上面提到的标准class定义，以及其它功能逻辑。
再打开`Default.sublime-commands`文件，注册插件的定义，这样我们就能在`Ctrl+Shift+P`打开面板时候搜索到自己的插件了。

定义内容如下：
```json
[
    {
    "caption": "面板中显示名称",
    "command": "要执行的class名"
    }
]
```
