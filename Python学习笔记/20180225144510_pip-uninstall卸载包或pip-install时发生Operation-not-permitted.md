# `pip uninstall`卸载包或`pip install`时发生`Operation not permitted`错误
在Mac上，无论是pip uninstall还是`sudo pip uninstall`，都会发生这个错误。
实际上，是Mac装机自带python的固有问题，包括如果不`sudo pip`就不能用的问题，都是这里的原因。
解决方法很简单：
只要`brew reinstall python`就全解决了！
注意，重装python意味着很多之前装的packages包都会丢失，请用`pip freeze requirements.txt`备份。

当然，我目的就是为了清楚所有系统python环境下的包才重装的，结果发现重装python之后还顺便解决了之前的各种权限问题。现在不用sudo也能`pip install`和`pip uninstall`了。
删除了系统python中所有的packages后，感觉轻松了很多。
之后就可以无忧无干扰的在virtualenv下安心编程了。

