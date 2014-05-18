Webサーバをapacheからnginxへ移行した際のgitlabでhttp経由のcloneができない問題
================================================================================

今更ですがapacheからnginxへ移行してみました。

その際にgitlabのhttp経由でのcloneができなくなったので、その時の対応メモしておきます。

.. more::

nginxへ移行した後にgitlabのリポジトリをcloneしてくると以下のエラーがでました。

.. code:: bash

 git clone XXX
 Cloning into 'XXX'...
 fatal: git fetch_pack: expected ACK/NAK, got '
 0008NAK
 0022Counting objects: 104, done.
 002eCompressing objects: 100% (88/88), done.
 2004PACK'


現象としてはsshでのcloneは出来ていてhttp経由のみエラーになるというもの。

=======
解決法
=======

調べてみると `fatal: git fetch_pack: expected ACK/NAK #120 <https://github.com/gitlabhq/gitlab-shell/issues/120>`_ に理由が書かれていて、どうやらnginxのバグ?のようだとのこと。

さらに `http clone doesnt work over nginx(gitlab latest master)#5774 <https://github.com/gitlabhq/gitlabhq/issues/5774>`_ にnginxのバージョンを1.4にしたら直ったとの報告があったので試してみることに。

自分が利用しているSientific Linuxのyumで入れたnginxは1.0だったのでrpmを利用して最新のものにアップデートしました。

`Nginxを公式サイトから最新版をインストールする(CentOS/ScientificLinux編) <http://server-setting.info/centos/apache-nginx-1-rpm-nginx-install.html>`_ ここを参考に以下のようにしました。

.. code:: bash

 # 自分の環境はSL6なので6のrpmを取得
 wget http://nginx.org/packages/centos/6/noarch/RPMS/nginx-release-centos-6-0.el6.ngx.noarch.rpm
 sudo rpm -Uvh nginx-release-centos-6-0.el6.ngx.noarch.rpm
 sudo yum install nginx.x86_64
 
上記インストール後、nginxを再起動したところhttp経由でもcloneできるようになりました。

.. author:: default
.. categories:: gitlab
.. tags:: gitlab
.. comments::
