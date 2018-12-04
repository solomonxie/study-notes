# 编译VIM

编译VIM最麻烦的只有一个问题：
**各个语言的位置和`开发库的位置`。**

注意：语言本身的位置好说，但是`dev`开发库就不一样了。
比如，一般我们本机只安装`python`，而不会安装`python-dev`。这是两个完全不一样的概念。第一个我们直接使用的语言，第二个是本机编译、开发能够引用的开发lib库。
所以，根据语言支持的需要，我们要安装这些开发库：
- python-dev
- python3-dev
- ruby-dev
- perl-dev
- lua-dev
- libncurses5-dev

如果安装好这些依赖，且明白各自的位置后，剩下的VIM编译是超级简单的。
如果编译出现问题，也绝对是这些位置出现了问题。


## 树莓派编译VIM包括Python／Lua／Ruby／Perl支持

```sh
# 下载源码
cd /tmp
wget https://github.com/vim/vim/archive/v8.1.0561.tar.gz
tar -xzvf v8.1.0561.tar.gz
cd vim-8.1.0561

# 下载语言支持的开发库（和本机的各种语言使用无关）
sudo apt-get install -y libncurses5-dev liblua5.3-dev libperl-dev python-dev python3-dev ruby-dev

# 定义各个语言的开发库位置

# 修复lua位置
sudo mv $(which lua) "$(which lua)_old"
sudo ln -s /usr/bin/lua5.3 /usr/bin/lua
sudo ln -s /usr/include/lua5.3 /usr/include/lua
sudo ln -s /usr/lib/arm-linux-gnueabihf/liblua5.3.so /usr/local/lib/liblua.so

# 修复python位置
sudo ln -s /usr/lib/python2.7/config-arm-linux-gnueabihf /usr/lib/python2.7/config
sudo ln -s /usr/lib/python3.4/config-3.4m-arm-linux-gnueabihf /usr/lib/python3.4/config

# Build
./configure \
    --prefix=/opt/vim-8.1 \
    --enable-gui=auto \
    --enable-luainterp \
    --enable-python3interp \
    --enable-pythoninterp=dynamic \
    --enable-perlinterp=dynamic \
    --enable-rubyinterp=dynamic \
    --enable-cscope \
    --enable-multibyte \
    --enable-fontset \
    --enable-largefile \
    --enable-fail-if-missing \
    --with-features=huge \
    --with-python-config-dir=/usr/lib/python2.7/config \
    --with-python3-config-dir=/usr/lib/python3.4/config \
    --disable-netbeans && \
    echo '[ OK ]'

make && sudo make install && echo '[ OK ]'

# 将旧版本的vim替换
sudo mv $(which vim) "$(which vim)_old"
sudo ln -s /opt/vim-8.1/bin/vim /usr/bin/vim
```


## Mac编译VIM包括Python／Lua／Ruby／Perl支持

```sh
# Download
cd /tmp
wget https://github.com/vim/vim/archive/v8.1.0561.tar.gz
tar -xzvf v8.1.0561.tar.gz
cd vim-8.1.0561

# Build
./configure \
--prefix=/opt/vim-8.1 \
--enable-multibyte \
--enable-perlinterp=dynamic \
--enable-rubyinterp=dynamic \
--with-ruby-command=/usr/local/bin/ruby \
--enable-pythoninterp=dynamic \
--with-python-config-dir=/usr/lib/python2.7/config \
--enable-python3interp \
--with-python3-config-dir=/usr/local/Cellar/python/3.7.0/Frameworks/Python.framework/Versions/3.7/lib/python3.7/config-3.7m-darwin \
--enable-luainterp \
--with-lua-prefix=/usr/local/Cellar/lua/5.3.5_1 \
--enable-cscope \
--enable-gui=auto \
--with-features=huge \
--enable-fontset \
--enable-largefile \
--disable-netbeans \
--enable-fail-if-missing && \
echo '[ OK ]'

make && sudo make install && echo '[ OK ]'
```

如果本机没有lua的话：
```sh
brew install lua
```
然后仔细查看lua路径，一般是`/usr/local/Cellar/lua*`，把它替换到configure的参数中去。


如果Python没有配置好的话，则到`/usr/local/Cellar/python`目录下搜索`config-*`文件：
```sh
find /usr/local/Cellar/python -name "config-*"
```
然后我得到的是`/usr/local/Cellar/python/3.7.0/Frameworks/Python.framework/Versions/3.7/lib/python3.7/config-3.7m-darwin`。把它替换到configure的参数中相应位置。


