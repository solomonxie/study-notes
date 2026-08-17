# Linux命令行FTP客户端


## FTP

Ubuntu安装:
```sh
$ sudo apt-get install ftp
```

使用：
```sh
ftp <URL> 

ftp> ls
ftp> cd <path>

# 设置下载至的本地文件夹
ftp> lcd /home/Jason/ftpshare
ftp> get <FILE NAME>
```


## curlftpfs

将FTP映射为本地文件夹，正常操作。

Ubuntu安装：
```sh
$ sudo apt-get install curlftpfs

# 挂载
$ mkdir ~/ftpshare
$ curlftpfs <URL> ~/ftpshare

# 解除挂载
sudo umount ~/ftpshare
```

