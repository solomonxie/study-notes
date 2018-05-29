# Git merge 合并分支

## 本地分支操作
```sh
# 先切换到主分支（或即将被覆盖的分支）
$ git checkout master

# 将某个指定分支覆盖到当前分支
$ git merge <branch-name>

# 删除之前的分支 (已经没用了)
$ git branch -d <branch-name>
```

## 远程分支操作
本地不管怎么push，如果不指定push的分支的话，远程是没有变化的。
```sh
# 把本地分支更新到远程分支
$ git push origin <branch-name>

# 删除远程分支：语法非常奇怪 但就是这么操作的
$ git push origin <local-branch-name>:<remote-branch-name>
# 如 $ git push origin :dev
```
