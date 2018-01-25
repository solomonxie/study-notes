## Ubuntu中无法激活中文输入法问题

```shell
# 新建`.xprofile`文件并编辑
sudo vim /home/.xprofile
# 然后输入并保存
export LC_ALL=zh_CN.utf8 
export XMODIFIERS=@im=fcitx 
export QT_IM_MODULE=xim 
export GTK_IM_MODULE=xim 
fcitx -d
```
