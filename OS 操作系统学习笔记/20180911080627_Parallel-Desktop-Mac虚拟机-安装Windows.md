# Parallel Desktop (Mac虚拟机) 安装Windows


## 安装Ghost版Win7系统

![image](20180911080627_Parallel-Desktop-Mac虚拟机-安装Windows_files/img_01.png)

![image](20180911080627_Parallel-Desktop-Mac虚拟机-安装Windows_files/img_02.png)

![image](20180911080627_Parallel-Desktop-Mac虚拟机-安装Windows_files/img_03.png)

无法检测到系统没关系，可以自己手动选：

![image](20180911080627_Parallel-Desktop-Mac虚拟机-安装Windows_files/img_04.png)

![image](20180911080627_Parallel-Desktop-Mac虚拟机-安装Windows_files/img_05.png)



![image](20180911080627_Parallel-Desktop-Mac虚拟机-安装Windows_files/img_06.png)


设置自己想要的硬件等配置：

![image](20180911080627_Parallel-Desktop-Mac虚拟机-安装Windows_files/img_07.png)


![image](20180911080627_Parallel-Desktop-Mac虚拟机-安装Windows_files/img_08.png)


记得调整好开机的读取顺序，相当于设置主机的BIOS了：

![image](20180911080627_Parallel-Desktop-Mac虚拟机-安装Windows_files/img_09.png)


开始正常安装：

![image](20180911080627_Parallel-Desktop-Mac虚拟机-安装Windows_files/img_10.png)


进入了光盘或USB的安装界面，选择WinPE系统：

![image](20180911080627_Parallel-Desktop-Mac虚拟机-安装Windows_files/img_11.png)


进到WinPE系统中会看到，本地没有磁盘。
实际上是虚拟机分配了，但没有格式化的原因。
打开分区软件，手动格式化：

![image](20180911080627_Parallel-Desktop-Mac虚拟机-安装Windows_files/img_12.png)

之后就是常规的Ghost安装了。

![image](20180911080627_Parallel-Desktop-Mac虚拟机-安装Windows_files/img_13.png)



## 安装正常安装版Win7系统

直接连接ISO光盘文件，正常安装，比Ghost简单的多。



## Reclaim
安装好后，肯定有很多不喜欢的软件，比如Office等。
想方设法把不需要用的软件全部删除，然后用电脑管理软件如模仿、360安全卫士等，清除各种缓存、没用的东西。
然后磁盘会减少几个G的空间，这时候STOP虚拟机，然后在控制页面里面选择`Reclaim`，就可以给U盘节省几个G的空间了。
