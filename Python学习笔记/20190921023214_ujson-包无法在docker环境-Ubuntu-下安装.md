# `ujson` 包无法在docker环境(Ubuntu)下安装

Docker的Ubuntu中安装会出现这种错误：
```sh
$ pip install ujson

Installing collected packages: ujson
  Running setup.py install for ujson ... error
    ERROR: Command errored out with exit status 1:
     command: /usr/bin/python -u -c 'import sys, setuptools, tokenize; sys.argv[0] = '"'"'/tmp/pip-install-odf2bpos/ujson/setup.py'"'"'; __file__='"'"'/tmp/pip-install-odf2bpos/ujson/setup.py'"'"';f=getat
tr(tokenize, '"'"'open'"'"', open)(__file__);code=f.read().replace('"'"'\r\n'"'"', '"'"'\n'"'"');f.close();exec(compile(code, __file__, '"'"'exec'"'"'))' install --record /tmp/pip-record-ytau26tb/install-
record.txt --single-version-externally-managed --compile
         cwd: /tmp/pip-install-odf2bpos/ujson/
    Complete output (16 lines):
    Warning: 'classifiers' should be a list, got type 'filter'
    running install
    running build
    running build_ext
    building 'ujson' extension
    creating build
    creating build/temp.linux-x86_64-3.7
    creating build/temp.linux-x86_64-3.7/python
    creating build/temp.linux-x86_64-3.7/lib
    x86_64-linux-gnu-gcc -pthread -DNDEBUG -g -fwrapv -O2 -Wall -g -fstack-protector-strong -Wformat -Werror=format-security -Wdate-time -D_FORTIFY_SOURCE=2 -fPIC -I./python -I./lib -I/usr/include/python3
.7m -c ./python/ujson.c -o build/temp.linux-x86_64-3.7/./python/ujson.o -D_GNU_SOURCE
    In file included from ./python/ujson.c:39:0:
    ./python/py_defines.h:39:10: fatal error: Python.h: No such file or directory
     #include <Python.h>
              ^~~~~~~~~~
    compilation terminated.
    error: command 'x86_64-linux-gnu-gcc' failed with exit status 1
    ----------------------------------------
ERROR: Command errored out with exit status 1: /usr/bin/python -u -c 'import sys, setuptools, tokenize; sys.argv[0] = '"'"'/tmp/pip-install-odf2bpos/ujson/setup.py'"'"'; __file__='"'"'/tmp/pip-install-odf
2bpos/ujson/setup.py'"'"';f=getattr(tokenize, '"'"'open'"'"', open)(__file__);code=f.read().replace('"'"'\r\n'"'"', '"'"'\n'"'"');f.close();exec(compile(code, __file__, '"'"'exec'"'"'))' install --record
/tmp/pip-record-ytau26tb/install-record.txt --single-version-externally-managed --compile Check the logs for full command output.
```

原因是这个环境里没有安装一些GNU编译的基本工具。参考Dockerfile
```dockerfile
# Dockerfile

FROM ubuntu:18.04
MAINTAINER Solomon Xie <solomonxiewise@gmail.com>

RUN apt-get update
RUN apt-get install -y python3.7 && \
    ln -sf /usr/bin/python3.7 /usr/bin/python

# Install pip
RUN apt-get install -y --no-install-recommends \
    libpython3.7-dev \
    libpq-dev python3-distutils build-essential

COPY get-pip.py /get-pip.py
RUN python /get-pip.py

# RUN apt-get install build-essential software-properties-common -y
COPY requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

COPY main.py /main.py
CMD ["python3.7", "/main.py"]
```
