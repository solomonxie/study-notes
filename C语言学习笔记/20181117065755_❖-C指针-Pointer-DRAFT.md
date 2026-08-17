# ❖ C指针 Pointer [DRAFT]

作为系统底层语言，经常需要操作内存等，如`动态内存分配`，这是没有指针就无法完成的。



## 理解 `&`和`*`

每个变量都有两部分：⓵数据值  ⓶内存地址
而指针相当与一个`反变量`，它也是两部分但是相反： ⓵内存地址 ⓶数据值

假设有一个变量`int var = 100`，和一个指针`int *ptr = &var`。
当我们把指针指向了那个变量的时候，实际上的操作只是：把⓵和⓶换个位置。

**直接调用`var`或`ptr`的时候，都是显示⓵部分的值。**

但是如果要显示隐藏在背后的⓶部分的值，就需要用到这两个操作符号：
- `&`作用于变量，用于查看变量的⓶部分的值：即内存地址，如`&var`显示的是0x7fff5ccaf7dc。
- `*`作用于指针，用于查看指针的⓶部分的值：即数据值，如`*ptr`显示的是100。

明白这个“互反”规则后，以后的`**ptr`指向指针的指针也就好理解了。



## 使用指针

假设现在有一个普通变量`int height = 10;`，那么查看这个变量的`内存地址`的方法就是打印`&height`。

C指针也是一个`变量`，但是它的值是另一个变量的内存地址。

声明C指针型变量的方法：
```c
type *var-name;

// 如
int    *ip;    /* 一个整型的指针 */
double *dp;    /* 一个 double 型的指针 */
float  *fp;    /* 一个浮点型的指针 */
char   *ch;    /* 一个字符型的指针 */
```


怎么给指针赋值？当然不能手动写，而是需要把另一个变量的内存地址传给它：
```c
int variable = 1234;
int *addr;

addr = &variable;
```
这样就完成了指针的赋值。

怎么打印指针？
打印的时候要用特殊的`%p`格式化符号，代表`pointer`：
```c
// 打印指针中的指向的内存地址：
printf("%p", addr);

// 等同于：
printf("%p", &variable);

// 获得这块内存中的存储值：即刚才赋值的1234
printf("%d", *addr);
```


## 指向指针的指针

[参考：Making Peace with Double Pointers](https://www.youtube.com/watch?v=k6ESk9zafHM&index=28&list=PL9IEJIKnBJjGsttQusXPNuEknLQ6leUfS)

一个指针ptr指向variable的内存地址，那么另一个指针pptr指向前一个指针ptr，就相当于得到了variable的值。有点像`互反`的关系。

声明一个指针的指针：
```c
int  var;
int  *ptr;
int  **pptr;

var = 3000;
ptr = &var;   // 获取变量的内存
pptr = &ptr;  // 获取指针的值

// 打印
printf("%d\n", var );
printf("%d\n", *ptr );
printf("%d\n", **pptr);

// 输出结果全部都是3000
```

当然，你还可以设计`triple pointer`，比如：`int ***ppptr`，把它指向一个`double pointer`: `**ptr`.


## 函数指针

```c
// 声明函数
int max(int i, int j) { /* ... */ }

// 声明函数指针
int (* p)(int, int) = & max;   // &可以省略

// 使用函数指针
p(12, 34)
```



## 指针作为参数

```c
// 声明普通函数
int max(int i, int j) { /* ... */ }

// 声明参数为指针的函数
void func( int *arr, int (*max)(void) ) { /* .... */ }

// 使用函数（正常用，只不过不会把参数“复制“进去，而是直接使用，相当于公用变量）
func( [1,2,3], max );
```

## 从函数返回指针

```c
// 声明函数
void * func() { /* ... /* }

// 传递函数
int *ptr = func();

// 使用函数
ptr();
```


## 指针的算术运算

指针的算术运算有：
- `ptr++`，即`ptr = ptr + 1`
- `ptr--`，即`ptr = ptr - 1`
- `ptr = ptr + n`
- `ptr = ptr - n`

指针的`p++`，`p+1`, `p--`, `p-1`等，都是指的`指针位移`。
假设一个指针指向了数组，如：
```c
int arr[] = {123, 456, 789};
int *ptr = arr;
```
那么，实际上指针是指向了`数组的第一个元素`。
另外，由于数组本质上也是个指针，所以不需要`&arr`来得到内存地址。

也就说，这个时候，实际上`ptr == &arr == &arr[0]`，这三项的值是一样的。
那么当`ptr++`或`ptr=ptr+1`的时候，指针移向了下一个位置，即`arr[1]`的内存地址。这时：`ptr == &arr[1]`。

同理，`ptr--`只是往前位移了1而已。

既然指针ptr是一个简单的位置信息，那么我们同样可以`比较指针`：
```c
if (ptr < &arr[2])
    printf("%d", ptr);
```

