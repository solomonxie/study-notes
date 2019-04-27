# Infrastructure as Code (IaC) [DRAFT]

`IaC`是一种**策略**，是DevOps的一种工作策略：即把所有架构性部署操作都变为代码或配置文件，在Git Repo中进行版本管理，然后上线部署、监控等都是根据这些配置文件自动执行的，无需手动敲命令行的命令。

> 这个过程中，最重要的就是用**`Git`**版本控制来管理部署。

所以整个部署过程，不但可以保存历史变动，还能免去记忆一大堆命令，还能自动执行，同时还对其他所有成员透明。每个参与项目的人都能知道整个部署过程是什么。

我们可以用`IaC`来做什么呢？
结合当前Infrastructure流行架构的技术，我们可以把这种"部署即代码"的策略应用在：
- 容器管理
    - Docker compose
    - Kubernetes
- Web Server 部署管理
    - Django
    - Flask
    - Gunicorn
- Configuration 配置管理
