# Git: How to delete all branches except master?

Simple solution-1:
```sh
git checkout master
git branch -D $(git branch)
```
^ This will hard delete all branches except the current one (because its name got a `*`)

Simple solution-2:
```sh
cd ..
mv /path/to/project /tmp
git clone https://path/to/project
```
^ This will remove the whole project and download again :) be very careful unless you're sure of the risk
