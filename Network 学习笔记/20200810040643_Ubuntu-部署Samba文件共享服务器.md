# Ubuntu 部署Samba文件共享服务器

Refer to: https://ubuntu.com/tutorials/install-and-configure-samba#1-overview

```sh
sudo apt install samba -y
mkdir ~/sambashare/
sudo echo [sambashare] >> /etc/samba/smb.conf
sudo echo     comment = Samba on Ubuntu >> /etc/samba/smb.conf
sudo echo     path = /home/solnas/sambashare >> /etc/samba/smb.conf
sudo echo     read only = no >> /etc/samba/smb.conf
sudo echo     browsable = yes >> /etc/samba/smb.conf
sudo service smbd restart
sudo smbpasswd -a solnas
```
