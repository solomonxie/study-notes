# VIM内置文件浏览框NetRW

g:netrw_browse_split是重要的选项，直接影响体验：
```vim
 *g:netrw_browse_split*    when browsing, <cr> will open the file by:
                =0: re-using the same window  (default)
                =1: horizontally splitting the window first
                =2: vertically   splitting the window first
                =3: open file in new tab
                =4: act like "P" (ie. open previous window)
```

```vim
  *g:netrw_liststyle*		Set the default listing style:
                                = 0: thin listing (one file per line)
                                = 1: long listing (one file per line with time
				     stamp information and file size)
				= 2: wide listing (multiple files in columns)
				= 3: tree style listing
```
