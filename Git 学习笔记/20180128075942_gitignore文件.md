# .gitignore文件
> 整个项目里面肯定会有这个文件的，用来屏蔽一些文件的记录和上传。比如一些临时文件夹和涉及隐私的文件，就不需要传到github上了。

## 语法
简单说起来就是：
- 直接写一个名字（文件名或文件夹名），它就是被屏蔽的;
- 在名字前加上`!`就是不被屏蔽的，用于屏蔽整个文件夹时却不屏蔽其中的某个文件;
- `#`是注释符号;
- 名字里的`*`会代替名字里不限量的字，如`*.gif`, `test*.html`;
- 直接写文件夹名，只会屏蔽直属于该文件夹的所有文件，但不会屏蔽其子文件夹;
- 文件夹名后加`/`，就会屏蔽其中所有文件和文件夹，包括子文件夹

引用一个[网上文章](https://www.jianshu.com/p/ea6341224e89)的例子：
```gitignore
# 忽略 .a 文件
*.a
# 但否定忽略 lib.a, 尽管已经在前面忽略了 .a 文件
!lib.a
# 仅在当前目录下忽略 TODO 文件， 但不包括子目录下的 subdir/TODO
/TODO
# 忽略 build/ 文件夹下的所有文件
build/
# 忽略 doc/notes.txt, 不包括 doc/server/arch.txt
doc/*.txt
# 忽略所有的 .pdf 文件 在 doc/ directory 下的
doc/**/*.pdf
```
再加一篇网上文章：[彻底理解.gitignore](http://ybin.cc/git/gitignore-syntax/)


## gitignore失效？已经被tracked文件的处理

一般gitignore教程都只会解释，当文件是`untracked`状态下，是怎么被git给ignore掉的。
但是他们很少提到，如果我有些文件已经被tarck了且已经有了commit历史了，怎么去ignore？

比如我有个`settings-local.ini`曾经被提交上去，但是发现这是个只需要本地存在而不想公开的文件，那么怎么ignore它？
如果你试过就知道，不管在`.gitignore`中怎么配置，都屏蔽步不掉它！换了很多种语法都是一样的结果，还以为是自己没写好gitignore。

实际上，要屏蔽已被追踪的文件，需要一步特殊处理：
```sh
$ git rm --cached path/to/file

# or folder
$ git rm -r --cached path/to/folder
```

参考：https://stackoverflow.com/questions/1274057/how-to-make-git-forget-about-a-file-that-was-tracked-but-is-now-in-gitignore

清除掉cache后，git会显示你已删除了这些文件（但实际上本地还存在），然后提交变动。这样git就再也感知不到它的存在了。
