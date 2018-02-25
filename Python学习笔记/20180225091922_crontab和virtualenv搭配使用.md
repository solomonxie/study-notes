# `crontab`和`virtualenv`搭配使用
`crontab`是linux系统下定时执行任务的命令，`virtualenv`是python虚拟环境。
那么，怎么让crontab定时执行某个python脚本时是保证在virtualenv的虚拟环境中运行的呢？
答案是：
~在crontab执行shell命令时，不是用系统默认的python如`python PATH-TO-SCRIPT.py`这样的，而是指定运行虚拟环境中的python，如`~/venv/bin/python PATH-TO-SCRIPT.py`这样的。~
参考[这篇文章](https://stackoverflow.com/questions/4150671/how-to-set-virtualenv-for-a-crontab)。
