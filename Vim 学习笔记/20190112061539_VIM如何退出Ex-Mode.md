# VIM如何退出Ex Mode

用了VIM很久，以为摆脱了VIM初学者`退出VIM`的噩梦。
但没想到还是栽到了`退出Ex Mode`上。

一旦在Normal模式下“不小心”按到了大写的`Q`键，就会进入`Ex Mode`。先不说这个模式作用是什么（实际用处极少），光想尽方法退出就废了很大劲。
首先说明的是，以下这些方法都是不管用的：`exit`, `q`, `x`, `q!`, `wq`

Ex mode下的说明，输入`:visual`会退出，但其实不是！

如果在`:`模式下，输入`visual`按回车，只是进入`Ex Mode`的Normal模式，这时候你还要再按`.`点再按回车，再次回到`Ex Mode`下的`:`模式，再输入`visual`按回车才能真正退出。

[参考：How to exit Ex mode in vim (typing :visual does not work)](https://stackoverflow.com/questions/52656164/how-to-exit-ex-mode-in-vim-typing-visual-does-not-work)

[参考：Vim as the poor man's sed](https://www.brianstorti.com/vim-as-the-poor-mans-sed/)
