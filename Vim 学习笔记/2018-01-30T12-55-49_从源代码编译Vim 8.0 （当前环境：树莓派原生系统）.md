# 从源代码编译Vim 8.0 （当前环境：树莓派原生系统）
> 因为在安装某个vim最难安装的插件，必须要最新版本的vim才行，而通过`apt-get`是无法更新vim的，所以又必须要自己在本地编译源代码才行。所以才花了几个小时倒腾这个。我相信，非常非常非常多的人在编译vim都遇到了困难。

因为不敢在Mac自己机子上随便试，就拿树莓派练手。安装过程不光麻烦，而且耗时比较长。具体是参考[这篇文档](https://github.com/Valloric/YouCompleteMe/wiki/Building-Vim-from-source)安装，中文翻译版本在[这里](https://linux.cn/article-8094-1.html)。
简而化之，我使用的命令如下：
```shell
# 安装基础支持库
sudo apt install libncurses5-dev libgnome2-dev libgnomeui-dev \
    libgtk2.0-dev libatk1.0-dev libbonoboui2-dev \
    libcairo2-dev libx11-dev libxpm-dev libxt-dev python-dev \
    python3-dev ruby-dev lua5.1 lua5.1-dev libperl-dev git

# 删除已安装的vim和所有相关
sudo apt-get remove vim vim-runtime gvim vim-tiny vim-common vim-gui-common vim-nox

# 从vim的github上下载最新的源文件（太慢的话就直接手动去其github页面下载zip文件并解压）
cd ~
git clone https://github.com/vim/vim.git

# 初始化配置
cd vim
./configure --with-features=huge \
    --enable-multibyte \
    --enable-rubyinterp=yes \
    --enable-pythoninterp=yes \
    --with-python-config-dir=/usr/lib/python2.7/config \
    --enable-python3interp=yes \
    --with-python3-config-dir=/usr/lib/python3.5/config \
    --enable-perlinterp=yes \
    --enable-luainterp=yes \
    --enable-gui=gtk2 --enable-cscope --prefix=/usr
make VIMRUNTIMEDIR=/usr/share/vim/vim80

# 编译
cd ~/vim
sudo make install

# 设置vim为默认编辑器
sudo update-alternatives --install /usr/bin/editor editor /usr/bin/vim 1
sudo update-alternatives --set editor /usr/bin/vim
sudo update-alternatives --install /usr/bin/vi vi /usr/bin/vim 1
sudo update-alternatives --set vi /usr/bin/vim

# 检查vim版本
vim --version
```
