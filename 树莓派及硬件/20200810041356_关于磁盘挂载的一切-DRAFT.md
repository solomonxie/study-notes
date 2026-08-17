# 关于磁盘挂载的一切 [DRAFT]

四部分：
- 查看所有已连接磁盘 (fdisk)
- 磁盘格式化 (mkfs, file)
- 临时挂载磁盘 (mount)
- 持久挂载磁盘 (fstab)


## 查看已连接磁盘

- List devices
    - `lsblk` list all connected
    - `df -h` list all mounted
    - `sudo fdisk -l`
- List devices by meta-info
    - `ls -l /etc/disk/by-id` list ID
    - `ls -l /etc/disk/by-uuid` list UUID
    - `ls -l /etc/disk/by-partuuid` list partition-uuid
    - `ls -l /etc/disk/by-label` list Label
    - `ls -l /etc/disk/by-path` list path


## 磁盘格式化

- Check Device file system
    `sudo file -s /dev/sda1`
- Format device (Make file system)
    `sudo mkfs -t ext4 /dev/sda1`


## mount 临时挂载磁盘

- Mount all disks defined in fstab
    `sudo mount -a`
- FAT32 disk
    `sudo mount -t vfat /dev/sda1 /udisk`
- NTFS disk
    ```
    sudo apt-get install ntfs-3g
    sudo mount -t ntfs-3g /dev/sda1 /udisk
    ```
- ExFat disk
    ```
    # For Raspberry Pi
    sudo apt-get install exfat-fuse
    # For ubuntu
    sudo apt-get install exfat-utils

    # Mount
    sudo mount -t exfat /dev/sda1 /udisk
    ```



## fstab 持久化磁盘挂载配置

Refer to: https://help.ubuntu.com/community/Fstab

- Forbit auto-mount & build Device->Folder mapping
    `UUID=5B7D-9E47 /udisk exfat noauto 0 0`

