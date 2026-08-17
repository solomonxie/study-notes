# ❖ 利用Sphinx+Github+Readthedocs+Rst快速创建规范文档 [DRAFT]

> 注意：这个服务的文档不能用Markdown，只能用reStructuredText.

虽然比较像Jekyll，是快速建站类服务，但是是完全不同的逻辑和构建思维。
这个方式是快速建立一本书、一份完整文档、一个规范攻略的方式，与github和Readthedocs结合非常棒。

大概运行逻辑是：
- 本地运行Sphinx生成项目文件夹和基本构成文件
- 上传到Github专门的repo仓库
- 在这个repo中的settting设置添加与Readthedocs关联的服务
- 到Readthedocs添加这个repo的地址，并开启关联
- Readthedocs定期（大概每分钟）扫描repo并在远程执行生成命令，更新文档

## 安装配置

Sphinx是基于Python构建的，所以一般在各个平台直接用pip安装最方便：
```sh
# 建议在虚拟环境里安装
$ pip install sphinx --user

# 创建项目文件夹
$ mkdir test
$ cd test

# 生成项目结构
$ python -m sphinx-quickstart
```

在执行`sphinx-quickstart`后，会进入十几二十个问题选择环节，可以一直按回车选择默认选项，但是前几项一定要认真自己选择，要不然很麻烦：
```sh
$ python -m sphinx.quickstart

Welcome to the Sphinx 1.7.6 quickstart utility.

Please enter values for the following settings (just press Enter to
accept a default value, if one is given in brackets).

Selected root path: .

You have two options for placing the build directory for Sphinx output.
Either, you use a directory "_build" within the root path, or you separate
"source" and "build" directories within the root path.
> Separate source and build directories (y/n) [n]: y

Inside the root directory, two more directories will be created; "_templates"
for custom HTML templates and "_static" for custom stylesheets and other static
files. You can enter another prefix (such as ".") to replace the underscore.
> Name prefix for templates and static dir [_]: .

The project name will occur in several places in the built documentation.
> Project name: testtest
> Author name(s): Solomon
> Project release []: 0.01

If the documents are to be written in a language other than English,
you can select a language here by its language code. Sphinx will then
translate text that it generates into that language.

For a list of supported codes, see
http://sphinx-doc.org/config.html#confval-language.
> Project language [en]: en

The file name suffix for source files. Commonly, this is either ".txt"
or ".rst".  Only files with this suffix are considered documents.
> Source file suffix [.rst]: .rst

One document is special in that it is considered the top node of the
"contents tree", that is, it is the root of the hierarchical structure
of the documents. Normally, this is "index", but if your "index"
document is a custom template, you can also set this to another filename.
> Name of your master document (without suffix) [index]: index

Sphinx can also add configuration for epub output:
> Do you want to use the epub builder (y/n) [n]: n
Indicate which of the following Sphinx extensions should be enabled:
> autodoc: automatically insert docstrings from modules (y/n) [n]: n
> doctest: automatically test code snippets in doctest blocks (y/n) [n]:
> intersphinx: link between Sphinx documentation of different projects (y/n) [n]:
> todo: write "todo" entries that can be shown or hidden on build (y/n) [n]:
> coverage: checks for documentation coverage (y/n) [n]:
> imgmath: include math, rendered as PNG or SVG images (y/n) [n]:
> mathjax: include math, rendered in the browser by MathJax (y/n) [n]:
> ifconfig: conditional inclusion of content based on config values (y/n) [n]:
> viewcode: include links to the source code of documented Python objects (y/n) [n]:
> githubpages: create .nojekyll file to publish the document on GitHub pages (y/n) [n]:

A Makefile and a Windows command file can be generated for you so that you
only have to run e.g. `make html' instead of invoking sphinx-build
directly.
> Create Makefile? (y/n) [y]:
> Create Windows command file? (y/n) [y]:
```

