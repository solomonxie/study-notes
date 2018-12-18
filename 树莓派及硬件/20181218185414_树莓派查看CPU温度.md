# 树莓派查看CPU温度

无需安装工具即可查看：
```sh
cat /sys/class/thermal/thermal_zone0/temp
>>> 62838
```
显示数字为千分之一度。所以说，除以1000就是当前温度值。

可以设置watch实时观看：
```sh
watch -n 0.1 cat /sys/class/thermal/thermal_zone0/temp
```
