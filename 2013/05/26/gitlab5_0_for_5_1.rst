Gitlabを5.0から5.1にあげてみた
===============================

バージョンアップが早ことで有名なGitlab。月に一回くらいあるんだっけ

2013/05/26現在は5.2がリリースされている

まずは5.0 -> 5.1にしてみる

.. more::

=============
手順メモ
=============

※自分の環境はCentOS5

基本的には `公式の手順どおり。 <https://github.com/gitlabhq/gitlabhq/blob/master/doc/update/5.0-to-5.1.md>`_


Stop Server
------------

.. code-block:: bash

 /etc/init.d/gitlab stop

Get latest Code
-----------------

.. code-block:: bash

 cd /home/git/gitlab
 sudo -u git -H git fetch
 sudo -u git -H git checkout 5-1-stable

Update gitlab-shell
---------------------

.. code-block:: bash

 cd /home/git/gitlab-shell
 sudo -u git -H git fetch
 sudo -u git -H git checkout v1.3.0


Install libs, migratins etc
----------------------------

.. code-block:: bash

 cd /home/git/gitlab
 sudo rm tmp/sockets/gitlab.socket
 sudo -u git -H cp config/puma.rb.example config/puma.rb
  
 sudo -u git -H bundle install --without development test postgres --deployment
 sudo -u git -H bundle exec rake db:migrate RAILS_ENV=production
 sudo -u git -H bundle exec rake migrate_merge_requests RAILS_ENV=production

Update init.d script with a new one
-------------------------------------

.. code-block:: bash

 sudo rm /etc/init.d/gitlab
 sudo curl --output /etc/init.d/gitlab https://raw.github.com/gitlabhq/gitlab-recipes/5-1-stable/init.d/gitlab
 sudo chmod +x /etc/init.d/gitlab


Mysql grant privileges
------------------------

.. code-block:: bash

 mysql -u root -p
 mysql> GRANT LOCK TABLES ON `gitlabhq_production`.* TO 'gitlab'@'localhost';
 mysql> \q

ここでmysqlのパスを忘れる

`ここ <http://blog.layer8.sh/ja/2011/12/09/mysql%E3%81%AEroot%E3%81%AE%E3%83%91%E3%82%B9%E3%83%AF%E3%83%BC%E3%83%89%E3%82%92%E5%BF%98%E3%82%8C%E3%81%9F%E5%A0%B4%E5%90%88%E3%81%AE%E5%AF%BE%E5%87%A6%E6%B3%95/>`_ を参考に対処

自分の環境の時の対処は以下

.. code-block:: bash

 # セーフモードでログイン
 # 殺して
 killall mysqld
 # セーフモードで起動
 /usr/bin/mysqld_safe --user=root --skip-grant-tables &

さらにもう一つコンソールを立ち上げ

.. code-block:: bash

 mysql mydql
 mysql > update user set Password=null where Host='localhost' and User='root';
 mysql > \q
 # mysqld 再起動
 /etc/rc.d/init.d/mysqld restart
 # パス設定(パスなしで入れるはず)
 mysql -u root
 mysql > set password for root@localhost=password('ぱすわーど');

んで実行


Start application
-------------------

.. code-block:: bash

 # ドキュメントでは以下だが
 # sudo service gitlab start
 # 自分は/etc/init.d/gitlab startで実行
 /etc/init.d/gitlab start

そしてアクセスしてみる(自分の場合はポートを設定していたのでhttp://www.example.com:XXXXにアクセス)

アクセスできない...

**原因**

アプリケーションサーバunicornからpumaに変わった

上記の変更によりunicorn時にはlistenで直接アクセスするポートを指定できたが、pumaでは出来なくなってる

**追記:バーチャルホスト利用しなくても普通に出来た**

**対処**

Apacheのバーチャルホストを利用


バーチャルホストの設定
------------------------

-------------
pumaの設定
-------------

.. code-block:: bash

 su git
 vi /home/git/gitlab/config/puma.rb
 #↓をコメントアウトする
 #bind "unix://#{application_path}/tmp/sockets/gitlab.socket"
 #以下を有効にする
 bind 'tcp://0.0.0.0:ぽーと'


ポートの部分は自分の環境に合わせて変更


-------------
Apacheの設定
-------------

/etc/httpd/conf.d/virtualhost.confに以下の内容のファイルを作成

.. code-block:: bash

 NameVirtualHost *:80
 NameVirtualHost *:自分の設定したいぽーと
  
 <VirtualHost *:80>
     ServerName "www.yourdomain"
 </VirtualHost>
 <VirtualHost *:"自分の設定したいぽーと">
     DocumentRoot /home/git/gitlab/public
     proxypass / www.yourdomain:"pumaの設定で指定したポート"/
     proxypassreverse / www.yourdomain:"pumaの設定で指定したポート"/
     ProxyPreserveHost On
 </VirtualHost>


80は今まで通りにアクセスさせる

さらに/etc/httpd/conf/httpd.confに以下を追加

.. code-block:: bash

 Listen 80
 Listen "自分の設定したいぽーと"
  
 #
 # Load config files from the config directory "/etc/httpd/conf.d".
 #
 Include conf.d/*.conf

Include conf.d/*.confはデフォルトで有効になっている気がする

.. /*

---------
再起動
---------

.. code-block:: bash

 /etc/init.d/httpd restart
 /etc/init.d/gitlab stop
 /etc/init.d/gitlab sart

http://www.example.com:XXXXにアクセスしてみる


.. image:: ../../../_image/gitlab_login.png

でたー！

|

----

================
まとめ
================

5.0から5.1のアップデートは楽チンでしたな

そう5.0から5.1は...

5.1から5.2へつづく

----

.. 

.. author:: default
.. categories:: Gitlab
.. tags:: Gitlab
.. comments::
