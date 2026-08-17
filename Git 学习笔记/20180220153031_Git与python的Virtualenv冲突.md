# Git与python的Virtualenv冲突
如果在git仓库中使用了virtualenv，那么每当使用`git add .`或者`git commit`都会遇到错误，使得不能继续。问题就在于virtualenv对它的冲突。
目前简单的解决办法就是在`.gitignore`中把所有virtualenv相关的文件都屏蔽，一般包括`.Python`,`lib`,`include`,`bin`。
