# Makefile Is The New Python [DRAFT]

> "Makefile is the new python" - Forget who wrote that in a tutorial

That is the point where I was intrigued the most to decide to learn `Makefile`.

Don't get it wrong,
the `Makefile` is **NOT** only for compiling the C/C++ programmes, but to **"anything"**.

Even if it's just a normal folder contains some _markdown_ files, you can create a `Makefile` to do some automation stuff to it.

In essence, a `Makefile` is just to run some _bash commands_ for you.

e.g., you want to do some `cp`, `rm` & `mv` in a folder, you can line them up in a `Makefile` and give it a simple name like `orgainize`, and run the command `make organize` to run all the commands you have defined, in which it looks like this:
```Makefile
# Makefile

organize:
    cp test.py test2.py
    rm *.pyc
    mv test.py test_bak.py
```


## Syntax

[Refer to: What is a Makefile and how does it work?](https://opensource.com/article/18/8/what-how-makefile)

The simplest one:
```Makefile
TAG1:
    command
    command
```
Notice that before each command there're 4 spaces or a tab.

But this will display each command entirely, which sometimes we don't want that. To hide display of commands but only coomand outputs, we simply add `@` to each command:
```Makefile
say_hello:
    @echo "Hello, world!"
```

Tag with "prerequisites" (other tags):
```Makefile
init:
    cp 01.txt 02.txt

clean: init
    rm 02.txt
```

When you run `make clean`, the command `rm 02.txt` only works when the `init` works


### Headers

At the top of `Makefile`, you can add some useful `headers` like constant variables or options to make the "script" cleaner.



## Sub-make

[Refer to StackOverflow: make : rule call rule](https://stackoverflow.com/questions/8646688/make-rule-call-rule)
[Refer to GNU: How the MAKE Variable Works](https://www.gnu.org/software/make/manual/html_node/MAKE-Variable.html)

`./Makefile` in root directory:
```makefile
tosub:
	@cd sub && $(MAKE) sub
```

`./sub/Makefile`:
```makefile
sub:
	$(MAKE) subcommand

subcommand:
	@echo This recipe is in sub folder.
```

Run:
```sh
$ cd /path/to/project
$ make sub
/usr/bin/make subcommand
This recipe is in sub folder.
```
