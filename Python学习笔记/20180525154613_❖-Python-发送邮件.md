# ❖ Python 发送邮件

> 程序人员对于`邮件自动化`的日常需求还是很高的。但是入过了Linux的命令行邮件客户端如`Sendmail`, `Mutt`, `Alpine`等坑之后，发现现代其实很少人真的在用它们实现邮件自动化，根据搜索引擎里相关文章的数量就可知一二。取而代之的是，现代都在用Python或PHP等编程语言直接实现。Python更是自带一套模块实现邮件发送。

先上示例代码，之后再详解。

注：全部代码在Python3环境下测试通过，正常使用，正常显示，无需任何外置模块。

[参考：菜鸟教程 - Python SMTP发送邮件](http://www.runoob.com/python/python-email.html)
[参考：简单三步，用 Python 发邮件](https://zhuanlan.zhihu.com/p/24180606)

## 发送HTML格式的漂亮邮件

```py
import smtplib
from email.mime.text import MIMEText

# Settings of sender's server
host = 'smtp.aliyun.com'
sender = 'Jason@aliyun.com'
user = 'Jason@aliyun.com'
password = input('Please type your password: ')
to = ['Jason@outlook.com']

# Content of email
subject = 'Python send html email test'
with open('./test.html', 'r') as f:
    content = f.read()

# Settings of the email string
email = MIMEText(content,'html','utf-8')
email['Subject'] = subject
email['From'] = sender
email['To'] = to[0]
msg = email.as_string()

# Login the sender's server
print('Logging with server...')
smtpObj = smtplib.SMTP() 
smtpObj.connect(host, 25)
smtpObj.login(user, password)
print('Login successful.')

# Send email
smtpObj.sendmail(sender, to, msg) 
smtpObj.quit() 
print('Email has been sent')
```

## 发送带附件的邮件

```py
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage

# Settings of sender's server
host = 'smtp.aliyun.com'
sender = 'Jason@aliyun.com'
user = 'Jason@aliyun.com'
password = input('Please type your password: ')
to = ['Jason@outlook.com']

# Make content of email
subject = 'Python send email with attachments'
with open('./test.html', 'r') as f:
    content = MIMEText(f.read(),'html','utf-8')
    content['Content-Type'] = 'text/html'
    print('Loaded content.')

# Make txt attachment
with open('./txt.md', 'r') as f:
    txt = MIMEText(f.read(),'plain','utf-8')
    txt['Content-Type'] = 'application/octet-stream'
    txt['Content-Disposition'] = 'attachment;filename="txt.md"'
    print('Loaded txt attachment file.')

# Make image attachment
with open('./pic.png', 'rb') as f:
    img = MIMEImage(f.read())
    img['Content-Type'] = 'application/octet-stream'
    img['Content-Disposition'] = 'attachment;filename="pic.png"'
    print('Loaded image attachment file.')

# Attach content & attachments to email
email = MIMEMultipart()
email.attach(content)
email.attach(txt)
email.attach(img)

# Settings of the email string
email['Subject'] = subject
email['From'] = sender
email['To'] = to[0]
msg = email.as_string()

# Login the sender's server
print('Logging with server...')
smtpObj = smtplib.SMTP() 
smtpObj.connect(host, 25)
smtpObj.login(user, password)
print('Login successful.')

# Send email
smtpObj.sendmail(sender, to, msg) 
smtpObj.quit() 
print('Email has been sent')
```


## 发送邮件大杀器：Yagmail

> 之所以放在最后，是相衬托出传统的发送邮件是多繁琐多麻烦，实际上我们需要的只是超级简单的东西。Yagmail正是为了实现这个而生的，一句话就可以完成所有的登录、发送文字、HTML、附件等功能。

[参考Github：yagmail -- Yet Another GMAIL/SMTP client](https://github.com/kootenpv/yagmail)

一句话发送邮件：
```py
yagmail.SMTP('username').send('to@a.com', 'Subject', 'This is the body')
```

正常一点的发送邮件：
```py
import yagmail

yag = yagmail.SMTP('user', 'password', host='server.com', port='123')
contents = [
    'This is the body, and here is just text http://somedomain/image.png',
    'You can find a file attached.', 
    './dataset/pic.jpg'
]
yag.send('solomonxie@outlook.com', 'yagmail tst', contents)
```
