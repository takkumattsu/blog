Tinkererを使ってみた
=======================

Tinkererとは？

TinkererとはSphinxでブログを作成するツール。

もともとWordPressを利用していたんだけど、html形式？WYSIWYGモード？とかに慣れなくて微妙に思っていた。

.. more::

`numa08 <https://twitter.com/numa08>`_ がブログをはてなに移したときに

 `Markdown いいね！！`

って〆てた


|

**はてなはMarkdownでかけるのか！**

あ、オレもはてなにしよう

と思ったのですが、どうせならreStructuredTextで書けないかなーと探したのがTinkererでした。
(インストール方法は `pip install tinkerer` `公式サイト <http://tinkerer.me/index.html>`_ に色々書いてある)

普段reStruectredTextを利用しているから書きやすくてたまらん！

基本的にはSphinxで利用できる機能はそのまま使えるので以下みたいなこともできる


=====================
ブロック図
=====================

ソース

.. code-block:: rst

 .. blockdiag::
    :desctable:
 
    blockdiag {
       A -> B -> C;
       A -> D -> E;
       A -> F -> G;
       A [label = "A画面", description = "A画面の説明"];
       B [label = "B画面", description = "B画面の説明"];
       C [label = "C画面", description = "C画面の説明"];
       D [label = "D画面", description = "D画面の説明"];
       E [label = "E画面", description = "E画面の説明"];
       F [label = "F画面", description = "F画面の説明"];
       G [label = "G画面", description = "G画面の説明"];
    }

実際の表示

.. blockdiag::
   :desctable:

   blockdiag {
      A -> B -> C;
      A -> D -> E;
      A -> F -> G;
      A [label = "A画面", description = "A画面の説明"];
      B [label = "B画面", description = "B画面の説明"];
      C [label = "C画面", description = "C画面の説明"];
      D [label = "D画面", description = "D画面の説明"];
      E [label = "E画面", description = "E画面の説明"];
      F [label = "F画面", description = "F画面の説明"];
      G [label = "G画面", description = "G画面の説明"];
   }

==================
Tweet埋め込み
==================

ソース

.. code-block:: rst

 .. tweet:: https://twitter.com/NorsteinBekkler/status/347375975799087104


表示

.. tweet:: https://twitter.com/NorsteinBekkler/status/347375975799087104



すごい便利！やったね！

ただまだアップの仕組みを入れてない...

流れはgit push -> jenkinsおじさん発動 -> 公開ディレクトリへコピーみたいな

それはまたいつか

.. author:: default
.. categories:: Tinkerer
.. tags:: Tinkerer
.. comments::
