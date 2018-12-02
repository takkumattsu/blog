ターミナルからXcodeを起動する
===============================

Xcodeをターミナルから開きたい時ってありますよね。gitとか使っていると特に

`MacOSXでターミナルからGUIアプリケーションを起動したい <http://d.hatena.ne.jp/tsua/20100310/1268231225>`__ のエントリーを参考にしてターミナルからXcodeを起動できるようにしました。

.. gist:: https://gist.github.com/TakkuMattsu/7667631

.. more::


今までは

1. ターミナルから open . してフォルダー開いて
2. Xcodeのプロジェクトをダブルクリック

としていたのですが下記のように起動できます。

.. code-block:: bash

 # xcodeのあるディレクトリで
 xopen .


やったね！

.. author:: default
.. categories:: その他
.. tags:: その他
.. comments::
