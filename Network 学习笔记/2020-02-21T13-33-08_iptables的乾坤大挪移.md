# iptables的乾坤大挪移


## 流量转发、端口转发——俗称NAT，翻译为乾坤大挪移

参考：https://github.com/shadowsocks/shadowsocks/wiki/Setup-a-Shadowsocks-relay

```sh
 sudo su
 echo 1 > /proc/sys/net/ipv4/ip_forward
 iptables -t nat -A PREROUTING -p tcp --dport 8388 -j DNAT --to-destination US_VPS_IP:8388
 iptables -t nat -A POSTROUTING -p tcp -d US_VPS_IP --dport 8388 -j SNAT --to-source JAPAN_VPS_IP
```


## 备份／恢复iptables设置

参考：https://upcloud.com/community/tutorials/configure-iptables-centos/

```sh
sudo su
iptables-save > /etc/iptables-rules
iptables-restore < /etc/iptables-rules
```
