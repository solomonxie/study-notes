# Linux查看文件及文件夹大小
```sh
# 查看某目录或文件的大小(目录的话默认显示里面所有文件的大小)
$ du <file-or-folder>

# 只查看某文件夹自身的总大小("-d  0"代表max depth为0)
$ du -d 0 <folder>

# 指定size单位查看（如k, M, G等）
$ du -d 0 -h <folder>
```
