# Move the most recent commits (multiple) to another branch

The story is:
> After a few hours of hard work & submitted a few commits, and realized that all the commits were submitted at the MASTER branch !!!

Something like this:
```
master A - B - C - D - E
```
in which `C - D - E` are the newest commits I made on master branch that should be on a feature branch.
What I expected:
```
newbranch     C - D - E
             /
master A - B 
```

What should be done is to commit on feature-branch then merge to master, but definitely not directly commit on master branch.

What I'm gonna do to fix it is easy:
- Checkout to a new branch from master, which will copy all the commits history to the new branch
- Checkout to master-branch, **delete** recent local commits (thank God haven't pushed to remote yet).

```sh
(master)$ git checkout -b new-feature
(new-feature)$ git checkout master
(master)$ git reset --hard head~3
```

The key command is `git reset --hard head~3` which **deletes** the most recent 3 commits.

