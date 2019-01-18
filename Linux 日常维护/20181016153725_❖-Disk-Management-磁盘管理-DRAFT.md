# ❖ Disk Management 磁盘管理 [DRAFT]


## Badblocks 坏道修复

坏道检查命令`/sbin/badblocks`：
```sh
# 检测并输出坏道信息（信息等下会被用到）
$ sudo badblocks -v /dev/sda > badsectors.txt

# 根据坏道信息进行修复
# ------------ 针对 for ext2/ext3/ext4 文件系统 ------------
$ sudo e2fsck -l badsectors.txt /dev/sda
#或
# ------------ 针对其它文件系统 ------------
$ sudo fsck -l badsectors.txt /dev/sda
```

cron任务定期坏道检查，编辑`/etc/cron.d/badblocks`文件：
```sh
30 4 * * 3 root [ -x /sbin/badblocks ] && [ $(date +\%d) -le 7 ] && /sbin/badblocks /dev/sda
```



## 空白硬盘分区、格式化

主要执行的命令顺序为：`lsblk`查看已连接硬盘 -> `file`查看硬盘是否格式化 -> `fdisk`分区 -> `mkfs`格式化

Ubuntu系下：
```sh
# 查看添加的网盘名称和地址(如/dev/sda)
$ lsblk

# 查看网盘的文件系统状况（是否格式化了）
$ sudo file -s /dev/sda

# 最好先检查和修复坏道后再操作
# ......

# 分区 (进入交互shell）
$ sudo fdisk /dev/sda
# 创建一个或几个分区，根据提示很容易搞定
# ....
# 保存分区表
：w

# 用不同的格式来格式化每个分区（不要在fdisk里面格式化）
$ sudo mkfs -t exfat /dev/sda1
$ sudo mkfs -t ntfs /dev/sda2
```

Mac终端下：
```sh

```
