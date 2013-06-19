Gitlabでpush出来ない問題
===============================

OSをCentOS5からScientific Linuxに変えて再セットアップしたところちょっとはまった

pushすると以下のようなエラーがでる

.. code-block:: bash

 git push -u -v origin master
 Pushing to ssh://git@www.example.com:XXXX/hoge.git
 fatal: The remote end hung up unexpectedly

原因
 /home/git/gitlab-shell/config.ymlのgitlab_urlが違っていた。自分はポートを変更していたのでそこを含めて記述しないといけなかった

.. code-block:: diff

 --- gitlab-shell/config.yml.bad 2013-06-17 03:36:30.319129785 +0900
 +++ gitlab-shell/config.yml     2013-06-17 03:35:59.668130013 +0900
 @@ -2,7 +2,7 @@
  user: git
 
  # Url to gitlab instance. Used for api calls. Should be ends with slash.
 -gitlab_url: "http://www.example.com/"
 +gitlab_url: "http://www.example.com:ポート/"
 
  http_settings:
  #  user: someone

上記をポートまで指定することでpushできるようにった


.. author:: default
.. categories:: Gitlab
.. tags:: Gitlab
.. comments::
