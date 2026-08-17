# ❖ Jinja2语法学习 （Flask/Django模版引擎）
`副标题：Jinja2 Template Engine`

Flask和Django，以及其它很多Python框架，都默认使用`Jinja2`来作为模版引擎。

在Python中，什么是模版？就是在一个静态HTML加入一些类似变量的标签，然后引擎在渲染这个HTML时候会动态的把变量填入内容，生成一个最终的HTML。
什么是模版引擎？其实就是一种能解析`类似Python语言`的标记语言的解释器。

比如我们在HTML模版中输入一个`<p> {{ post.title }} </p>`，显然这不是真正的HTML语法。但是当Jinja2解释器读取到`{{ ...}}`后知道里面是一个变量，那么就把这个变量替换为真正的值，最后翻译出来就变成了`<p> 大标题 </p>`这样的HTML内容。

**Jinja2是一个模版语言，只是类似Python，比较符合Python语法，但不完全相同！**

所有的模版引擎，实际上都差不多，不管是基于VBS语言的ASP模版，还是基于PHP语言的PHP模版，都不是与原本语言一摸一样，而只是做到尽量一样而已。

## Jinja2语言基础

注意：`Jinja2`模版语言，是不区分缩进的，和纯python不同。实际上所有模版语言都不区分缩紧。

常用标记：
- 注释：`{# 这是注释 #}`
- 变量：`{{ post.title }}`，或字典元素`{{your_dict['key']}}`，或列表`{{your_list[0]}}`
- 多行代码块：`{% 开始 %} HTML标签 {% 结束 %}`

示例：
```jinja2
{% if user %}
    {{ user }}
{% else %}
    hello!
    {% for index in indexs %}
        {{ index }} 
{% endfor %}
```

## Jinja2 Filter 过滤器 (即函数)

一个filter过滤器的本质就是一个function函数。使用格式为：`变量名 | 函数`。
它做到的就是，把变量传给函数，然后再把函数返回值作为这个代码块的值。

如：
```jinja2
<!-- 带参数的 -->
{{变量 | 函数名(*args)}}

<!-- 不带参数可以省略括号 -->
{{变量 | 函数名}}
```

链式调用（管道式）：
和命令行的pipline管道一样，可以一次调用多个函数（过滤器），如：
```jinja2
{{ "hello world" | reverse | upper }}
```

文本块调用（将中间的所有文字都作为变量内容传入到过滤器中）：
```jinja2
{% filter upper %}
    一大堆文字
{% endfilter %}
```

## Jinja2常用内置函数（过滤器）

字符串操作：
```jinja2
safe：禁用转义
<p>{{ '<em>hello</em>' | safe }}</p>

capitalize：把变量值的首字母转成大写，其余字母转小写
<p>{{ 'hello' | capitalize }}</p>

lower：把值转成小写
<p>{{ 'HELLO' | lower }}</p>

upper：把值转成大写
<p>{{ 'hello' | upper }}</p>

title：把值中的每个单词的首字母都转成大写
<p>{{ 'hello' | title }}</p>

reverse：字符串反转
<p>{{ 'olleh' | reverse }}</p>

format：格式化输出
<p>{{ '%s is %d' | format('name',17) }}</p>

striptags：渲染之前把值中所有的HTML标签都删掉
<p>{{ '<em>hello</em>' | striptags }}</p>

truncate: 字符串截断
<p>{{ 'hello every one' | truncate(9)}}</p>
```

列表操作：
```jinja2
first：取第一个元素
<p>{{ [1,2,3,4,5,6] | first }}</p>

last：取最后一个元素
<p>{{ [1,2,3,4,5,6] | last }}</p>

length：获取列表长度
<p>{{ [1,2,3,4,5,6] | length }}</p>

sum：列表求和
<p>{{ [1,2,3,4,5,6] | sum }}</p>

sort：列表排序
<p>{{ [6,2,3,1,5,4] | sort }}</p>
```


## Jinja2 Macro 宏 (自定义函数)

Jinja2是允许自定义函数的，这样在模版中可以重复利用这个自定义函数。Jinja2称之为`Macro`宏。

定义方法：
```jinja2
{% macro 函数名(参数) %}
    具体的HTML内容
{% endmacro %}

<!-- 使用 -->
{{ 函数名(参数) }}

<!-- 或作为过滤器 -->
{{ 变量 | 函数名(参数) }}
```

关于Jinja2自定义函数的`context`上下文和环境变量的问题：
Jinja2的自定义函数“宏”，本身是没法像filter过滤器函数一样使用上下文和环境变量的。
不过可以加上`@contextfilter`装饰器达到同样的效果。


导入另一个文件的自定义函数“宏”：
假设在`macro.html`文件中我们定义了一个函数`func()`。
那么现在我们可以在另一个文件`reference.html`中像python导入模块一样导入它：
```jinja2
{% import 'macro.html' as module %}
{{ module.func() }}
```



## Include 模版引用

Include是我们常用的操作，即定义一个框架模版（父模版），然后一个一个指定性的把子模版引入进来。

框架模版`frame.html`如下：
```jinja2
{% include 'header.html' %}

{% include 'body.html' %}

{% include 'footer.html' %}
```


## Extend 模版继承

我们可以在一个父模版中定义一个`block`代码块，然后在另一个子模版中“继承”这个父模版，并重写这个`block`代码块。
不过一般模版中的父模版，都只是留出一个`block`空位，里面不写东西，特意等子模版来实现。

假设现在有一个父模版`parent.html`：
```jinja2
{% block HEADER %}
    页头部分的HTML内容。
{% endblock HEADER %}

{% block BODY %}
    正文部分的HTML内容。
{% endblock BODY %}

{% block FOOTER %}
    页脚部分的HTML内容。
{% endblock FOOTER %}
```
其中定义了三个block，页头、正文和页脚。

然后我们就可以定义一个模版`child.html`来继承父模版，并且只重写BODY部分：
```jinja2
{% extends 'parent.html' %}
{% block BODY %}
    由子页面重写改写的的HTML内容，替换父页面的BODY。。。
{% endblock BODY %}
```

扩展完成后，我们最终得到的结果是：
```jinja2
{% block HEADER %}
    页头部分的HTML内容。
{% endblock HEADER %}

{% block BODY %}
    由子页面重写改写的的HTML内容，替换父页面的BODY。。。
{% endblock BODY %}

{% block FOOTER %}
    页脚部分的HTML内容。
{% endblock FOOTER %}
```


## Jinja2模版引用Flask路由中的内容

在Flask应用Jinja2模版时，在模版中可以直接调用Flask app中的一些公用变量和方法。

引用Flask的`request`对象：
```jinja2
<p> {{ request.url }} </p>
<p> {{ request.form.get('name') }} </p>
```

引用Flask的`url_for(...)`方法：
```jinja2
<!-- 它会返回我们定义的路由`app.route('/index')`所对应的URL -->
<p> {{ url_for('index') }} </p>

<!-- 它会返回我们定义的路由`app.route('/post/{post_id}')`所对应的URL -->
<p> {{ url_for('post', post_id='127') }} </p>
```

在模版中，我们可以引用`get_flashed_messages()`方法，获取Flask路由传来的`闪现信息`：
```jinja2
{% for msg in get_flashed_messages() %}
    <p> {{ msg }} </p>
{% endfor %}
```
这种闪现信息是从Flask路由中传来的，只要在路由中发一个`flash('hello')`信息，相当于弹了一个`alert()`。然后我们可以在Jinja2的模版中用`get_flashed_messages()`获得flash过来的信息列表。


