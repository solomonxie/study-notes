# ❖ 「AWS S3」 静态对象存储

静态对象存储的意思就是，和FTP差不多，只能上传、下载、删除，不能修改、更新，更不能存动态数据库一类的东西。
虽然还是有很多差别，但是S3和CDN差不多。

为什么不选择可以当硬盘一样随便操作的EBS而是用静态对象存储的S3呢？
- 便宜
- 作为Archive存档还是非常值的
- 作为CDN也是很方便的


## Cost 费用计算

S3一样传承了AWS复杂的Cost Calculation。

每月需要上缴的费用主要是这3部分的总和：
- ⓵ 数据所占的容量：
    - Standard标准版是 $2.5/100GB/mo
    - 低频率IA Standard是$2.4/100GB/mo
    - 最便宜的Glacier是$2.3/100GB/mo
- ⓶ API请求数量:
    - Write写请求(PUT, COPY, POST, or LIST)：Standard标准 $0.05/万次，IA低频率和Glacier $0.1/万次
    - Read读请求(Get and all other requests)：Standard标准 $0.004/万次，IA低频率和Glacier $0.1/万次
    - Delete删除请求：$0 免费
- ⓷ 数据传输费用：
    - 传输到AWS的不相同Region：2 USD/100GB, 
    - 传输到AWS之外的Internet：月内首次1GB $0免费，之后 $9/100GB
    - 传输到AWS相同的Region：$0 免费
    - 外界上传到AWS：$0 免费

几种个人常见案例（月）：
- 标准配置：100GB标准存储 + 1万次读 + 1万次写 + 20G的Internet传输 = $3/mo
- 最低配置：20GB的Glacier存储 + 1万次读 + 1万次写 + 5GB的Internet传输 = $2.5/mo

也就是说，API请求非常便宜，数据传输可以通过EC2内部传输的免费额度来省钱，最贵的是数据存储费用。这样来算，个人直接用Glacier最划算。

其中比较乱的是传输费用。

- 与AWS的EC2等云服务器的传输：
- 与其它云产品（相当于“与Internet互联网”）传输的费用：
- 与AWS的子产品（不包括在AWS中）Lightsail传输的费用：


## Cost 费用优化

[参考：Optimizing Costs for S3](https://www.sumologic.com/aws/s3/s3-cost-optimization/)
[参考：10 Things You Might Not Know About Using S3](https://www.sumologic.com/aws/s3/10-things-might-not-know-using-s3/)



## 创建Bucket

登录AWS进入S3 -> create bucket -> 创建S3全网唯一名称 -> 默认选项 -> 选择公开数据的浏览权限 -> 完成创建Bucket。


过程十分简单，就不截图占地方了。之后都可以修改，填错了也没问题。

下一步：获取`secret_key`，用于之后各种访问。

进入[`官网: Security Credential `](https://console.aws.amazon.com/iam/home?#/security_credential)创建key:
选择左侧User -> 为s3创建专门的用户(IAM) -> 输入名称、密码 -> 成功后，获取这个用户独有的key pair -> 记住key pair。



## awscli：在命令行客户端控制S3

安装客户端（基于Python，强烈推荐Virtualenv中安装）：
```sh
$ pip3 install awscli --upgrade --user
```


配置文件：
AWS CLI的配置文件都存在`~/.aws`目录中，如果没有可以自己创建。具体的每个配置文件，都是`ini`语法，如同git配置文件一样。

登录认证配置：
文件是`~/.aws/credentials`，可以配置多项登录用的key pairs:
```ini
[default]
aws_access_key_id=YourKeyID
aws_secret_access_key=YourSecretCode
```
具体的key pair的值，需要到AWS的权限配置中自己添加IAM账户，然后自动获得key pair。
[`进入官网: IAM - Security Credential `](https://console.aws.amazon.com/iam/home?#/security_credential)


在`awscli`的登录验证已经配置好的情况下，可以直接用`aws s3`命令进行一系列的操作：

```sh
# 列出当前账户下有哪些Bucket
$ aws s3 ls

# 列出指定bucket下有哪些文件
$ aws s3 ls s3://bucket-name/path

# 删除
$ aws s3 rm s3://bucket-name/path/to/file
```

同步本地和远程的文件夹（方向可换）：
```sh
# 
$ aws s3 cp /path/to/local/file s3://bucket-name/path/to/file

# 下载

# 同步
$ aws s3 sync <source> <target> [--options]
```

其中sync同步的选项和网页管理后台中显示的选项一样，有很多需要设置的：
- `--recursive`:
- `--delete`: 删除目标目录中有而源目录中没有的
- `--exclude`: 排除指定的文件和文件夹，语法和`.gitignore`一样很简单
- `--include`: 在排除的文件夹里挑出来包括指定的文件和文件夹同步
- `--storage-class`: 存储类型，可以是`STANDARD`, `STANDARD_IA`, `GLACIER`
- `--acl`:




## 用「s3fs」将S3挂载为本地文件夹 Map S3 as local drive


注意：`Public access`权限必须设置成`Everyone`，要不然无法从各种程序访问。
进入bucket的管理后台，选择`Permissions`，然后设置`Public access`. 

安装工具：
```sh
# MacOS
brew cask install osxfuse
brew install s3fs

# Ubuntu
sudo apt-get install -y s3fs
```

具体步骤参考：https://cloud.netapp.com/blog/amazon-s3-as-a-file-system

```sh
# Change key pairs to yours
echo ACCESS_KEY:SECRET_KEY > ~/.passwd-s3fs
chmod 600 ~/.passwd-s3fs

mkdir ~/s3-drive

# Mount the aws S3 bucket (replace your uid and gid)
s3fs Your-Bucket-Name ~/s3-drive -o umask=0007,uid=1000,gid=1000

# Show all the mounted devices
mount

# Show what's in the bucket
ls ~/s3-drive
```

## 「s3fs」的文件读取权限问题

注意，S3的权限问题十分严格。而且每个文件的权限都有可能不一样。
如果是网页上传的，有可能和本地s3fs上传的权限不同，这样就不能互通操作。但是一旦用`s3fs`上传全部的文件，那么权限就都是统一的。
一旦文件权限没有统一，那么就会在访问时出现`No such file`或`Permission denied`问题。

目前解决方案有两种：
1. 为文件设置Headers，格式是`x-amz-meta-(mode,mtime,uid,gid) `
2. (推荐) 在启动s3fs挂载时，明确指定`umask`, `uid`, `gid`。如`-o umask=0007,uid=1000,gid=1000`

有几点需要注意：
- 因为固定权限问题，所以不要在多台设备同时挂载（因为每个用户权限可能不同）。如果要多台使用，建议统一在一台服务器上挂载，然后在服务器上把文件夹分享为Webdav，其它设备再来访问webdav。

如何修改header: `x-amz-meta-`?
在后台文件管理界面，批量选择文件，然后点Actions，点change metadata，选择`x-ama-meta-`，输入对应value。

## 将S3作为Webdav服务器

搜遍了全网，都没找到靠谱的S3转Webdav服务器方案，差点就自己写Webdav的protocol实现了。还好，经过各种换词搜索，灵机一动，换了种思路：可不可以先把S3映射为本地drive，然后再正常把本地drive共享为webdav？
答案是：可以的。

具体做法就是：用`s3fs`映射到本地文件夹，再用`wsgidav`或apache或nginx将文件夹共享为webdav服务器。
亲测可用，而且十分好用。因为同属AWS资源，同属一个Region区，所以访问速度和访问EBS硬盘感受不到什么区别。
