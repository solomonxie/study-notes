# ❖ Webdav (Apache) 的文件权限问题

Apache的Webdav实现是目前最稳定最完善的，所以这里就只讲Apache版本的问题。

这个实现最主要混淆的地方，就是文件权限问题。即我们默认赋予了webdav共享文件夹`www-data`用户和用户组，这样就导致普通用户没法正常在上面创建文件，必须用sudo才行。
或者我们直接把webdav文件夹权限组设置为`me:me`这样的纯属于本用户的权限，可是会导致网络无法发现或无权读写。

如果再加上是跑在docker容器里的apache版Webdav，那么问题就更复杂一步了：docker里面和host主机上分别怎么对同一个文件夹设置权限组？
尝试了很多种配合组合，都不太满意，总是有问题。

Stackoverflow了一下发现最简单的解决方案：
（如果涉及docker，无需到容器里面改权限，全部在host主机上改即可）
```sh
sudo chown -R YOURNAME:www-data /var/www/webdav
sudo chmod -R g+s /var/www/webdav
```
这种做法是，把webdav文件夹的权限设为`当前用户+www-data组`。然后为组加上`g+s`，这样新创建的文件就会自动刚刚设置的`www-data`组的id了。

> For a directory, g+s overrides the group id that new files and directories will have (it is usually inherited from the creator).
