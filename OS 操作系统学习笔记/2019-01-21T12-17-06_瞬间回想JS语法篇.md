## 瞬间回想JS语法篇
> 有时候在各种语言间穿梭，时时会忘了这个东西的最基本语法区别，比如声明变量、循环、条件判断等。所以就需要在这里立个篇章专门说。

```javascript
// 注释单条语句
/* 注释块语句 */

// 声明变量
var a = 1;
var b = "hello", c = [];
var c = {}; // Object

// Json变量
var json = {
    "name": "jason",
    "skills": ["programming", "swimming"]
};

// 变量操作
[1,2,3] + "hello" == "1,2,3hello";

// 条件判断
if (true && true) { }
else if (1==1 || 2!=3) {}
else {}

// for循环
for (var i=0; i<arr.length; i++) {
    // 停止循环
    break;
    // 继续循环并跳过本次
    continue;
}
```
