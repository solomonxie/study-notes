# Git push error:  [remote rejected] remote: error: cannot lock ref 'refs/heads/mybranch': Unable to create '/path/to/project/project.git/./refs/heads/mybranch.lock': File exists.

Refer to: https://stackoverflow.com/questions/6656619/git-and-nasty-error-cannot-lock-existing-info-refs-fatal

Solution:
```sh
$ git remote prune origin
$ git push origin mybranch
```
