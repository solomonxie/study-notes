# ❖ FLask 初接触

> Flask是基于Python的Web后台服务器框架，相对于Django来讲属于非常灵巧的轻量级框架。目前市面上应用程度很广，值得学习一下。

## Installation

- Windows Git Bash

```
pip install virtualenv
mkdir /d/workspace/myFlask
cd /d/workspace/myFlask

virtualenv --no-site-packages venv
source venv/Scripts/activate
# Now is already in virtual enviroment

pip install Flask
```

- Windows CMD

```
# 其他都一样 只有运行不同
venv\Scripts\activate
```

## Deployment

```
touch hello.py
mkdir static
mkdir templates
```

## Hello World

在hello.py中输入以下内容并保存(最简单Flask)

```
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

    if __name__ == '__main__':
        app.run(debug=True)
```

## 运行

```
python hello.py
```

## 渲染模板

在`template`文件夹中新建模板users.html，并随便写几句话，在hello.py中加入如下语句：

```
#记住在前面需要引用渲染函数
from flask import render_template

@app.route('/users/')
def show_users():
    return render_template('users.html') 
```


