# ❖ BeautifulSoup 入门 (Python)

> BeautifulSoup是Python包里最有名的HTML parser分解工具之一。简单易用

## 安装：
```shell
pip install beautifulsoup4
``` 
注意大小写，而且不要安装`BeautifulSoup`，因为`BeautifulSoup`代表3.0，已经停止更新。

## 常用语法
[参考我之前的文章：BeautifulSoup ：一些常用功能的使用和测试](https://www.jianshu.com/p/55fc16eebea4)

```py
# 创建实例
soup = BeautifulSoup(html, 'html5lib')
```

## 选择器
根据不同的网页，选择器的使用会很不同：
- 绝大部分下使用CSS选择器`select()`就足够了
- 如果按照标签属性名查找，而属性名中有`-`等特殊字符，那么就**只能**使用`find()`选择器了。

```py
# 最佳选择器: CSS选择器（返回tag list）
results = soup.select('div[class*=hello_world] ~ div')

for tag in results:
    print(tag.string)       #print the tag's html string
    # print(tag.get_text())     #print its inner text

#单TAG精确选择器：返回单个tag. 
tag = soup.find('div', attrs={'class': 'detail-block'})
print(tag.get_text())

# 多Tag精确选择器: 返回的是text，不是tag
results = soup.find_all('div', attrs={'class': 'detail-block'})

# 多class选择器(标签含有多个Class)，重点是"class*="
results = soup.select('div[class*=hello_world] ~ div')
```

## 获取值
```py
tag = soup.find('a')

# 只获取标签的文本内容
text = tag.get_text()

# 获取标签的全部内容(如<a href='sdfj'> asdfa</a>)
s = tag.string

# 获取标签的属性
link = tag['href']
```

## 修改值
[参考：Beautiful Soup（四）--修改文档树](https://blog.csdn.net/yybmec/article/details/44426081)

```py
tag = soup.find('a', attrs={'class': 'detail-block'})

#修改属性
tag['href'] = 'https://google.com'

# 修改内容 <tag>..</tag>中间的内容
tag.string = 'New Content'

# 删除属性
del tag['class']

```

## 对象类型
在我们使用选择器搜索各类tag标签时，BeautifulSoup会根据使用的函数而返回不同类型的变量。而不同的变量的使用方法也需要注意。

- Tag类型（`<class 'bs4.element.Tag'>`）:
    - `tag.string`
    - `tag.get_text()`
    
- 可遍历字符串类型（`bs4.element.NavigableString`）:
- Comment类型（`<class 'bs4.element.Comment'>`）:

## 增删改标签
[参考：使用BeautifulSoup改变网页内容](https://blog.csdn.net/abclixu123/article/details/39754799)

```py
# 修改标签内容
tag = soup.find('title')
tag.string = 'New Title'
```
