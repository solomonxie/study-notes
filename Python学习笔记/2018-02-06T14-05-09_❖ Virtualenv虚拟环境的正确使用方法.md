# ❖ Virtualenv虚拟环境的正确使用方法
之前当真以为是每个小项目都配置一个virtualenv环境，就每个文件夹都分别用`virtualenv`命令生成一个环境，还出现了一大堆文件夹，而且每次都要`pip install`重新安装一系列东西。
再加上很多小项目都有git配置，两者冲突，所以必须在`.gitignore`文件里屏蔽virtualenv都一切文件夹。

后来发现：
virtualenv虚拟环境不是只在这一个文件夹里生效的，它是那种只要开启了，你就带着这个虚拟都帽子到哪里哪个文件夹哪个项目都生效。
所以我就想，直接配置一个单独的文件夹专门放置virtualenv环境，然后每次都开启着它然后`cd`到项目文件夹去操作就行了。
这样既不会搞乱系统python环境，又不会每次都创建环境那么麻烦，毕竟不是什么大项目嘛。
如果是大型的项目，再单独在项目其中创建一个虚拟环境就好了。绝大多数时候，我只需要一个虚拟环境代替系统的python环境就足够了。

步骤是这样的：
1. 随便建一个位置，比如`cd ~/`，然后`virtualenv venv`，创建了一个叫`venv`的文件夹并且在里面配置了虚拟python环境。
2. 配置命令行别名：`alias venv="source ~/venv/bin/activate"`，这样就能一键开启虚拟空间，带上小帽子。
3. 安装自己所有需要的包，代替系统环境：`pip install PACKAGE-1 PACKAGE-2...`，或者`pip install -r PATH/requirements.txt`从之前的备份列表中一键恢复安装。
