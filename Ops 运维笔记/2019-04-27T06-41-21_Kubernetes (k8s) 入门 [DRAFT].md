# Kubernetes (k8s) 入门 [DRAFT]

> 单主机当然没有使用Docker的必要性。

一般企业级应用，必然要涉及多主机，即Cluster集群的部署。
而这种分布式架构，目前几乎必然会用到Docker。

Docker在集群部署上，有以下三种流行的方式：
- Docker官方出品：`docker-swarm` + `docker-machine` + `docker-compose`
- Apache出品：`Mesos` + `Marathon` + `Zookeeper`
- 市场占有率80%的绝对垄断者：`Kubernetes`，简称K8s

"_Kubernetes_"在希腊语中代表舵手，或是飞行员。这也就是为什么在其源码中会出现`飞行员手册式编程`这种东西。Kubernetes是2014年由几位Google工程师创建的开源产品，是真正的新生代，年头很短但势力强劲。它的开发深受Google内部著名的`Borg`大规模集群容器管理系统的影响，直接将它的思路用Go重新实现。也就是说它不是真正的新产物而是有深厚技术和历史基础的，是站在巨人的肩膀上的，所以才能一出事就被市场这么广泛的接受。

> 一句话说明：Kubernetes就是一个集群，把多个主机当成一个主机来用。


## K8s的最小管理单元

在Kubernetes中，能够管理的最小单元就不再是Container容器了，而是一个叫`Pod`的单元，它是一个`"逻辑组件"`。K8s是在这个pod内运行容器。
一个`Pod`内，有多个containers，而这些containers之间可以进行通信，且共享多种资源，如：
- 网络名称空间
- Volume存储卷
- xxx?


但是Pod内的各个容器之间的user等命名空间还是相互隔离的。
