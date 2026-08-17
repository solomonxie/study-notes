# Python处理XML

[参考：The Hitchhiker's Guide to Python: XML parsing](https://docs.python-guide.org/scenarios/xml/)

```xml
<mydocument has="an attribute">
  <and>
    <many>elements</many>
    <many>more elements</many>
  </and>
  <plus a="complex">
    element as well
  </plus>
</mydocument>
```


## xmltodict

安装：`pip install xmltodict --user`

```py
import xmltodict

with open('path/to/file.xml') as fd:
    doc = xmltodict.parse(fd.read())

doc['mydocument']['@has'] # == u'an attribute'
doc['mydocument']['and']['many'] # == [u'elements', u'more elements']
doc['mydocument']['plus']['@a'] # == u'complex'
doc['mydocument']['plus']['#text'] # == u'element as well'
```
