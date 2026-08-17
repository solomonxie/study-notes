# ❖ 操作系统安装及启动原理详解 [DRAFT]

涉及术语：
- BIOS vs. UEFI
- CMOS
- MBR or GPT
- Grub & Grub2


## 电脑启动流程 BOOT PROCESS

简而言之：
打开电源 -> 主板通电 -> 主板上的BIOS芯片启动 -> BIOS检查所有硬件连接正常 -> BIOS去找硬盘 -> 找到第一块硬盘(或者自己在BIOS里设置的任何其它盘) -> 找到存在这个硬盘上第一块区域的的分区表(MBR) -> 然后找到分区下的Grub（bootmgr启动管理器）-> 然后


## 硬件层面 HARD WARES

### BIOS

BIOS迷你系统是存在一个叫`BIOS Chip`的小芯片上，里面“刻录”了一个只读的小系统，用来控制在通电后如何启动OS操作系统。


### CMOS

由于BIOS是没有保存Settings设定功能，每次重启就忘记了设置，所以加了一块能保存设置信息的`CMOS chip`芯片，这样每次重启后还能保持BIOS设置信息。
但是CMOS必须要有电才能保存，所以主板上有一块圆圆的“手表电池”，就是只为了CMOS使用的。一旦把电池拔下来，那么保存的BIOS设置就都恢复出厂值了。



### 分区表 PARTITION TABLE

- `MBR` (Master Boot Record): 所有老式主板所支持的分区表。不支持2TB以上硬盘。不能创建EFI分区。
- `GPT` (**GUID** Partition Table): 新式UEFI主板所必须的分区表。


### 分区格式 PARTITION FORMAT

- **EFI格式分区**: 也称为`ESP` (EFI System Partition)。 是用来启动UEFI主板上磁盘用的分区格式。
- ExtFat: 能同时被Linux、Windows支持。适合作为两种操作系统间共享文件的磁盘格式。
- Ext4: Linux主流分区格式，在Windows不支持。
- Fat32: 能同时被Windows、Linux默认支持。不支持存储4GB以上文件。
- NTFS: Windows主流分区格式，Linux默认不支持。


## 软件层面 SOFTWARES


