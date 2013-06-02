# Tinkererを利用したブログ

Tinkererとは？

Sphinxを利用したブログツール。reStructuredTextで書ける！
詳しくは[公式ページ](http://tinkerer.me/ "Tinkerer")


## blog作成

```bash
tinker -s
```

## 記事作成

```bash
tinker -p "記事名"
```

記事名は半角英数にすること

## 公開の流れ

1. 記事を書く

2. git pushする

3. jenkinsが裏でごにょごにょして、ビルド結果を公開ディレクトリへ
