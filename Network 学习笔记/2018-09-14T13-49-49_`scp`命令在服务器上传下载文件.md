# `scp`命令在服务器上传下载文件

```shell
#Copy a local file to a remote host:
scp path/to/local_file remote_host:path/to/remote_file

#Copy a file from a remote host to a local folder:
scp remote_host:path/to/remote_file path/to/local_dir

#Recursively copy the contents of a directory from a remote host to a local directory:
scp -r remote_host:path/to/remote_dir path/to/local_dir
```
