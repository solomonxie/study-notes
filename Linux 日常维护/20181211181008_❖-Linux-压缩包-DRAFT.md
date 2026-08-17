# ❖ Linux 压缩包 [DRAFT]

## .zip
解压：unzip FileName.zip
压缩：zip FileName.zip DirName

解压多个文件到各自独立目录：
参考：https://askubuntu.com/questions/518370/extract-several-zip-files-each-in-a-new-folder-with-the-same-name-via-ubuntu-t
```sh
for i in *.zip; do unzip "$i" -d "${i%%.zip}"; done
```
———————————————


## .tar 
解包：tar xvf FileName.tar
打包：tar cvf FileName.tar DirName
（注：tar是打包，不是压缩！）
———————————————

## .gz
解压1：gunzip FileName.gz
解压2：gzip -d FileName.gz
压缩：gzip FileName

## .tar.gz 和 .tgz
解压：tar xzvf FileName.tar.gz
压缩：tar czvf FileName.tar.gz DirName
———————————————

## .bz2
解压1：bzip2 -d FileName.bz2
解压2：bunzip2 FileName.bz2
压缩： bzip2 -z FileName

## .tar.bz2
解压：tar xjvf FileName.tar.bz2
压缩：tar cjvf FileName.tar.bz2 DirName
———————————————

## .bz
解压1：bzip2 -d FileName.bz
解压2：bunzip2 FileName.bz
压缩：未知

## .tar.bz
解压：tar xjvf FileName.tar.bz
压缩：未知
———————————————

## .xz
解压1：xz -d FileName.xz
压缩：

———————————————

## .tar.xz
解压1：xz -d FileName.tar.xz && tar -xvf FileName.tar
解压2：tar -xJvf FileName.tar.xz
压缩：

———————————————
## .Z
解压：uncompress FileName.Z
压缩：compress FileName
.tar.Z

解压：tar xZvf FileName.tar.Z
压缩：tar xZvf FileName.tar.Z DirName
———————————————

## .rar
解压：rar x FileName.rar
压缩：rar a FileName.rar DirName
———————————————

## .lha
解压：lha -e FileName.lha
压缩：lha -a FileName.lha FileName
———————————————

## .rpm
解包：rpm2cpio FileName.rpm | cpio -div
———————————————

## .deb
解包：ar p FileName.deb data.tar.gz | tar zxf -
———————————————

## .tar .tgz .tar.gz .tar.Z .tar.bz .tar.bz2 .zip .cpio .rpm .deb .slp .arj .rar .ace .lha .lzh .lzx .lzs .arc .sda .sfx .lnx .zoo .cab .kar .cpt .pit .sit .sea
解压：sEx x FileName.*
压缩：sEx a FileName.* FileName

