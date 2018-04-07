Gitlabを使ってみた
=====================

.. image:: ../../../_image/gitlab_logo.png
   :scale: 50%
   :align: center

やたらキモイロゴの `Gitlab <http://gitlab.org/>`_

githubのオープンソースクローンと呼ばれている。

.. more::

用途はたぶん以下に当てはまる場合

* githubでプライベートリポジトリ作るのにお金がかかるのがイヤ
* 社内の開発リポジトリを外部に出すのに抵抗がある

正直メンテを考えたらgithubのプライベートリポジトリを使った方がいいような気もする。それか `Bitbucket <https://bitbucket.org/>`_


入れ方は `gitlabのgithubのところに書いてある <https://github.com/gitlabhq/gitlabhq/blob/5-0-stable/doc/install/installation.md>`_ (2013/04/25現在は5.0が推奨) 

インストールはDebian系で書かれているけど、CentOS※でも必要なものを入れれば動いた

※CentOS5系


自分が入れた際のメモ
----------------------

..

----

|

-----------------------
必要なパッケージを用意
-----------------------

.. list-table:: 
   :widths: 10 10
   :header-rows: 1

   * - Debian系のパッケージ名
     - Redhat系のパッケージ名
   * - build-essential
     - ?(たぶんgcc gcc-c++ kernel-develあたり)
   * - zlib-dev
     - zlib-devel
   * - libyaml-dev
     - libyaml-devel
   * - libssl-dev
     - openssl-devel
   * - libgdbm-dev
     - gdbm-devel
   * - libreadline-dev
     - readline-devel
   * - libncurses5-dev
     - ncurses-devel
   * - libffi-dev
     - libffi-devel
   * - git-core
     - git-core
   * - openssh-server
     - openssh-server
   * - redis-server
     - redis
   * - postfix
     - postfix
   * - checkinstall
     - ないので手動
   * - libxml2-dev
     - libxml-devel
   * - libxslt-dev
     - libxslt-devel
   * - libcurl4-openssl-dev
     - libcurl-devel
   * - libicu-dev
     - libicu-devel


checkinstallだけは手動でいれる `ここ参照 <http://www.genteel.org/archives/132>`_

.. code-block:: bash

 wget http://asic-linux.com.mx/~izto/checkinstall/files/source/checkinstall-1.6.2.tar.gz
 tar xvf checkinstall-1.6.2.tar.gz
 cd checkinstall-1.6.2/
 make && make insatll

RPM化

.. code-block:: bash

 checkinstall

---------------------------
rubyのインストール(1.9.3)
---------------------------

自分の環境には1.8が入っていたのでいったんアンインストール

.. code-block:: bash

 yum remove ruby

1.9.3インストール

.. code-block:: bash

 curl --progress http://ftp.ruby-lang.org/pub/ruby/1.9/ruby-1.9.3-p327.tar.gz | tar xz
 cd ruby-1.9.3-p327/
 ./configure
 make && make install

BundlerGemのインストール

sudo gem install bundler

----------------------
Gitlabのユーザ作成
----------------------

.. code-block:: bash

 # 手順では以下だがCentOSなので
 # sudo adduser --disabled-login --gecos 'GitLab' git
 # こっち
 adduser -c 'GitLab' git

---------------------------
Gitlab shellのインストール
---------------------------

