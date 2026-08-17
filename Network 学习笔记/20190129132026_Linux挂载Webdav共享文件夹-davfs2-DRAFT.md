# Linux挂载Webdav共享文件夹 (davfs2) [DRAFT]

[参考：Ubuntu 16.04: Install davfs2 for WebDAV client](https://www.hiroom2.com/2017/07/30/ubuntu-1604-davfs2-en/)


需要用到`davfs2`这个程序。

Ubuntu、树莓派安装：
```sh
$ sudo apt install davfs2 -y

# 进入交互
#。。。

# 或者设置默认选项，免交互安装：
cat <<EOF | sudo debconf-set-selections
davfs2 davfs2/suid_file boolean false
EOF
sudo apt install davfs2 -y
```


挂载远程Webdav共享文件夹：
```sh
$ sudo mount -t davfs "地址" /path/to/mount/point/
# 然后进入交互，输入用户名和密码
# ...
# OK完成挂载
```

完成挂载后，就可以像正常访问本地文件夹一样在命令行里操作了。


## 在fstab中设置自动挂载


## 安全的记住密码自动登陆


## davfs2体验

虽然直接把webdav共享文件夹映射为本地磁盘／文件夹用起来很方便，但是缺点也和其它所有把网盘映射为文件系统的程序一样很明显：速度太慢！而且卡顿起来会把整个系统都卡住！别的什么事都做不了。

