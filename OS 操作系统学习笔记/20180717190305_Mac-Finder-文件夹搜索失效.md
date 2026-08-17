# Mac Finder 文件夹搜索失效
在文件夹里怎么搜索都不管用，不出结果。
查了下，原来是`~/Library/Preferences/com.apple.finder.plist`这个文件出了错。

直接把它删除，然后Finder搜索就恢复正常了。

[参考：What to Do When Mac Finder is Slow or Not Responding?](https://www.anysoftwaretools.com/mac-finder-slow-not-working/)
