#  ❖ Git LFS (Large File Storage) 二进制文档版本控制

一直有对二进制文档版本控制的需求，比如一些修图的文档，图片库什么的。之前不懂，一直在用原生git进行控制，结果原本的2G文件夹，很快变成了4G+。
然后参考了git文档发现，官方是不推荐git进行二进制文档控制的。

然后顺着思路找，发现二进制版本控制是有的，而且是git系统能提供的：`Git LFS`。

Git LFS需要单独下载，看似是独立于git的另一个程序，但其实只是相当于一个git插件的存在。

主要好处有：
- 逻辑变了，运行速度就加快了。

问题：
- 使用了Git LFS后，只不过体积增大问题还是没解决。2G的图片仓库还是会翻倍变成5G+，多出来的全都在`.git/lfs/objects`文件夹中（以前是存在`.git/objects`中）。



[参考Github官方：Git Large File Storage](https://git-lfs.github.com/)


## 安装和初始配置
```sh
# Mac
$ brew install git-lfs
```

初始配置（只需要在第一次安装时配置一次）：
```sh
$ git lfs install
```

## 生成和配置本地项目

到这里，就要进入lfs领域了。需要说明的是，
**其实绝大多数时间里，你都还是在使用原生的git命令。**

我在一开始用时，脑袋非常混乱：到底怎么看待git lfs？另一套程序？还是git的一个指令？
其实都不是，如果非要说的话，把它看出git的一个extension插件，看成一个Filter过滤器更为方便。

现在来说一个典型的Git LFS Workflow流程：
- 打开一个本地文件夹
- `git init` 初始化为git仓库
- `git lfs track` 指定监控的LFS大文件类型
- `git add . && git commit` 正常添加、提交仓库变化
- `git lfs push` 通过lfs优化推送到远程
- 修改一些文件
- `git add . & git commit -m "update"` 正常git流程
- 修改一些文件
- `git add . & git commit -m "update"` 正常git流程
- 修改一些文件
- `git add . & git commit -m "update"` 正常git流程
- `git lfs pull` 通过lfs优化更新本地仓库
- `git lfs push`


实际上，Git LFS在这里的作用是一个Filter，把大文件过滤出来，不对它使用文本的处理方式增大体积，而采用另一套方案处理。
所以你只要一开始建立好filter，后面就不用再管了。

```sh
# 指定监视的文件类型
$ git lfs track "*.jpg"
$ git lfs track "*.png"
$ git lfs track "*.jpeg"
```

## 连接远程仓库

使用的Gitlab来做LFS仓库时，第一次push会出现以下消息：
```
Locking support detected on remote "origin". Consider enabling it with:
  $ git config lfs.https://gitlab.com/jason/test.git/info/lfs.locksverify true
```
然后照着它的提示，输入命令后再push，就没有问题了。

常用的Git LFS远程连接有几项常用方法：
```sh
$ git lfs clone <URL>

$ git lfs pull

$ git lfs push

# 断点续传（GB级别的仓库常用）
$ git lfs fetch
```
这几项至关重要，如果没有加`lfs`三个字的话，效率真的极低。
lfs的远程逻辑完全不同：
比如下载文件的话，不像git原生一个一个下载，lfs是先把所有文件夹、文件名都创建好，然后再把真实所需的文件下载下来。


## 注意事项

### 一定要`git lfs clone`, `git lfs push`和 `git lfs pull`
如果不是使用git lsf指令clone、push、pull的话，git就会按照正常的步骤把**所有文件和所有版本**全部下载下来，对二进制文档来说效率极低。
所以注意这里一定要指定`lfs`!
