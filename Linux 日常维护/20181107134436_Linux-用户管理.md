# Linux 用户管理


## 添加新Admin用户

[参考：How to Change Linux User’s Password in One Command Line](https://www.systutorials.com/39549/changing-linux-users-password-in-one-command-line/)

假设我们要添加一个用户`test`:
```sh
# 添加用户
$ sudo adduser test

# 根据交互，填写密码和默认信息
#...

# 将用户添加到sudoer权限组
$ sudo usermod -aG sudo test

# 切换到用户
$ su - test
```


在`root`用户下无交互模式创建新用户`test`：
```sh
useradd  -s /bin/bash test
usermod -aG sudo test
echo -e "test123\ntest123" | passwd test
su - test
```

在本机通过ssh一键添加sudo用户并创建密码：
```sh
ssh root@IP 'useradd  -s /bin/bash test; usermod -aG sudo test; echo -e "test123\ntest123" | passwd test' && echo '[ OK ]'
```

记住，如果是在脚本里面，引号必须用双引号`"`，而不能单引号！
```sh
pass="test123"
echo -e "${pass}\n${pass}" | passwd test
```
