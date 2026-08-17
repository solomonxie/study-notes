# 蜗牛星际NAS安装系统
为什么蜗牛星级要单独讲安装系统？因为太麻烦！
要不就是主板上的UEFI坏了，要不就是UEFI本身安装就很麻烦，所以才出这么多幺蛾子。


## 硬件配置
最好拔掉自带MSATA卡，鸡肋，而且容易混淆视听，无论是安装系统、BIOS启动顺序，总是被它混淆。
推荐用两块SSD固态硬盘装两种系统，这样维护起来更简单，换系统只需要插拔两下就好了。作为长期开机的NAS，作为没有显示器在角落被远程的服务器，没有一个硬盘装两个系统的需求—— **因为没有显示器，没有鼠标键盘，没法开机的时候选择系统！！！**



## 安装Windows



## 安装Linux (Ubuntu)

参考：https://www.gitmemory.com/issue/solomonxie/solomonxie.github.io/33/506933418
参考：https://www.youtube.com/watch?v=BwXRtJ6eC7I
参考：https://post.smzdm.com/p/a83dp8l0/

先下载个Ubuntu的官方镜像，然后把它刻录到任意U盘上：
- Windows：用Rufus刻录
- Mac：用Etcher刻录

刻录完成后就可以插上U盘启动系统了，这里的尝试是：先把BIOS的boot顺序改为U盘优先，这样才能进去U盘的临时系统。

安装重点：
- [x] 先进Try Ubuntu系统里，再Install安装
- [x] BIOS设置启动系统设置为Windows
- [x] BIOS设置boot启动顺序为Linux这块硬盘优先
- [x] 分区分区分区！和网友的蜗牛星级生效的分区设置不同，我体验的成功分区配置只有 (按顺序)：
    1. `efi`格式 设为primary主分区，1GB
    2. `SWAP` 4GB
    3. `/` 为系统分区，20GB
    4. `/home` 为个人目录，30GB
    5. 其它都先不管，留为Free以后再弄
- [x] 如果上面不行，那就选择Erase disk那个，自动分区并安装系统，有时候也管用
- [x] 分区完后先不要点下一步，确定下面的下拉框那里选择启动磁盘为刚才分给`/boot`的分区
- [x] 安装全程不要插网线
