#  ❖ Git缓冲区理解：index，add和reset，staged和unstaged

> 在git里面，有一个叫`index`的区域，你把东西加到那里叫`add`， 把东西再从哪里撤回来叫`reset`；已经在里面的我们形容它是`staged`，还没有加进去的我们形容它是`unstaged`。

其实`index区`就是一个纯粹的缓冲区，也叫`staging area`，是正式提交之前给我们的一个缓冲，还有犹豫的余地。因为一旦正式commit提交了，你所有还没解决的愚蠢的傻事都会公开，即使能覆盖能撤销，但还是掩藏不了历史。

自己做的话无所谓其实，但是如果是团队合作的话，每次commit都是一次公开。
其实形容的话，就相当于老板让你做个项目，你肯定不可能做了一点东西就跑到老板办公室去送一趟文件，应该会先把做好的放在桌子的上那个小文件架上。然后那个文件架就叫`index`。

[参考：Git 基础 - 撤消操作](https://git-scm.com/book/zh/v1/Git-%E5%9F%BA%E7%A1%80-%E6%92%A4%E6%B6%88%E6%93%8D%E4%BD%9C)

## 撤销add
```sh
# 指定文件
$ git reset HEAD file.txt

# 全部撤销
$ git reset HEAD .
```

## 撤销修改
```sh
# 指定文件
$ git checkout -- file.txt

# 全部撤销
$ git checkout -- .
```

## 删除commit
**一旦commit，就不能撤销！会永远留在历史里面。**

## 修改commit
一般流程如下：
```sh
$ git commit -m '首次提交'

$ git add forgotten_file
$ git commit --amend
```

## 恢复某个文件到以前版本
```sh
# 用git log得知某个版本SHA后，恢复readme.md这个文件
$ git reset <SHA> readme.md

# 切换到该版本
$ git checkout readme.md

# 把变动提交
$ git add . && git commit
```
