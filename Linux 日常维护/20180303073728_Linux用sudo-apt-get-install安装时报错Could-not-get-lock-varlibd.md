# Linux用`sudo apt-get install`安装时报错`Could not get lock /var/lib/dpkg/lock` 
之前因为`sudo apt-get install`安装什么东西，然后按键终止掉了安装，结果就一直被锁住。
[解决方案参考文章。](https://askubuntu.com/questions/15433/unable-to-lock-the-administration-directory-var-lib-dpkg-is-another-process)

1. 删除文件锁：`sudo rm /var/lib/dpkg/lock`
2. 然后虽然没有被锁住了，但是还报错误`E: dpkg was interrupted, you must manually run 'sudo dpkg --configure -a' to correct the problem.`
于是按照系统提示的解决方法输入命令，如下：
```shell
sudo dpkg --configure -a
```
3.这时虽然可以启动安装程序了，但是运行到最后往往还是会报这个错误：
```
Errors were encountered while processing:
 cups
 ssl-cert
 sudo
E: Sub-process /usr/bin/dpkg returned an error code (1)
```
尝试了网上无数种apt-get purge, clean, -f install等等等等，都不行。
于是看到了[一篇中文文章](https://www.cnblogs.com/anpengapple/p/5098960.html)两句话解决：
```shell
# 删除锁
sudo rm -r /var/lib/dpkg/info/
sudo rm /var/lib/apt/lists/lock
sudo rm /var/cache/apt/archives/lock
sudo rm /var/lib/dpkg/lock
# 重新配置
sudo mkdir /var/lib/dpkg/info
sudo dpkg --configure -a
```
意思是，主要出错原因在于`/var/lib/dpkg/info/`文件夹，把它备份或删掉就好了，然后再创建一个同名文件夹。
之后`sudo apt-get upgrade`升级试试，一切完好！
