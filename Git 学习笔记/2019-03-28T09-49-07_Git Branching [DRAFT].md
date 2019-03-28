# Git Branching [DRAFT]


Check out to a remote branch (not exists locally):
```sh
git checkout -b feature01 origin/feature01
```

Delete all local commits on this branch:
```sh
git reset --hard @{u}
```

Fetch **ALL** remote branches (you have to do it manually):
```sh
git branch -r | grep -v '\->' | while read remote; do git branch --track "${remote#origin/}" "$remote"; done
```

Fetch for current branch from ALL remote servers:
```sh
git fetch --all
```

Update all local **EXISTING** branches from remote:
```sh
git pull --all
```
