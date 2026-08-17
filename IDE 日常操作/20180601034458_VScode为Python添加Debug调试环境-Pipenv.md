# VScode为Python添加Debug调试环境(Pipenv)
是时候更新virtualenv环境为pipenv环境了，比较方便。但是vscode中配置就麻烦了一点。

[参考：使用VS Code调试Python代码](https://plytools.github.io/2017/04/29/VSCode-Debug-Python/)

还是主要配置这三个文件让python正常的在vscode中达到差错、调试、运行的功能：
- `settings.json` 当前工作环境的所有配置
- `launch.json` 设置python的调试功能
- `tasks.json` 一般用不到。是设置python在vscode中Run运行的配置


## `settings.json`
`settings.json`是vscode管理项目文件夹最重要的配置文件。

需要配置的变量有两个：`python.venvPath`用来指定pipenv存放虚拟环境的文件夹（不是这个repo的bin文件夹）；`python.pythonPath`用来指定具体执行`python`命令的位置。如下所示：
```json
    "python.venvPath": "/Users/Jason/.local/share/virtualenvs",
    "python.pythonPath": "/Users/Jason/.local/share/virtualenvs/repository-QDdBvXzX/bin/python"
```
注意，一般大家经常忽略这点，但是如果没有指定`venvPath`，那么就会弹出这样的错误：
Workspace contains pipfile but attempt to run 'pipenv --venv' failed with Traceback (most recent call last): File "/usr/local/Cellar/pipenv/2018.5.18/libexec/bin/pipenv", line 11, in <module> 

重启软件以后生效。

吐槽下：
这个配置唯一麻烦一点点的就是，不是每个项目文件夹都通用的，因为`python.pythonPath`是需要指明绝对路径的，所以你的每个项目里，都要自己去执行`pipenv --venv`去查询当前项目的虚拟环境的存储位置，然后拷贝到这个settings里来。
如果不喜欢这样，那就干脆在生成pipenv环境时，指定存储位置为当前目录。那么就可以用`./.venv`这样的相对路径来指定位置了。



## `launch.json`
如果没有`launch.json`这个配置文件，vscode就不会自动帮你查错。

生成方法：
如果在项目文件夹中的`.vscode/`中存在这个文件，那么就直接编辑。如果不存在，则需要在vscode的左侧栏的`Debug`栏目中，点击代表`设置`的小按钮，创建一个`launch.json`。然后点击`add configuration`，输入`python`，根据提示创建python相关的配置行。

打开文件以后，主要需要修改的内容如下：
- 找到`pythonPath`变量，可以用两种方式修改其内容：
    - 使用`settings.json`里配置的python位置：`"pythonPath": "${config:python.pythonPath}"`
    - ~指定python的绝对路径~，不推荐。`"pythonPath": "/Users/Jason/.local/share/virtualenvs/test-venv/bin/python"`。

编辑好后，vscode会提示你安装`pylint`的python包，确定后它会自动用`pip install pylint`安装到你指定的python环境里，这样它就可以随时检查你的文件语法错误了。

## `tasks.json`
这个文件是点击菜单中Run按钮时会用到的配置。
里面没有什么具体指定，都是直接调用settings里面的变量值的，像这样`"${config:python.pythonPath}"`。所以不需要什么改动。
