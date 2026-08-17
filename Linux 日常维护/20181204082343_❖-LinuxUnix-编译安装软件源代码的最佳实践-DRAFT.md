# ❖ Linux/Unix 编译安装软件源代码的最佳实践 [DRAFT]

`Subtitle: Linux / Unix Build Software From Source Code Best Practice`

*nix下编译安装开源软件是新手的一大痛。鉴于我胆小怕事、在正式学习前不随便使用新东西的心态，用了Linux很多年后现在才开始正式学习怎么编译一个新版本的开源软件。因为迫于跟不上新版本、包管理器不支持某些硬件平台等原因，现在已经到了不编译不行的地步，所以扛不住了，开始学习！


## 理解软件编译

源代码下载的话，基本上都是到Github直接下载zip或tar包即可。

**常用的需要编译的开源软件主要指C或C++开发的软件。**

一般编译这些软件主要有这几步：
- `./configure` - 检测本机当前的环境，看看是否满足权限和依赖包等。
- `make` - 把源代码编译成二进制文件
- `make install` - 把各个二进制文件和配置文件等复制到对应的目录
- `make uninstall` - 卸载(删除) make install时存到各个目录的文件。（如果Makefile中定义了才能用）


## Dependency Hell

软件编译的最大问题就是`依赖`。遇到`Dependency Hell`，绝对是大概率事件。


## `/usr/local` vs. `/opt` [DRAFT]

对于自己编译的软件安装到哪里，可以比得上`Vim vs. Emacs`之争了。

简单来说：
- `/usr/local` - 
- `/opt` - 


## 总结

```sh
./configure --prefix=/opt/MyProgram && echo [  OK  ]
make && echo [  OK  ]
sudo make install && echo [  OK  ]
```

每一句是完全隔离是因为这样能更清晰的知道错误出现在哪里。
每一句后面打印`[  OK  ]`是为了更方便看到知道命令是否产生错误。
