# 两台服务器主机之间测速 [DRAFT]

有很多种方法：

## iPerf命令 测试带宽

> iPerf是跨平台的工具，Linux/Unix平台都能很简单就安装好了。

具体做法就是：在服务器上运行iperf，在本地也运行iperf，然后测出两者之间的带宽。


```sh
# 服务器端(18.191.36.156), 监听5001端口，等待客户端
$ iperf -s -L 5001
>> Server listening on TCP port 5001

# 客户端
$ iperf -c -p 5001 18.191.36.156
>> [ ID] Interval       Transfer     Bandwidth
   [  4]  0.0- 1.0 sec   384 KBytes  3.15 Mbits/sec
```

详细测试：
```sh
# 服务器端(18.191.36.156), 监听5001端口，等待客户端
$ iperf -s -u -L 5001
>> Server listening on TCP port 5001

# 客户端 (指定带宽-b 100M，测试-t 30秒， 间隔-i 1秒，用UDP传输-u)
$ iperf -u -b 100M -t 30 -i 1 -p 5001 -c 18.191.36.156
>> [ ID] Interval       Transfer     Bandwidth
   [  4]  0.0- 1.0 sec  12.5 MBytes   105 Mbits/sec
```
