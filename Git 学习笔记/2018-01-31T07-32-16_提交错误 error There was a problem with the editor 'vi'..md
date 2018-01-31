## 提交错误 error: There was a problem with the editor 'vi'.
在Mac上，可能之前重装vim变动了一些设置，所以才会有这个错误，导致git不能提交。
![image](2018-01-31T07-32-16_提交错误 error There was a problem with the editor 'vi'._files/img_01.png)
查了后解决方案很简单，直接输入：
```shell
git config --global core.editor $(which vim)
```
