# Git: How to copy a file from another branch

[Refer to: How do I copy a version of a single file from one git branch to another?](https://stackoverflow.com/questions/307579/how-do-i-copy-a-version-of-a-single-file-from-one-git-branch-to-another)

Change the file to another version:
```
git checkout other-branch myfile.txt
```

Copy a file from another file in another branch:
```
git show commit_id:path/to/file > path/to/file
```
