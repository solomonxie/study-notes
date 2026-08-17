# ❖ Bash脚本中的「闭包」

高级语言中的闭包或装饰器，是个非常好用的功能。Bash没有直接的闭包，但是Bash可以将函数作为参数传递给另一个函数，这样我们就可以达到闭包功能了。

[参考：Bash: 将函数作为参数传递](https://ask.helplib.com/bash/post_659593)

```sh
function inner() {
    echo "Hello, world!"
}

function outter() {
    echo "before"
    eval $1
    echo "after"
}

outter inner
```

然后就会输出：
```
before
Hello world
after
```
