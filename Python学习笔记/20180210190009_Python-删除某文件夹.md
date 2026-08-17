# Python 删除某文件夹
[参考文章](https://askubuntu.com/questions/555318/delete-all-files-except-files-with-the-extension-pdf-in-a-directory/555326)
- os.remove() will remove a file
- os.rmdir() will remove an empty directory
- [shutil.rmtree()](https://docs.python.org/3/library/shutil.html#shutil.rmtree) will delete a directory and all its contents

```python
# 删除某个目录及里面所有内容，第二个参数为True时忽略所有错误中断
shutil.rmtree('<path>', True)
```



