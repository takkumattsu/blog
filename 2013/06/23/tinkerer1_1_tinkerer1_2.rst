Tinkerer1.1からTinkerer1.2にあげた際にはまったこと
=====================================================

Tinkerer1.2がリリースされたということでアップデートして使ってみたところエラーが出た

その時の対処メモ

.. more::

エラーは以下

.. code-block:: bash

 tinker -b
 Making output directory...
 Running Sphinx v1.2b1
 loading translations [ja]... done
 loading pickled environment... not yet created

 Theme error:
 no theme named 'minimal' found, inherited by 'custom_minimal'

minimalテーマなんてねーです

って言ってます

1.1ではあったのに(´･ω･`)

どうやらhtml5ベース？のminimal5を使えとのこと

そもそも自分のTinkererは

`Tinkererを使ってブログを作るまでのメモ <http://www.shomah4a.net/2013/02/26/setup_tinkerer.html>`_ を参考にカスタマイズをしています。

そのせいでテーマをminimalからminimal5にただ置き換えただけではエラーになる

=====
原因
=====

そもそもtwitterボタンは_themes/custom_minimal/page.htmlや_themes/custom_minimal/aggregated.htmlを配置して追加している。
そこで利用しているpage.htmlとかはminimalをベースにしている(と思われる)。なのでminimal5にするとエラーになる。

====
対処
====

minimal5のpage.htmlやaggregated.htmlをもとにtwitterボタン配置の修正を入れる

=====
手順
=====

minimal5のpage.htmlやaggregated.htmlはboilerplateに含まれている(minimal5はboilerplateを継承？している)

自分の環境だと以下

**aggregated.html**

.. code-block:: bash

 find /lib -type f | grep aggregated.html
 /lib/python2.7/site-packages/tinkerer/themes/boilerplate/aggregated.html
 /lib/python2.7/site-packages/Tinkerer-1.2-py2.7.egg/tinkerer/themes/boilerplate/aggregated.html


**page.html**

.. code-block:: bash

 find /lib -type f | grep page.html
 /lib/python2.7/site-packages/Sphinx-1.1.3-py2.7.egg/sphinx/themes/basic/page.html
 /lib/python2.7/site-packages/Sphinx-1.2b1-py2.7.egg/sphinx/themes/basic/page.html
 /lib/python2.7/site-packages/tinkerer/themes/boilerplate/page.html
 /lib/python2.7/site-packages/tinkerer/themes/flat/page.html
 /lib/python2.7/site-packages/Tinkerer-1.2-py2.7.egg/tinkerer/themes/boilerplate/page.html
 /lib/python2.7/site-packages/Tinkerer-1.2-py2.7.egg/tinkerer/themes/flat/page.html


_themes/custom_minimal5/にコピーしてくる

.. code-block:: bash

 cp -f /lib/python2.7/site-packages/Tinkerer-1.2-py2.7.egg/tinkerer/themes/boilerplate/page.html _themes/custom_minimal5/
 cp -f  /lib/python2.7/site-packages/Tinkerer-1.2-py2.7.egg/tinkerer/themes/boilerplate/aggregated.html _themes/custom_minimal5/

ちなみにtheme.confは以下

.. code-block:: bash

 cat _themes/custom_minimal5/theme.conf

 [theme]
 inherit = minimal5

んでconf.pyのテーマをcustom_minimal5に変更

とりあえず上記の対処でうまくいった

.. author:: default
.. categories:: Tinkerer
.. tags:: Tinkerer
.. comments::
