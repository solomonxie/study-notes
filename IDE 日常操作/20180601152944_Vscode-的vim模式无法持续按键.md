# Vscode 的vim模式无法持续按键
默认下，Mac上的vscode进入vim模式后，一直按住h, l, j, k等键，无法持续移动。
虽然在mac的vim里和sublime text里都没问题，但这不是vscode的问题，而还是mac的问题。

[参考：How do I press and hold a key and have it repeat in VSCode?](https://stackoverflow.com/questions/39972335/how-do-i-press-and-hold-a-key-and-have-it-repeat-in-vscode/44010683#44010683)

试着在终端里面输入以下命令关闭Mac的该功能：
```sh
# Disable Mac's "Press&Hold" feature
$ defaults write NSGlobalDomain ApplePressAndHoldEnabled -bool false
```
如果要恢复的话，再用这句：
```sh
# Re-enable this feature
$ defaults write NSGlobalDomain ApplePressAndHoldEnabled -bool true
```

 然后重启vscode就可以了。
