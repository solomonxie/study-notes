# Git: How to force merge/overwrite from one branch to another

Scenario:
The feature-branch has been merged to master-branch, then something bad happened, and you decid to roll-back. Then you want to fix the problem on feature-branch again...


## Easier way

Refer to: https://superuser.com/questions/692794/how-can-i-get-all-the-files-from-one-git-branch-and-put-them-into-the-current-b

Scenario: You want to copy all files from feature 
```sh
git checkout master
git checkout feature .
```


## Harder way

[Refer to: How do you force a merge with Git?](https://www.quora.com/How-do-you-force-a-merge-with-Git)

**I don’t care if there is any other conflict. My branch A will win. Always:**
```
git checkout A
git merge -s ours master
git checkout master
git merge A
```
