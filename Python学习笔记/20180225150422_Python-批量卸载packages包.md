# Python 批量卸载packages包
不像`pip install -r requirements.txt`可以批量安装包，卸载就没有原生方法了，需要用巧劲。
目前Stackoverflow有这么一种用法：
`pip freeze | grep pyobjc-framework | xargs pip uninstall -y`
其中`pyobjc-framework` 是搜索关键字，搜索包含这些字的包然后批量卸载。
如果不是指定某些关键字，直接`pip freeze | xargs pip uninstall -y`，那么就是卸载所有的包了。
不出所料的话，应该是执行不了的，总有哪个包的卸载会出错，然后中断进程。

如果想达到`恢复出厂设置`的感觉，那么直接类似`brew reinstall python`这样的重装python就可以了罢。不过我再重装后，虽然很多删掉了，但还是会有些遗留，需要手动清除。

