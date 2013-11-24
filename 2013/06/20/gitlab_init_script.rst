Gitlabの/etc/init.d/gitlabについて
======================================

5.2のスクリプトをそのまま利用するとエラーになっていた

bundleがないって怒られる

そんなはずはない

コンソールから叩くと普通にある

パスが通ってないのか？

.. more::

.. code-block:: bash

 which bundle
 /usr/local/bin/bundle


/usr/local/binにパスを通してみる

.. code-block:: bash

 --- gitlab.org  2013-06-12 01:37:53.931164955 +0900
 +++ gitlab      2013-06-12 23:01:10.918884056 +0900
 @@ -52,7 +52,7 @@
    else
      if [ `whoami` = root ]; then
        execute "rm $SOCKET_PATH/gitlab.socket"
 -      execute "RAILS_ENV=production bundle exec puma $DAEMON_OPTS"
 +      execute "PATH=$PATH:/usr/local/bin RAILS_ENV=production bundle exec puma $DAEMON_OPTS"
        execute "mkdir -p $PID_PATH && $START_SIDEKIQ  > /dev/null  2>&1 &"
        echo "$DESC started"
      fi
 @@ -83,7 +83,7 @@
      kill -USR2 `cat $WEB_SERVER_PID`
      execute "mkdir -p $PID_PATH && $STOP_SIDEKIQ  > /dev/null  2>&1 &"
      if [ `whoami` = root ]; then
 -      execute "mkdir -p $PID_PATH && $START_SIDEKIQ  > /dev/null  2>&1 &"
 +      execute "PATH=$PATH:/usr/local/bin mkdir -p $PID_PATH && $START_SIDEKIQ  > /dev/null  2>&1 &"
      fi
      echo "$DESC restarted."
    else

パスを通すことで起動するようになった

おそらく自分のユーザの作り方が悪かったっぽい

.. author:: default
.. categories:: Gitlab
.. tags:: Gitlab
.. comments::
