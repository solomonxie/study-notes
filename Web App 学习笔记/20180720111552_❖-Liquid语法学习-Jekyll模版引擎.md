# ❖ Liquid语法学习  (Jekyll模版引擎)
`副标题：Liquid Template Engine`

> 学习制作Jekyll模版，其实主要是学习Liquid语法。

参考：[Liquid官方文档。](https://shopify.github.io/liquid/)

就像PHP、ASP、Python等一切网络动态语言一样，`Liquid`也相当于一种独立的动态语言，没什么大差别，基本功能都有。
说白了就是动态生成HTML，可以输出变量，操作数组，调用外部数据，设置IF ELSE判断，FOR循环等，这些都能达到。

开始讲语法前，大概说明一下运行流程：



## 常用变量及属性

[参考：Jekyll 语法简单笔记](http://github.tiankonguse.com/blog/2014/11/10/jekyll-study.html)

### site对象
site对象是全站都能调用的变量，全部都在`_config.yml`文件中定义。
常用变量如下：
- `site.pages`: 所有`_
- `site.posts`: 所有文章
- `site.categories`: 所有的 categories
- `site.tags`: 所有的 tags
- `site.related_posts`: 从`LSI Keywords`提取出来最相关最新的10篇文章
- `site.collections`: 所有集合（与posts逻辑很大不同，一般用来放members等特殊数据）
- `site.documents`: 所有 collections 里面的文档
- `site.data`: `_data` 目录下的数据
- `site.[abc]`: 自定义的变量（手动在`_config.yml`中指定）

### page对象
- `page.content`: 页面的内容
- `page.title`: 标题 （手动在Front Matters中指定）
- `page.excerpt`: 摘要
- `page.url`: 链接
- `page.date`: 时间
- `page.id`: 唯一标示
- `page.categories`: 分类（手动在Front Matters中指定）
- `page.tags`: 标签（手动在Front Matters中指定）
- `page.path`: 源代码位置
- `page.next`: 下一篇文章
- `page.previous`: 上一篇文章

### categories对象
从`site.categories`列表中循环得到的是一个一个的`category`，其中包括这些属性：
- `cat[0]`: 返回`cat`的名称
- `cat[0].size`: 返回这个分类里的文章数量
- `cat[1]`: 返回一个`post_list`列表，包含这个category里所有的post对象。
- `cat[1].size`: 返回这个`post_list`列表中的对象数量。


### tag对象
从`site.tags`列表中循环得到的是一个一个的`tag`，其中包括这些属性：
- `tag[0]`: 返回`tag`的名称
- `tag[0].size`: 返回这个tags里的文章数量
- `tag[1]`: 返回一个`post_list`列表，包含这个tags里所有的post对象。
- `tag[1].size`: 返回这个`post_list`列表中的对象数量。


### paginator对象
- `paginator.per_page`: 每一页的数量
- `paginator.posts`: 这一页的数量
- `paginator.total_posts`: 所有文章的数量
- `paginator.total_pages`: 总的页数
- `paginator.page`: 当前页数
- `paginator.previous_page`: 上一页的页数
- `paginator.previous_page_path`: 上一页的路径
- `paginator.next_page`: 下一页的页数
- `paginator.next_page_path`: 下一页的路径


## 列表读取（各种归档页面用）
### 循环读取Posts
读取全站所有的posts：
```php
{% for post in site.posts %}
    <h2> {{ post.title }} </h2>
    <h2> {{ post.url }} </h2>
    <h2> {{ post.category }} </h2> 
    <h2> {{ post.excerpt }} </h2>  ◀︎ 文章摘要，自动生成的
{% endfor %}
```

只读取`_posts/`文件夹中某个category中的posts，
例如`_posts/tech`文件夹中放的是一些category为`tech`的文章，那么读取方式是：
```php
{% for post in site.categories.tech %}
    <h2> {{ post.title }} </h2>
{% endfor %}
```
注意，在`_posts`中nested文件夹里的文章，也必须在Front matter中指定分类，要不然读不出来。

### 循环读取categories

读取全站所有的分类：
```php
{% for cat in site.categories %}
    <h2> {{ cat[0] }} </h2>
{% endfor %}
```

读取所有分类下的所有文章：
```php
{% for cat in site.categories %}
    {% for post in cat[1] %}
        <h2> {{ post.title }} </h2>
    {% endfor %}
{% endfor %}
```

读取某个分类下所有的文章：
```php
{% for post in site.categories.blog %}
    <h2> {{ post.title }} </h2>
{% endfor %}
```

### 循环读取tags
读取全站所有的tags：
```php
{% for tag in site.tags %}
    <h1> {{ tag[0] }} </h1>
{% endfor %}
```

读取所有tags下的所有文章：
```php
{% for tag in site.tags %}
    {% for post in cat[1] %}
        <h2> {{ post.title }} </h2>
    {% endfor %}
{% endfor %}
```

读取某个tag下所有的文章：
```php
{% for post in site.tags.math %}
    <h2> {{ post.title }} </h2>
{% endfor %}
```

### 读取某category下所有文章并按tag分组读取
```php
{% for post in site.categories.Tech %}   ◀︎ 先读取某分类下所有的文章
     {% assign tags = tags |concat: post.tags |uniq %}   ◀︎ 把每篇文章的tags存到列表里，并删除重复项
{% endfor %}

{% for tag in tags %}
    <h2> {{ tag }} </h2>   ◀︎ 循环输出这个category中的所有tags
    {% for post in site.categories.calculus %}
        {% if post.tags contains tag %}      ◀︎ 循环判断如果文章属于此tag则显示出来
            <h4> {{ post.title }} </h4>
        {% endif %}
    {% endfor %}
{% endfor %}
```


## Post读取
需要在MD文档里指定`layout`才能调用。比如文档里指定了`layout: post`，那么系统就找到`_layouts/post.html`这个文件；如果文档指定了`layout: blog`，那么系统就会找到`_layout/blog.html`这个文件。
在layout里面读取post数据很简单，不需要for循环，不需要if判断，直接用`post`这个对象就行。因为系统已经把文章的数据传过来了。

假如我们在`_posts/xx.md`文章的头信息中，定义了这些数据：
```yml
---
layout: post
title: I'm a post
category: 'blog'
tags: ['jekyll', 'wordpress', 'blog']
---
```
(注：tags列表等，在yaml中可以用`- tag`或`['tag']`表示，一样的 )

以下就是这个`post.html`文件读取post数据的方式：
```php
<h2> {{ post.title }} </h2>
<h2> {{ post.category }} </h2>

<h2> {{ post.content }} </h2>

{% for tag in post.tags %}
    <h2> {{ tag }} </h2>
{% endfor %}
```


## group_by 分组和where_exp条件筛选
官方的`group_by`做到了复杂查询的功能，比如查找某个category下的全部文章并按tag分组显示。
相对自己写`for/if`实现来说，虽然官方提供了这个功能，但是你仔细阅读文档就会发现，这个group_by必须配合单独的**静态的**额外的文档才能实现。
也就是说，你必须手动写个`mygroup.doc`文件，一个一个指定每篇文章的分组、分类、顺序等。
那实在太麻烦了。

[参考官方：Navigation](https://jekyllrb.com/tutorials/navigation/#scenario-8-retrieving-items-based-on-front-matter-properties)
