# How to pass multiple Environment variables in One String to the command

Refer to: https://stackoverflow.com/questions/59596537/how-to-pass-environment-variables-from-a-string-to-a-bash-command

Support we have a script to read environment variables:
```sh
# demo.sh
echo Name is: $NAME
echo Age is: $AGE
```

```sh
$ envvars=( NAME=Jason AGE=18 )
$ env "${envvars[@]}" ./demo.sh
Name is: Jason
Age is: 18
```
