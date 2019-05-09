# Git: How to View Single File Change History

```sh
$ git log -p /path/to/file
# or (same):
$ git log --follow -p /path/to/file
```

Set `~/.gitconfig`:
```gitconfig
    history = log --follow -p
```

```sh
$ git history /path/to/file
```


## View with Tig

```sh
$ Tig /path/to/file
```
