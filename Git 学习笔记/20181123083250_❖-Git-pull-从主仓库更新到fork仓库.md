#  ❖ Git pull 从主仓库更新到fork仓库


当我fork了一个人的repo后发现，我不能简单的`git pull`来自于源仓库的更新，只是在我自己的repo中玩耍。
搜索了一下发现，需要先把源仓库的remote端加入进来，才能pull。

假设源仓库是`git@github.com:yychuyu/LeetCode.git`，而我fork后的仓库是`git@github.com:solomonxie/LeetCode.git`。

```sh
# 添加源仓库的remote地址，相较于自己的远端名字"origin"，给它任意起个名字："source"
git remote add source git@github.com:yychuyu/LeetCode.git

# 指定pull自源仓库的master分支
git pull source master

# 下载更新后自动会然后进入commit提交页面
# commit更新
# 修改有conflict的文件，然后再次commit
# ...

# 将本地的更新push到自己的remote
git push origin master
```

记住，添加了源仓库的remote后，只能pull而不能push，因为没有权限。这时候需要到github网页上，提交`pull request`，然后等待源分支的主人允许合并。


`pull`方法其实是不推荐的，因为会自动覆盖当前分支，产生冲突。还有另一种`fetch`方法，把更新下载到本地后，我们可以为它创建一个分支，然后再选择性merge到自己的master分支即可。

```sh
git fetch source master

# 切换到刚刚更新的源分支
git checkout source/master
```
