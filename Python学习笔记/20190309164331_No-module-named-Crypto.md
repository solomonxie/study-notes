# No module named 'Crypto'

这是由于pip内部的模块命名、版本冲突导致的，只要卸载相关的包，再用`pycrypto`代替即可。
```sh
pip uninstall crypto 
pip uninstall pycrypto 
pip install pycrypto
```

之后就能正常的引用了：
```py
from Crypto.Cipher import AES
```
