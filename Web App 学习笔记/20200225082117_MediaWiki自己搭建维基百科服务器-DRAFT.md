#  MediaWiki自己搭建维基百科服务器  [DRAFT]

[Refer to: How to Setup MediaWiki with Docker](https://wiki.chairat.me/books/docker/page/how-to-setup-mediawiki-with-docker)

First try:
```sh
docker run --name some-mediawiki -p 8080:80 -d mediawiki
open http://localhost:8080
docker cp LocalSettings.php mediawiki:/var/www/html
open http://localhost:8080
```

More specific settings:
```yaml
# docker-compose.yaml
# Access via "http://localhost:8080"
#   (or "http://$(docker-machine ip):8080" if using docker-machine)
version: '3'
services:
  mediawiki:
    image: mediawiki
    # restart: always
    ports:
      - 8080:80
    # links:
    #   - database
    volumes:
      - ./images:/var/www/html/images
      - ./data:/var/www/data
      - ./LocalSettings.php:/var/www/html/LocalSettings.php
    environment:
      MEDIAWIKI_SERVER: http://localhost:8080
      MEDIAWIKI_SITENAME: MyWiki
      MEDIAWIKI_LANGUAGE_CODE: en
      MEDIAWIKI_SECRET_KEY: mysecret
      MEDIAWIKI_DB_TYPE: sqlite
      MEDIAWIKI_DB_NAME: wikidb
      MEDIAWIKI_ENABLE_UPLOADS: 1
      MEDIAWIKI_EXTENSION_VISUAL_EDITOR_ENABLED: 1
      MEDIAWIKI_DEFAULT_SKIN: vector
      MEDIAWIKI_DEBUG: 1
```

```sh
docker-compose up
```


## 安装自带插件

```php

```

## 安装第三方插件

必备插件：VisualEditor编辑器：
```sh
cd extensions
# 必须要配合当前的mediawiki的版本：1.34
git clone -b REL1_34 https://gerrit.wikimedia.org/r/mediawiki/extensions/VisualEditor.git
```

WYSIWYG编辑器：
```sh
cd wiki/extensions/
git clone https://github.com/Mediawiki-wysiwyg/WYSIWYG-CKeditor.git WYSIWYG-src
ln -s WYSIWYG-src/WYSIWYG  WYSIWYG
ln -s WYSIWYG-src/SemanticForms SemanticForms
mv WikiEditor WikiEditor-org
ln -s WYSIWYG-src/WikiEditor WikiEditor
```


## 利用Docker直接安装所有必备插件

> 因为各种插件的安装依赖实在太难找了，所以直接docker解决。

参考：https://github.com/pastakhov/compose-mediawiki-ubuntu
这个Docker是维护的最好最全的一份。

没有网络问题的话，下面几句就能完成安装运行：
```sh
git clone https://github.com/pastakhov/compose-mediawiki-ubuntu.git
cd compose-mediawiki-ubuntu
docker-compose up
```

如果遇到网络问题，比如git下载，那么就需要手动在网络方便的地方提前下载好：
```sh
#download.sh

mkdir required && cd required
export MW_VERSION=REL1_29

git clone --depth 1 -b $MW_VERSION https://gerrit.wikimedia.org/r/p/mediawiki/core.git
git clone --depth 1 -b $MW_VERSION https://gerrit.wikimedia.org/r/mediawiki/skins/Vector
git clone --depth 1 -b $MW_VERSION https://gerrit.wikimedia.org/r/mediawiki/skins/Modern
git clone --depth 1 -b $MW_VERSION https://gerrit.wikimedia.org/r/mediawiki/skins/MonoBook
git clone --depth 1 -b $MW_VERSION https://gerrit.wikimedia.org/r/mediawiki/skins/CologneBlue

git clone --depth 1 -b $MW_VERSION https://gerrit.wikimedia.org/r/p/mediawiki/extensions/ConfirmEdit
git clone --depth 1 -b $MW_VERSION https://gerrit.wikimedia.org/r/p/mediawiki/extensions/Gadgets
git clone --depth 1 -b $MW_VERSION https://gerrit.wikimedia.org/r/p/mediawiki/extensions/Nuke
git clone --depth 1 -b $MW_VERSION https://gerrit.wikimedia.org/r/p/mediawiki/extensions/ParserFunctions
git clone --depth 1 -b $MW_VERSION https://gerrit.wikimedia.org/r/p/mediawiki/extensions/Renameuser
git clone --depth 1 -b $MW_VERSION https://gerrit.wikimedia.org/r/p/mediawiki/extensions/WikiEditor
git clone --depth 1 -b $MW_VERSION https://gerrit.wikimedia.org/r/p/mediawiki/extensions/Cite
git clone --depth 1 -b $MW_VERSION https://gerrit.wikimedia.org/r/p/mediawiki/extensions/ImageMap
git clone --depth 1 -b $MW_VERSION https://gerrit.wikimedia.org/r/p/mediawiki/extensions/InputBox
git clone --depth 1 -b $MW_VERSION https://gerrit.wikimedia.org/r/p/mediawiki/extensions/Interwiki
git clone --depth 1 -b $MW_VERSION https://gerrit.wikimedia.org/r/p/mediawiki/extensions/LocalisationUpdate
git clone --depth 1 -b $MW_VERSION https://gerrit.wikimedia.org/r/p/mediawiki/extensions/PdfHandler
git clone --depth 1 -b $MW_VERSION https://gerrit.wikimedia.org/r/p/mediawiki/extensions/Poem
git clone --depth 1 -b $MW_VERSION https://gerrit.wikimedia.org/r/p/mediawiki/extensions/SpamBlacklist
git clone --depth 1 -b $MW_VERSION https://gerrit.wikimedia.org/r/p/mediawiki/extensions/TitleBlacklist
git clone --depth 1 -b $MW_VERSION https://gerrit.wikimedia.org/r/p/mediawiki/extensions/CiteThisPage

git clone --depth 1 -b $MW_VERSION https://gerrit.wikimedia.org/r/p/mediawiki/extensions/SyntaxHighlight_GeSHi
git clone --depth 1 -b $MW_VERSION https://gerrit.wikimedia.org/r/p/mediawiki/extensions/Echo
git clone --depth 1 -b $MW_VERSION https://gerrit.wikimedia.org/r/p/mediawiki/extensions/Thanks
git clone --depth 1 -b $MW_VERSION https://gerrit.wikimedia.org/r/p/mediawiki/extensions/CheckUser
git clone --depth 1 -b $MW_VERSION https://gerrit.wikimedia.org/r/p/mediawiki/extensions/Flow
git clone --depth 1 -b $MW_VERSION https://gerrit.wikimedia.org/r/p/mediawiki/extensions/Babel
git clone --depth 1 -b $MW_VERSION https://gerrit.wikimedia.org/r/p/mediawiki/extensions/cldr
git clone --depth 1 -b $MW_VERSION https://gerrit.wikimedia.org/r/p/mediawiki/extensions/CleanChanges
git clone --depth 1 -b $MW_VERSION https://gerrit.wikimedia.org/r/p/mediawiki/extensions/UniversalLanguageSelector
git clone --depth 1 -b $MW_VERSION https://gerrit.wikimedia.org/r/p/mediawiki/extensions/VisualEditor \
    && cd VisualEditor && git submodule update --init && cd ..
git clone --depth 1 -b $MW_VERSION https://gerrit.wikimedia.org/r/p/mediawiki/extensions/CirrusSearch
git clone --depth 1 -b $MW_VERSION https://gerrit.wikimedia.org/r/p/mediawiki/extensions/Elastica
git clone --depth 1 -b $MW_VERSION https://gerrit.wikimedia.org/r/p/mediawiki/extensions/MultimediaViewer
git clone --depth 1 -b $MW_VERSION https://gerrit.wikimedia.org/r/p/mediawiki/extensions/MobileFrontend
git clone --depth 1 -b $MW_VERSION https://gerrit.wikimedia.org/r/p/mediawiki/extensions/ElectronPdfService
```

然后把Dockerfile一下：
```sh
# 所有git clone的地方，都替代成类似这种：
ADD required/VisualEditor $MW_HOME/extensions/VisualEditor
RUN set -x \
    && cd $MW_HOME && cd /extensions/VisualEditor \
    && git submodule update --init
```
