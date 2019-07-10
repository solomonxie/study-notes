# Linux创建相对软链接

Refer to: https://unix.stackexchange.com/questions/10370/make-a-symbolic-link-to-a-relative-pathname/10371

如果用比较新的linux版本，就可以使用`relative symbolic link`相对软链接了。
用这个命令可以看到是否支持：
```sh
$ ln --help | grep relative
```

创建软链接方式：
```sh
$ ln -rs /tmp/test/to /tmp/test/from
```
