# Git误删文件恢复的方法
Stackoverflow的这个回答相当不错，我也很快找回了文件。[参考链接](https://www.quora.com/How-can-I-recover-a-file-I-deleted-in-my-local-repo-from-the-remote-repo-in-Git)
具体说起来是这样的，
```
# If the deletion has not been committed, 
# the command below will restore the deleted file in the working tree.
git checkout -- <file>

# You can get a list of all the deleted files in the working tree using the command below.
git ls-files --deleted

If the deletion has been committed, find the commit where it happened, then recover the file from this commit.
git rev-list -n 1 HEAD -- <file>
git checkout <commit>^ -- <file>
```
