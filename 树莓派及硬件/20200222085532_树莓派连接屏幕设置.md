## 树莓派连接屏幕设置

所有设置都需要编辑这个文件：`/boot/config.txt`，然后重启。

## 通用显示设置

参考：https://www.jianshu.com/p/a7657245293f

```cfg
# 插线接口：1->HDMI
hdmi_group = 1

# 屏幕分辨率
hdmi_mode=22
```

## 连接HDMI显示器

```cfg
# 屏幕旋转：0->不旋转，1->90度, 2->180度, 3->270度。竖屏的话选3
display_rotate=0
```


## 连接触摸屏

```cfg
# 屏幕旋转：0->不旋转，1->90度, 2->180度, 3->270度。竖屏的话选3
lcd_rotate = 0
```
