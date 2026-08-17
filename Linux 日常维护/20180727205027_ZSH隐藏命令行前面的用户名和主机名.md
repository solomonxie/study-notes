# ZSH隐藏命令行前面的用户名和主机名

只需要修改`~/.zshrc`即可：
- 隐藏用户名和主机名：
```
prompt_context() {}
```
- 只保留用户名，隐藏主机名：
```
prompt_context() {
  if [[ "$USER" != "$DEFAULT_USER" || -n "$SSH_CLIENT" ]]; then
    prompt_segment black default "%(!.%{%F{yellow}%}.)$USER"
  fi
}
```
