# Git为每个repo设置不同的用户名
之前讲过在电脑本地文件夹中`~/.gitconfig`文件即可设置本机的通用用户名，用来登录远程。
但我常会把公开代码上传到github，私密代码上传到Bitbucket，所以需要不同的登录名等。
Git其实可以为每个repo设置单独的用户名用来登录远端，像global的用法一样，可以命令行里设置也可以直接在文件里写：
```
$ git config user.name "John Doe"
$ git config user.email johndoe@example.com
```
手动改写文件的话，就位于repo目录中的`.git/config`这个文件。
设置的格式和`~/.gitconfig`完全一样，具体参考git初始配置那篇。