.. code-block:: bash

 su git
 cd /home/git
 git clone https://github.com/gitlabhq/gitlab-shell.git
 cd gitlab-shell
 cp config.yml.example config.yml
 # Edit config and replace gitlab_url
 # with something like 'http://domain.com/'
 vim config.yml
 'http://domain.com/'の部分を自分の環境に合わせて変更(自分の場合ポートも変えたのでそれを含め変更http://xxx.com:XXXXみたいに)
 あとsshポートを変更している人は'ssh_port'の部分を変更する
 ./bin/install

-------------------------------
データベースのセットアップ
-------------------------------

postgreでもいいみたいだけど、自分の場合はmysqlを利用

インストール

.. code-block:: bash

 yum install mysql-server mysql-devel

データベースのセットアップ

.. code-block:: bash

 mysql -u root -p
 mysql > CREATE USER 'gitlab'@'localhost' IDENTIFIED BY 'パスワード';
 mysql > CREATE DATABASE IF NOT EXISTS `gitlabhq_production` DEFAULT CHARACTER SET `utf8` COLLATE `utf8_unicode_ci`;
 mysql > GRANT SELECT, INSERT, UPDATE, DELETE, CREATE, DROP, INDEX, ALTER ON `gitlabhq_production`.* TO 'gitlab'@'localhost';
 mysql > \q
 sudo -u git -H mysql -u gitlab -p -D gitlabhq_production

-------------------------
Gitlabのソースの取得
-------------------------

.. code-block:: bash

 # gitにsu権限
 usermod -G wheel git
 cd /home/git
 sudo -u git -H git clone https://github.com/gitlabhq/gitlabhq.git gitlab
 cd /home/git/gitlab

--------------
Gitlabの設定
--------------

.. code-block:: bash

 cd /home/git/gitlab
 sudo -u git -H cp config/gitlab.yml.example config/gitlab.yml
 sudo -u git -H vim config/gitlab.yml
 # 自分の場合はlocalhostを変更した
 sudo chown -R git log/
 sudo chown -R git tmp/
 sudo chmod -R u+rwX  log/
 sudo chmod -R u+rwX  tmp/
 sudo -u git -H mkdir /home/git/gitlab-satellites
 sudo -u git -H mkdir tmp/pids/
 sudo chmod -R u+rwX  tmp/pids/
 sudo -u git -H cp config/unicorn.rb.example config/unicorn.rb
 vim config/unicorn.rb
 # 自分の場合はlistenポート変更

----------------------------
Gitlabの データベースの設定
----------------------------

.. code-block:: bash

 sudo -u git cp config/database.yml.mysql config/database.yml
 # データベースで設定したユーザとパスワードを指定
 vim config/database.yml


--------------------------
rubyパッケージの取得
--------------------------

.. code-block:: bash

 # reademeでは
 # sudo -u git -H bundle exec rake gitlab:setup RAILS_ENV=production
 # 自分はこっち(権限の関係かな)
 bundle exec rake gitlab:setup RAILS_ENV=production
 Administrator account created:

仮のアカウントが表示されるはず

-------------------
初期化スクリプト
-------------------

.. code-block:: bash

 sudo curl --output /etc/init.d/gitlab https://raw.github.com/gitlabhq/gitlab-recipes/master/init.d/gitlab
 sudo chmod +x /etc/init.d/gitlab


起動時に動くようにする

.. code-block:: bash

 sudo /sbin/chkconfig --level 2345 gitlab on

色々チェック

.. code-block:: bash

 bundle exec rake gitlab:env:info RAILS_ENV=production

上記で

.. code-block:: bash

 Git configured for git user? ... no
  Try fixing it:
   sudo -u git -H git config --global user.name  "GitLab"
   sudo -u git -H git config --global user.email "gitlab@localhost"

と言われたので

.. code-block:: bash

 git config --global user.name  "GitLab"
 git config --global user.email "gitlab@localhost"


--------------
Gitlabの起動
--------------

.. code-block:: bash

 bundle exec rake sidekiq:start RAILS_ENV=production

Gitlabのインストールガイドだとnginxだけど、自分はApacheなので特に何もせず

設定したURL:ポートにアクセスするとログイン画面が出てくる

.. image:: ../../../_image/gitlab_login.png
   :align: center

あとは `ここ <http://memocra.blogspot.jp/2012/02/gitlab.html>`_ を参考にユーザの設定を行う


**補足**

自分の場合コミット時にsshの権限まわりでエラーが出ていたので以下の対処を実施

.. code-block:: bash

 su git
 cd
 chmod 755 .ssh
 chmod 600 .ssh/authroized_keys

|

----

-----
感想
-----

普通はgithubでいいと思う。わざわざ構築したのはいつか会社とかでgitが主流になった時にgithubのプライベート案がけられた時に使いたいなーと思ったから。


----

..

.. author:: default
.. categories:: Gitlab
.. tags:: Gitlab
.. comments::
