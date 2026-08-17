# UEFI模式下安装Arch Linux

Arch Linux安装是一种非常愉快的体验，完全不同于网上的谣言：这里什么方便的命令都有，应有尽有。没有眼花缭乱的GUI桌面和鼠标的打扰，只要按照步骤输入命令，很快很快就完成安装了。

- ISO镜像只有600MB左右
- 全程需要联网安装
- 支持直接在命令行下添加EFI分区
- 镜像中直接进入了Arch Linux系统，相当于LiveCD，可以直接体验各种功能

[UEFI模式安装参考Youtube：Arch Linux UEFI step-by-step installation guide](https://www.youtube.com/watch?v=dOXYZ8hKdmc)
[传统模式安装参考Youtube：Installing Arch Linux in less than 10 minutes](https://www.youtube.com/watch?v=GKdPSGb9f5s)

## UEFI模式安装命令

```sh
# 查看所有磁盘挂载情况
$ lsblk

# 查看所有磁盘详情，找到需要安装Linux的磁盘号，如/dev/sdb
$ fdisk -l

# 开始分区表创建／修改，选择磁盘需要修改分区表的磁盘号：
$ cfdisk /dev/sdb

# 选择分区表格式：gdt，因为这个分区表能支持UEFI
# 进入分区表创建：左右键用于下面菜单栏选择，上下键用于列表选择

```
