## Bash里读取Json数据
查看Stackovervlow, 发现[答案](https://stackoverflow.com/questions/1955505/parsing-json-with-unix-tools)，既可以使用`sed+awk`来自己写解析读取json，也可以通过引用python方法来更方便的解析。推荐python方法，如下：
```bash
echo '{"hostname":"test","domainname":"example.com"}' | python -c 'import json,sys;obj=json.load(sys.stdin);print obj[0]["hostname"]'
```
由于*nix都原生带有python，所以这么执行是没问题的。而且一般也不用考虑到执行速度问题。
