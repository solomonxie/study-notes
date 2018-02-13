# Python操作Git库 `GitPython`
[参考文章](http://note.qidong.name/2018/01/gitpython/)
[参考文章](http://www.cnblogs.com/baiyangcao/p/gitpython.html)
[复杂点的参考](https://my.oschina.net/hopeMan/blog/141221)

试了一圈发现，git库的用法设置非常符合原生git命令，只不过之间加了个`.`而已。
比如原本命令行里是`git add .`，这里就是`repo.git.add('.')`，
原本是`git commit -m "信息"`，这里就是`repo.git.commit(m='信息')`
可以说减少了很多学习时间，基本上我很多都是没参考文档自己猜出来的也能用。

```
sudo pip install gitpython
```
库安装好后可以直接在python中用了。

### 创建、识别、克隆仓库
文件夹地址可以是全路径，也可以是`.`当前文件夹、`../`上级文件夹等用法。
```
# 在文件夹里新建一个仓库，如果已存在git仓库也不报错不覆盖没问题
repo = git.Repo.init(path='文件夹地址')

# 选择已有仓库
repo = git.Repo( '仓库地址' )

# 克隆仓库
repo = git.Repo.clone_from(url='git@github.com:USER/REPO.git', to_path='../new')
```
### 常用语句：
```python
# 查看repo状态
print repo.git.status()   # 返回通常的status几句信息
print repo.is_dirty()    # 返回是否有改动（包括未add和未commit的）

# 添加文件 可以是单个文件名，也可以是`[ ]`数组，还可以是`.`代表全部
print repo.git.add( '文件名' )

# commit提交
print repo.git.commit( m='提交信息' )
```

### 远程交互操作
```python
# 创建remote：
remote = repo.create_remote(name='gitlab', url='git@gitlab.com:USER/REPO.git')

# 远程交互：
remote = repo.remote()
remote.fetch()
remote.pull()
remote.push()
```

### 实验效果
```python
 # 原意是返回工作区是否改变的状态
# 但是测试发现，工作区有变动它返回False，没变动却返回True
print repo.is_dirty()
```

### 生成tar压缩包
```python
# 压缩到 tar 文件
with open('repo.tar', 'wb') as fp:
    repo.archive(fp)
```
