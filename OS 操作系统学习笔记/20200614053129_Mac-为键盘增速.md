# Mac 为键盘增速

Refer to: https://apple.stackexchange.com/questions/10467/how-to-increase-keyboard-key-repeat-rate-on-os-x
Refer to: https://www.howtogeek.com/267463/how-to-enable-key-repeating-in-macos/
Refer to: https://apple.stackexchange.com/questions/261163/default-value-for-nsglobaldomain-initialkeyrepeat#:~:text=The%20defaults%20for%20a%20freshly,%3D%2025%20and%20KeyRepeat%20%3D%206%20.

```sh
defaults write -g ApplePressAndHoldEnabled -bool false  # default true
defaults write -g InitialKeyRepeat -int 10  # default 25
defaults write -g KeyRepeat -int 1  # default 6
```

Re-login to make it work.
