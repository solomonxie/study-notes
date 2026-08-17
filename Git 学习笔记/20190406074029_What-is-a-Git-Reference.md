# What is a Git Reference?

> So Basically, a `git ref` is just an **"alias"** of a commit hash key like `d914f` for each branch's _newest_ commit (HEAD).

Actually, it's not only a branch's latest commit, but also some other type of _special commits_.
The types of `refs`:
- A local branch's latest commit: stored at `.git/refs/heads`
- A remote branch's latest commit: stored at `.git/refs/remote/`
- A tag's related commit: stored at `.git/refs/tags`

[Refer to: Deep dive into git: Git refs](https://aboullaite.me/deep-dive-into-git-git-refs/)

For example, I have a `fix-decoding` branch, and the hash key for its HEAD (newest commit) is `d914f9ad7d6547167f2f182ba7daa7174431b7ed`. 
What git does for our convenience is to create an _alias_ for that as a file at `.git/refs/heads/fix-decoding`, which has only the content `d914f9ad7d6547167f2f182ba7daa7174431b7ed`.


![git-refs](20190406074029_What-is-a-Git-Reference_files/img_01.gif)


So what you have in the `.git/ref` directory is:
- `heads`: The `HEAD` file of every branch, each file only contains the `commit-ID`.
- `remotes`: All heads of all branches of all remtoe servers
- `tags`: All tags, in which each tag contains the ID of specific commit.

How to see all `references`?
```sh
$ git reflog
  ceb40ab HEAD@{0}: commit: commit empty
  2937af1 HEAD@{1}: commit: Commit empty file
  e3c3a05 HEAD@{2}: commit (initial): add file 1
```



## HEAD: A Special Ref

Assume that you're at a `fix-decoding` branch, and the latest commit is `f09096f`. Now you want to do:
```sh
$ git show f09096f
commit f09096f8...........
...............

$ git show HEAD
commit f09096f8...........
...............
```
What you are looking at means that `f09096f = HEAD`. Exactly, the `HEAD` is just an _**alias**_ for the `Latest commit` of **CURRENT** branch.

How about other branches?
All the "heads" files are located in `.git/ref/heads`, which lets you and git know the HEAD for every branch. And when you perform a `git checkout xx`, git copy the specific head of current to be as `.git/HEAD`.

