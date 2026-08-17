# Docker 删除无名镜像

```sh
$ docker images
REPOSITORY                                                    TAG                 IMAGE ID            CREATED             SIZE
<none>                                                        <none>              5b021d7fb1c2        10 minutes ago      453MB
<none>                                                        <none>              b6fd958aee66        13 minutes ago      453MB
<none>                                                        <none>              066450d8f9f6        14 minutes ago      545MB
<none>                                                        <none>              6e3e8c5dc3ce        17 minutes ago      453MB
<none>                                                        <none>              2d7ab2f16ba8        20 minutes ago      545MB
```

很多这种创建不成功的镜像很占地方，所以一口气删除它们：
```sh
$ docker images --filter "dangling=true" -q |xargs docker rmi
```

[参考：Docker Images Filtering](https://docs.docker.com/engine/reference/commandline/images/#filtering)



```sh
$ docker images --format  "{{.ID}}:{{.Repository}}"
77af4d6b9913: <none>
b6fa739cedf5: committ
78a85c484f71: <none>
30557a29d5ab: docker
5ed6274db6ce: <none>
746b819f315e: postgres
746b819f315e: postgres
746b819f315e: postgres

$ docker images --format  "{{.ID}}: {{.Repository}}" | grep "none" |cut -d ':' -f 1
77af4d6b9913: <none>
78a85c484f71: <none>
5ed6274db6ce: <none>
```
