# Git push报错UNPROTECTED PRIVATE KEY FILE!

```sh
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@         WARNING: UNPROTECTED PRIVATE KEY FILE!          @
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
Permissions 0644 for '/Users/Jason/.ssh/id_rsa' are too open.
It is required that your private key files are NOT accessible by others.
This private key will be ignored.
Load key "/Users/Jason/.ssh/id_rsa": bad permissions
Permission denied (publickey).
fatal: Could not read from remote repository.
```

其实问题是，我拷贝来拷贝去，不小心改变了`~/.ssh`文件夹的权限。所以再把权限改回来就好了：
```sh
$ chmod 0400 ~/.ssh/id_rsa 
```


