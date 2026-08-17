# Project: Git issues App
专注于issues博客功能，出发点就不同于桌面已有的和手机上鲜有的应用。
特点：
- 每个issues笔记都算为github的contribution，美化profile工作日历
- 自动转md文件并上传到github中的repo，更填改完全对应
- 实时同步网络repo中的issues
- 本地存储性，没联网也可以编辑保存，联网了再自动同步（放心）
- 定期自动备份到多端
- 图片上传到github自带的repo中（市面所有应用都没做到）
- 同时支持desktop和iphone和web page
- 界面和笔记应用相同（如note.app）

实现主要技巧：
- 将issues映射到其repo的某一特定分支，每个comment为单独md文件
- 图片上传到repo中并引用其raw链接
- 建立每条comment和其md文件的对应表
- 实时监控本地更新，并push到远端；定期查询远端更新，pull到本地。如有冲突，则跳过有冲突的文件，让用户选择方案


## issues映射到独立博客
自动化工具，把issues映射到博客站，成为指定格式的MD文件。
注意：
- 自动列出所有issues和里面的comments，
- 然后有多选框，可以选择对哪些进行映射，哪些不映射。

在博客站中，
也可以对每篇文章进行选择：
是不是根据原始issue进行自动更新，或者手动更新。

### 更新idea：
1. 
改变下思路。
博客是正常的博客，正常让自己增删改的博客。
只是多出一个功能：
可以像Instapaper一样，增加一个链接url，然后它自动读取这个url页面的内容。
也就是说，我可以添加一个`自动页面`，指定某个github的issue的comment的url后，博客系统会定期自动提取这个url的内容更新到博客中。
这样的逻辑就更简单，实现起来更方便了。

2.
以上是针对后期的。
另外，前期因为已有的issue博客太多了，一个一个手动添加url太麻烦。
所以需要一个自动工具（可以显示在博客后台里）：
直接提取出某个github的所有issues和所有comments，然后通过选择框，让你选择哪些自动提取到博客里面来。

3. 
再后期，为了实现双向同步，还需要进一步完善逻辑：
原本的是博客根据github issue来更新。
但是如果从博客上更改了文章，那么也可以去更新github上对应的issue。

### 更新
一定一定一定要保持github issues的展示方式：列出所有的comments。
映射到博客时，千万不要一个comment一页，这样实在太麻烦太费劲了。
我真的体会到把所有相关笔记放在一个页面里，One page的便利性了。
唯一的缺点是东西太多加载过慢。

但是这个可以解决：
- 第一，可以用分页，50篇comments一页
- 第二，可以计算comments的大小（html和图片的总大小），根据文件大小觉得分页程度
- 第三也许是最好的，每篇comments都显示，但是每篇都只显示前100个字。其余的需要点击“加载全文”才显示。

# Project: Gitissues 分发系统
@2018-05-17

写的话，集中在一个repo的issues里面写就可以。
但是其实更需要分很多个repo来生成专门的博客。

先创建多个repo，如Math／ML／Tech 等等。

在总issue里，可以随便乱写，然后脚本根据每个issue的Milestone或label或某种设置，把它映射到不同的repo中的issues和markdown文件中去。


# Project: 根据github笔记制作遗忘曲线邮件提醒

利用github笔记的历史版本记录功能，
在树莓派上建立`定期发送邮件脚本`，
根据`遗忘曲线`的复习周期，定期将github的该篇笔记的markdown内容转为邮件富文本样式发送给指定邮箱。

主要技术：
- Linux的`sendmail`或`mail`命令设置
- Python的Markdown转html或邮件富文本格式
- github笔记的时间分析功能：以该笔记在git中记录的最早时间为记忆周期的starting point， 然后根据更新的时间点，判断last_updated时间处在记忆周期的哪个点上，然后排列出一个提醒日程表，根据日程发送邮件。
