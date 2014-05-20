Tinkererをビルドする際に'ascii' codec can't encode charactersになる問題
========================================================================

Tinkererをjenkinsで行うとエラーになって困っていたところ

Sphinxのスペシャリストが揃う「新宿Bookathon」で聞いてみたら一瞬で解決したのでメモとして残しておきます。

.. more::

============================
問題になっていたこと
============================

* jenkinsでtinker -bを実施すると'ascii' codec can't encode charactersが発生してビルドが失敗してしまう


.. image:: ../../../_image/jenkins_error.png

======
原因
======

ログを見てみると

.. code:: text
 
 # Sphinx version: 1.2.2
 # Python version: 2.6.6
 # Docutils version: 0.11 release
 # Jinja2 version: 2.7.2
 # Loaded extensions:
 #   tinkerer.ext.disqus from /usr/lib/python2.6/site-packages/tinkerer/ext/disqus.pyc
 #   sphinxcontrib.gist from /usr/lib/python2.6/site-packages/sphinxcontrib/gist/__init__.pyc
 #   sphinxcontrib.blockdiag from /usr/lib/python2.6/site-packages/sphinxcontrib/blockdiag.pyc
 #   sphinxcontrib.twitter from /usr/lib/python2.6/site-packages/sphinxcontrib/twitter/__init__.pyc
 #   sphinx.ext.oldcmarkup from /usr/lib/python2.6/site-packages/Sphinx-1.2.2-py2.6.egg/sphinx/ext/oldcmarkup.pyc
 #   tinkerer.ext.blog from /usr/lib/python2.6/site-packages/tinkerer/ext/blog.pyc
 Traceback (most recent call last):
   File "/usr/lib/python2.6/site-packages/Sphinx-1.2.2-py2.6.egg/sphinx/cmdline.py", line 254, in main
     app.build(force_all, filenames)
   File "/usr/lib/python2.6/site-packages/Sphinx-1.2.2-py2.6.egg/sphinx/application.py", line 212, in build
     self.builder.build_update()
   File "/usr/lib/python2.6/site-packages/Sphinx-1.2.2-py2.6.egg/sphinx/builders/__init__.py", line 214, in build_update
     'out of date' % len(to_build))
   File "/usr/lib/python2.6/site-packages/Sphinx-1.2.2-py2.6.egg/sphinx/builders/__init__.py", line 279, in build
     self.finish()
   File "/usr/lib/python2.6/site-packages/Sphinx-1.2.2-py2.6.egg/sphinx/builders/html.py", line 454, in finish
     self.handle_page(pagename, context, template)
   File "/usr/lib/python2.6/site-packages/Sphinx-1.2.2-py2.6.egg/sphinx/builders/html.py", line 780, in handle_page
     f = codecs.open(outfilename, 'w', encoding, 'xmlcharrefreplace')
   File "/usr/lib64/python2.6/codecs.py", line 881, in open
     file = __builtin__.open(filename, mode, buffering)
 UnicodeEncodeError: 'ascii' codec can't encode characters in position 47-49: ordinal not in range(128)

ログからファイルオープンで失敗している。しかも文字コードの問題で。

上記からTinkererが利用しているファイルでマルチバイトのファイルがないか検索をかける `@tk0miyaさん <https://twitter.com/tk0miya>`_

すると **blog/html/tags/その他.html** というファイルがヒット。これが読み込めなくてエラーになっていた模様。

ただいつもログインしているユーザでtinker -b してもエラーにならなかったので何故かなーと思っていたら

jenkinsのlocaleの設定がLANG=Cだったためエラーになっていたとのこと。

通常のユーザはja_JP.UTF-8になっていた。

よってjenkinsのビルドスクリプトにLANG=ja_JP.UTF-8を設定すれば直ることがわかりました。

==========
まとめ
==========

エラーログから原因の本質にたどり着く力がないことを痛感しました。

エラー解決に手伝ってくれた `@tk0miyaさん <https://twitter.com/tk0miya>`_ `@usaturnさん <https://twitter.com/usaturn>`_ ありがとうございました！

----

======
補足
======

今回の問題で `@tk0miyaさん <https://twitter.com/tk0miya>`_ が仰っていた対応方法

* ファイルに吐かれる可能性があるtagsディレクティブなどではマルチバイトは使わない

* tagsディレクティブなどで日本語を使う場合はLANGにja_JP.UTF-8を設定する

前者はtagsディレクティブなどにはマルチバイトを利用出来ない点がデメリット。

後者はURLにマルチバイトが入ってしまう(デメリットではないかもしれないですが)

どちらを採用するかは運用するルールやポリシーによって使いわけましょうとのことでした。


.. author:: default
.. categories:: Tinkerer
.. tags:: Tinkerer
.. comments::
