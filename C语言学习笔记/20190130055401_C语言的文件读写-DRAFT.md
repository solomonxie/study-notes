# C语言的文件读写 [DRAFT]

## `fopen` 最简单读写

简单读文件：
```c
FILE *to_read = fopen("test.txt", "r")

if (to_read == NULL) {
    printf("Cannot open file\n");
    return -1
}

char c;
while ( (c=fgetc(to_read)) != EOF) {
    printf("%c", c);
}
fclose( to_read );
```

简单写文件：
```c

```


## `open`读写

[参考视频：Reading and Writing Files in C, two ways (fopen vs. open)](https://www.youtube.com/watch?v=BQJBe4IbsvQ&list=PL9IEJIKnBJjG5H0ylFAzpzs9gSmW_eICB&index=7)

注意一：
- `fopen`是`Library call`，是建立在`open`上进行封装、改善、加强易用性的调用。
- `open`是`System call`，是系统底层的文件读写调用。

注意二：`open`比`fopen`慢100倍。
为什么？为什么即使`fopen`是调用`open`读写文件的，还要比`open`慢呢？
是因为`fopen`调用了缓存，即`Buffered I/O`。

既然`open`比`fopen`还要慢，还要麻烦，为什么我们还要用它呢？
因为，*nix系统中一切皆文件，不光有文本文件，还有很多设备文件、pipes文件。而不是所有文件都需要缓存。类似设备这种，需要都是立马就操作，而不希望等待操作缓存的时间。

所以除了文本文件外，广泛的文件处理还是要用`open`的，因为`open`是底层的，意味着你能有更多的细节控制。

简而言之，`fopen`和`open`相当于高级语言和低级语言。高级语言用起来方便，低级语言可控性强。


