# ❖ AWS CLI 命令行直接操作AWS控制台

安装（基于Python）：
```sh
$ pip3 install awscli --upgrade --user
```
建议在Virtualenv下安装，因为系统级别安装经过测试经常无法安装上。

如同git和docker，`awscli`分为入口命令和功能命令，入口命令为`aws`，功能命令各自对应一项aws服务。如`aws s3`就是针对S3存储的操作。

[参考官方所有命令：AWS CLI Command Reference](https://docs.aws.amazon.com/cli/latest/index.html)

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

配置好后，就可以直接用`aws xxx`命令操作了。`awscli`会自动根据你的登录信息，到你的账户查询相关的信息。

## `S3 静态对象存储`
[参考官方文档：AWS CLI S3](https://docs.aws.amazon.com/cli/latest/reference/s3/index.html)
[参考官方文档：Using High-Level s3 Commands with the AWS Command Line Interface](https://docs.aws.amazon.com/cli/latest/userguide/using-s3-commands.html)

在`awscli`已经配置好的情况下，直接可以用`aws s3`命令进行一系列的操作：

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

