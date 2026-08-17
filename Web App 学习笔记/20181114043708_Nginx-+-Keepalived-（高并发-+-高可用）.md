# Nginx + Keepalived （高并发 + 高可用）

> High Concurrency + High Available

`Nginx`处理**高并发**非常厉害。但是如果承载Nginx本身的服务器突然出了问题，就很没法再继续了。
`Keepalived`则用于建立集群，让Nginx可以同时在多个服务器上运行，一个出问题就切换到另一个，保证服务的**高可用**。


