## Ubuntu循环登陆问题（包括各种基于Ubuntu的系统）

网上各种说权限问题等，实际上绝大多数问题，都是由误装、误删软件引起的。
而这其中，绝大多数是搜狗拼音或其他输入法相关的操作引起的。
重新安装fctix各种输入法即可， 瞬间解决。

```
sudo apt-get install fcitx-pinyin fcitx-sunpinyin fcitx-googlepinyin fcitx-anthy fcitx-mozc -y
```
