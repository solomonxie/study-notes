# pip 同时升级所有package包

Refer to: https://stackoverflow.com/questions/2720014/how-to-upgrade-all-python-packages-with-pip

```sh
$ pip list --outdated --format=freeze | grep -v '^\-e' | cut -d = -f 1  | xargs -n1 pip install -U
```
