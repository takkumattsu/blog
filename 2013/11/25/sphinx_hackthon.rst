Sphinxハンズオンに参加してきた
===============================

.. author:: default
.. categories:: sphinx
.. tags:: sphinx
.. comments::


11/23(土)にあった `Sphinx+翻訳 Hack-a-thon 2013.11/Sphinxハンズオン <http://connpass.com/event/3926/>`__ に参加してきました。

前から興味があったのですが、この度ハンズオンを開催するとのことでこれ幸いと参加しました。

ハンズオン参加者は3人、Sphinx+翻訳 Hack-a-thon参加者は6人。

基本的には `Sphinxをはじめよう <http://www.oreilly.co.jp/books/9784873116488/>`_ にそってSphinxドキュメントを作ってみることをやりました。
主催の `tk0miya <https://twitter.com/tk0miya>`_  さんに講師として色々フォローしてもらいました。

( tk0miya_ さんは Sphinxをはじめよう_ の作者の一人)


=======================
今回の目的
=======================

今回自分が参加した目的はドキュメント管理をSphinxで行うためのノウハウ取得。

実際に運用されている tk0miya_ さんに色々教えてもらいました。


* 実際のドキュメントのフロー

  1. Sphinxでドキュメントを書く
  2. コミット(push) 
  3. jenkinsでビルド(htmlとPDF)
  4. jenkinsの概要部分にリンクを貼る
  5. 幸せになれる

* テスト項目書はSphinxではやっていない
  (やっぱりエクセルでやっているとのこと)

今回のハッカソンではjenkinsでビルドさせるところまで持っていきたかったのですが、jenkinsとgitlabの連携がうまいこといかずpush出来ず時間切れでした(´・ω・`)

Sphinxのドキュメント自体はこんな感じ

.. image:: ../../../_image/sphinx_example.png
   :scale: 40

PDFをはくにはtexを経由しないといけなく、ダウンロードに時間がかかるため断念

==============
おやつタイム
==============

途中に `usaturn <https://twitter.com/usaturn>`_ さんがおやつを差し入れてくれました！激ウマでしたー
  
.. tweet:: https://twitter.com/NorsteinBekkler/status/404133110440144896


====================
感想
====================

和気あいあいとした雰囲気でとても楽しかったです。また参加できたら参加してみたいと思います。

あと tk0miya_ さんは `新宿 Book-a-thon <http://connpass.com/series/75/>`_ なる積んでる本の読書会をやるとのこと。積んでる本があったら参加してみようかなー

