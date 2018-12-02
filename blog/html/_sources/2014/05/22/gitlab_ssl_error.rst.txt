GitlabをHTTPSにしたときにSSHアクセスできない問題
=================================================

HTTPSしてみたときにはまったのでメモ。

こういうのは偉大な先人の方がいるもので今回も以下を参考に解決できました。

 `何かの会長のブログ gitlabの設定でハマった点 <http://mudanakaigi.blogspot.jp/2013/10/gitlab.html>`_

.. more::

上記を見るとHTTPS化する際にgitlab-shell/config.ymlの欄にサーバ証明書を指定しないといけないらしい。

.. code-block:: diff

  --- /home/git/gitlab-shell/config.yml.example	2014-05-22 02:08:30.993796798 +0900
  +++ /home/git/gitlab-shell/config.yml	2014-05-22 23:24:26.058585592 +0900
  @@ -1,22 +1,17 @@
   # GitLab user. git by default
   user: git
   
  -# Url to gitlab instance. Used for api calls. Should end with a slash.
  -gitlab_url: "http://127.0.0.1/"
  +gitlab_url: "https://127.0.0.1/"
   
   http_settings:
   #  user: someone
   #  password: somepass
  -#  ca_file: /etc/ssl/cert.pem
  -#  ca_path: /etc/pki/tls/certs
  -   self_signed_cert: false
  +  ca_file: /etc/XXX
  +  ca_path: /etc/YYY
  +  self_signed_cert: true
   
   # Repositories path
   repos_path: "/home/git/repositories"
  
あとgitlab_urlもhttpsに変更した。
 
.. author:: default
.. categories:: Gitlab
.. tags:: Gitlab
.. comments::


