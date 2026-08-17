# ❖ “动态外键” 或——放弃外键 [DRAFT]

其实我们有很多的`动态外键`需求，因为当表格关系达到10+的话，很容易就产生大量数据冗余。要排除数据重复，那么就要“灵巧的”设计映射关系，那么就少不了有多主键或多映射表。
那么这种时候就必然被“固定外键”所捆绑。

自己思考到这一层后，想去网上看看。结果发现实践开发过程中，`放弃外键`已经成了主流。约束全都在程序里执行。的确！只要放弃外键这个概念，似乎数据库的一切都变得轻松了起来。


[参考：Is it possible to have an dynamic foreign key, and what is the best/correct to do so?](https://stackoverflow.com/questions/22372660/is-it-possible-to-have-an-dynamic-foreign-key-and-what-is-the-best-correct-to-d)
[参考：互联网开发中不用外键到底是个什么意思？](https://segmentfault.com/q/1010000015808865/a-1020000015819545)
[参考：知乎 大家设计数据库时使用外键吗？](https://www.zhihu.com/question/19600081)
[参考：google - generic FKs](https://www.google.com/search?q=generic+FKs&oq=generic+FKs&aqs=chrome..69i57&sourceid=chrome&ie=UTF-8)
