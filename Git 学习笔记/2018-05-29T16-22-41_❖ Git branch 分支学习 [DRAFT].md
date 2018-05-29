#  ❖ Git branch 分支学习 [DRAFT]

## 新建分支
```sh
$ git checkout <new-branch-name>

# 以上一句话等同于以下两句话：
$ git branch <new-branch-name>
$ git checkout <new-branch-name>
```

## 不同分支的修改状况
- 如果在一个分支进行修改，而没有`add`和`commit`，那么即使另一个分支，文件也一样是改变了的。
- 如果修改后commit了，那么切换分支时，则会体现出不同。


## 分支间拷贝文件 Copy files between Git branches

1. use the git show command:
```sh
$ git show <branch_name>:path/to/file > /path/to/local/file
```

2. use the git checkout command:
```sh
$ git checkout <branch_name> path/to/new/file

# 如：将master分支的abc目录下所有文件克隆到本分支内
$ git checkout master:abc/ -- .
```

## 从远程克隆所有分支
默认`git clone`只会下载master分支，想要下载所有分支，网上众说纷纭，而且很复杂，连写bash脚本的都有。
总算找到一个简单且合理可用的：
```sh
# 删除原先的.git
mv /path/to/repo/.git /tmp/

# 下载包含所有branches的.git
git clone --mirror <URL> /path/to/repo/.git

# 进入目录
cd /path/to/repo/

# 重新初始化
git init

# 取消自动add的文件
git reset HEAD .
```
