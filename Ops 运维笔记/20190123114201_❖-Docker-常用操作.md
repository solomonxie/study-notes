# ❖ Docker 常用操作

## Docker 基本信息显示

```sh
# 显示当前所有运行的docker
$ docker ps -a

# 显示所有docker对主机系统的占用
$ docker stats
```


## Container容器操作

```sh
# 查看现有容器
$ docker container ls -a

# 容器重命名
$ docker container rename <Name1> <Name2>

# 删除容器
$ docker container rm <ID or Name>

# 运行已有容器 (start + attach)
$ docker start <Name>
$ docker attach <Name>

# 运行已有容器 (start --attach) ====不建议，因为经常出问题，如卡住=====
$ docker start -a <Name>

# 进入已经运行的容器 或 执行命令
$ docker exec -it <Name> <CMD>

# 导出容器为镜像（于docker import相对应，只导出当前状态）
$ docker export -o <Filename.tar> <Container-ID>

# 导出容器为镜像（与docker save相对应，导出所有历史版本）
```

## Image镜像操作

```sh
# 显示所有镜像
$ docker images

# 删除镜像
$ docker image rm <Name or ID>
# 或
$ docker rmi <Name or ID>

# 从镜像生成容器
$ docker run -it <Image Name>

# 下载镜像
$ docker pull <Image Source>

# 导入本地镜像 (导入docker save出来的镜像）
$ docker load -i <Filename>

# 导入本地镜像（导入docker export 出来的镜像）
$ docker import <Filename>

# 为无名镜像创建tag标签
$ docker tag <Name or ID> <Name>:<Tag>
```


## 常见错误

### docker load导入本地镜像时出错
[参考：Error response from daemon: open /var/lib/docker/tmp/docker-import-537484462/repo/.cpt_hardlink_dir_a920e4ddc233afddc9fb53d26c392319/json: no such file or directory](https://github.com/moby/moby/issues/19566)

显示错误：
```
open /var/lib/docker/tmp/docker-import- ... /json: no such file or directory
```

一般要记住：
- 用`docker save`保存出来的镜像，要用`docker load -o <path>`导入
- 用`docker export`保存出来的镜像，要用`docker import <path>`导入

还有，导出镜像时，可以用`.tar`格式。
