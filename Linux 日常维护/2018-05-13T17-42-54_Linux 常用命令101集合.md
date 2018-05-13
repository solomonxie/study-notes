# Linux 常用命令101集合

## `mv`

### 移动多文件
[参考。](https://askubuntu.com/questions/214560/how-to-move-multiple-files-at-once-to-a-specific-destination-directory)
```shell
# 移动指定的多文件 (最后一个即终点)
mv file1 file2 file3 DESTINATION

# 根据查找结果移动多文件
mv  `ls|grep IDENTIFIER` DESTINATION
# or
mv *.doc /path/to/dest/folder/
```

### 重命名文件、文件夹
```shell
# 重命名文件夹
mv old_folder_name new_folder_name

# 重命名文件
mv old_file_name new_file_name
```
