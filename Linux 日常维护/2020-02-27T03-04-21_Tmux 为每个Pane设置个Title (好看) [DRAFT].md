# Tmux 为每个Pane设置个Title (好看) [DRAFT]


```sh
#tmux.conf

set -g pane-border-status top

# set -g pane-border-format " #P: #T #{pane_current_command} #{pane_name}"
set -g pane-border-format " [#P] #T "
```

默认的这个 `#T` 是Hostname。
为了方便换title，与其设各种function，我们最简单的就是设置一个alias：
```sh
$ alias panetitle="printf '\033]2;%s\033\\'"

$ panetitle 'this is my new title'
```
