# 栈与队列 Stack & Queue

栈与队列本质上也是线性表的不同存储方式：
- 栈Stack：像堆盒子一样，后进先出(LIFO)。
- 队列Queue：像排队办事一样，先来先处理（FIFO）。

## 栈 Stack
常用操作和线性表List一样。只是在插入和删除时需要执行这两个特殊的操作：
- 进栈：Push (in)
- 出栈：Pop (out)

Stack只能每次在栈顶进行操作，删除了栈顶，才能逐次操作下一层的数据。

栈也分为两种不同的存储结构：
- 顺序存储
- 链式存储 （链栈 Linked Stack）

链栈是不需要头节点的，因为栈顶自动成为了头部。

栈的应用：递归(Recursion)、多层括号匹配（Nested brackets)、基础四则算术

Basic Arithmetic Operations: 由于四种基本算术层层嵌套，电脑很难识别。所以利用了[`逆波兰表达法`(RPN, Reverse Polish Notation)](https://www.wikiwand.com/en/Reverse_Polish_notation)。
比如将：
`((15 ÷ (7 − (1 + 1))) × 3) − (2 + (1 + 1))`
表示为↓：
`15 7 1 1 + − ÷ 3 × 2 1 1 + + −`



## 队列 Queue

队列是FIFO，只允许在队列头部删除，在队列尾部插入。
