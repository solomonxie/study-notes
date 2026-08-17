#  ❖ Vimrc Tricks For Anything [DRAFT]


## BUFFER

### Check if buffers are empty (no file opened)
If there's no file opened, `:echo @%` would be empty.
```vim
if @% = ""                               
        dosomething....
endif     
```

## WINDOW | SPLIT


## TAB

### Close all buffers in a tab

```vim
:windo bdelete
```


## ENVIRONMENT


### Get current OS

```vim

```
