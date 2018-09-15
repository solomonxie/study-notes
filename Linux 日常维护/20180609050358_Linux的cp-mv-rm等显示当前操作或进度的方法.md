# Linux的cp, mv, rm等显示当前操作或进度的方法

## mv
```sh
# -v参数verbose
$ mv -v ./src/* /tmp
```

## rm
```sh
# -v 和-r参数 注意文件列表太多的话会不执行
$ rm -vr <from> <to>
```

## cp
```sh
# -v 和-r参数 verbose & recursive
$ cp -vr <from> <to>

# 使用rsync命令代替
$ rsync -avP <FROM> <TO>
```
