# VPS分区测速 [DRAFT]

## 主要方法
```sh
# 直接Ping
$ sudo ping -c 10 -i 10000 SERVERIP:Port 

# iPerf（需要服务端运行"iperf -s"，并开放相应端口）
$ iperf -c <IP>

# SSH 连接
$ time ssh ubuntu@IP exit

# 上传下载文件（文件是1M)
$ time scp ~/scptest ubuntu@IP:~/
$ time scp ubuntu@IP:~/scptest ~/

# Youtube下载（5M）
$ time youtube-dl --no-continue --proxy "localhost:1080" -f best,mp4 -o ~/speedtest "https://youtu.be/TO9TS4aGWL4"
```

## 期望值

**Local Average Speed**:
- Ping:
    - Local -> Local: 0.008ms
    - Local -> Router: 5ms
    - Local -> Baidu: 10ms
    - Local -> bilibili: 50ms
    - Local -> iQiyi: 15ms
- Video downloading:
    - Local <- iQiyi: 400 KB/S

**Cross Region Expected Speed**:
- Ping: 
    - Local -> Remote: 100 ms
    - Remote -> Google: 2ms
    - Remote -> Youtube: 2ms
- Youtube downloading: 
    - Remote -> Local: 400-1000 KB/S
    - Remote <- Youtube: 50-100 MB/S

## `AWS` (Amazon Web Service)

### `Singapore (ap-southeast-1)`

- Ping:
    - Local -> Remote: 216ms
- Youtube Downloading: 
    - Remote -> Local: 220 k/s


### `Virginia (us-east-1)`
```

```

### `Ohio (us-east-2)`
```

```
