Homebrewに自分用のformulaを作る
================================

みんな大好きHomebrewを使ってオレオレ便利スクリプトとかを使うときのメモ

.. more::

普段、自分用の便利シェルスクリプトとかを~/binとかに置いて使っているのですが、他のMacPCとかで使いたい時にわざわざGistとかから落としてきてゴニョゴニョするのがめんどくさい。

あと仕事で使うときにhomebrew経由だとセーフという謎の抜け道用というのもある

基本的にhomebrewの本家にマージしてもらうのではなく、オレオレツールとして使うことを目的にしている

いわゆるhomebrewの自作

===============
formulaの作り方
===============

以下のリンクを参考にしました。

* `HomeBrewで自作ツールを配布する <http://deeeet.com/writing/2014/05/20/brew-tap/>`_

* `homebrew - 手軽に自作アプリケーションをbrew installできるようにする by @masawada on @Qiita <http://qiita.com/masawada/items/484bbf83ef39cad7af74>`_


流れ的には以下

1. まず上記のリンクにあるようにgithubに **homebrew-xxx** というリポジトリを作る

2. homebrew-xxxのxxxの部分のformulaを作る

3. brew tapして使う

1. リポジトリ作成
-------------------

今回はxopenというXcodeを開くための簡単なスクリプトのコマンドにしたものを作ってみるので **homebrew-xopen** をリポジトリに作成

2. formula作成
---------------

homebrew-xxxをcloneしてきてxxx.rbを作成

xopen.rb

.. code-block:: ruby

 require "formula"
 
 # This is a non-functional example formula to showcase all features and
 # therefore, it's overly complex and dupes stuff just to comment on it.
 # You may want to use `brew create` to start your own new formula!
 # Documentation: https://github.com/Homebrew/homebrew/blob/master/share/doc/homebrew/Formula-Cookbook.md
 
 ## Naming -- Every Homebrew formula is a class of the type `Formula`.
 # Ruby classes have to start Upper case and dashes are not allowed.
 # So we transform: `example-formula.rb` into `ExampleFormula`. Further,
 # Homebrew does enforce that the name of the file and the class correspond.
 # Check with `brew search` that the name is free.
 
 class Xopen < Formula
   homepage "http://github.com/takkumattsu/homebrew-xopen.git" # used by `brew home example-formula`.
 
   # The url of the archive. Prefer https (security and proxy issues):
   url "https://gist.githubusercontent.com/TakkuMattsu/00229f904f0ca11f21ca/raw/aa3fd7a77c8b9205ea47cba7164f27ebfd27421f/xopen"
 
   # For integrity and security, we verify the hash (`openssl dgst -sha1 <FILE>`)
   # You may also use sha256 if the software uses sha256 on their homepage.
   # Leave it empty at first and `brew install` will tell you the expected.
   sha256 "40964d52c8865c9969d9d513d05e6f49343936e997ad081b5de610495be8a96f"
   version "1.0"
 
   def install
     bin.install "xopen"
   end
 
 end
 
 __END__
 # Room for a patch after the `__END__`
 # Read about how to get a patch in here:
 #    https://github.com/Homebrew/homebrew/blob/master/share/doc/homebrew/Formula-Cookbook.md
 # In short, `brew install --interactive --git <formula>` and make your edits.
 # Then `git diff >> path/to/your/formula.rb`
 # Note, that HOMEBREW_PREFIX will be replaced in the path before it is
 # applied. A patch can consit of several hunks.


* Formulaクラスを継承したクラスを作る、ここではXopenとしている。適宜変えてください。
* **homepage** は適当なものを指定(大抵homebrew-xxxに説明を書くからそこを指定しておけば問題ないと思う)
* **url** は落としてくるソースを指定。今回はgistから落としてくるだけなのでgistをそのまま指定
* **sha256** は落としてきたソースのsha256を記載。sha256は以下のコマンドでわかる

.. code-block:: sh
  
   openssl dgst -sha256 "落としてきたファイル"

* スクリプトをインストールするだけなのでbin.install に"落としてきたファイル"を指定

上記をgithubのリポジトリプッシュして用意完了

3. brew tapして使う
---------------------

インストール

.. code-block:: sh

 # brew tap "githubのユーザ名/リポジトリ名"
 brew tap takkumattsu/homebrew-xopen
 brew install xopen

アンインストール

.. code-block:: sh

 brew uninstall xopen
 brew untap takkumattsu/homebrew-xopen

.. takkumattsu:: happy brew life!


.. author:: default
.. categories:: Homebrew
.. tags:: Homebrew
.. comments::
