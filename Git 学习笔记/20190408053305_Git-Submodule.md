# Git Submodule

[Refer to: Using submodules in Git - Tutorial](https://www.vogella.com/tutorials/GitSubmodules/article.html)

`.gitmodules`
```
[submodule "binary"]
	path = binary
	url = git@git.github.com:Jason/binary.git
[submodule "locale"]
	path = locale
	url = git@git.github.com:Jason/locale.git
	branch = master
```

Clone project with submodules:
```sh
git clone --recursive [URL to Git repo]
```

Pull all submodules at once:
```sh
git submodule update --init
# if there are nested submodules:
git submodule update --init --recursive
```

Download up to 8 submodules at once:
```sh
git submodule update --init --recursive --jobs 8
git clone --recursive --jobs 8 [URL to Git repo]
# short version
git submodule update --init --recursive -j 8
```
