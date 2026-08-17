# ❖ Docker Volume 详解 [DRAFT]

[参考：深入理解Docker Volume（一）](http://dockone.io/article/128)

Docker为`容器`声明一个Volume数据存储，有三种方法，达到一样的效果：
- Dockerfile: `Volume: HostPath:ContainerPath`
- docker run: `-v HostPath:ContainerPath`
- docker run: `-volumes-from AnotherContainer`

## 数据容器

创建某容器并读取数据容器：
```sh
$ docker run -d --volumes-from dbdata --name db1 postgres
```

使用数据容器的两个注意点：
- 不要**运行**数据容器，这纯粹是在浪费资源。
- 不要为了数据容器而使用“最小的镜像”，如busybox或scratch，只使用数据库镜像本身就可以了。你已经拥有该镜像，所以并不需要占用额外的空间。


## 访问权限问题
> 如果把Host上文件夹映射到Container里，极有可能涉及权限问题，比如Container里所有者是`root`，但是Host里面这个文件夹的所有者是`guest`，那么就极有可能容器里的app无法正常读写这个文件夹。

所以，必须里外的所有者、权限是一样的。
**最好是从容器里面定义文件夹的权限，而不是从外部。** 如`chown -R www-data:wwwdata .`

[参考：定制ENTRYPOINT自动修改Docker中volume的权限](http://note.qidong.name/2018/01/docker-volume-permission/)


