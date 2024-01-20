## pip の導入方法

おそらく[ドキュメント](https://pip.pypa.io/en/stable/installation/)通りのコマンドでできると思います

## 環境構築

仮想環境を採用した理由は[こちら](https://zenn.dev/nekoallergy/articles/py-env-pipenv01#%E7%92%B0%E5%A2%83%E3%82%92%E5%88%86%E3%81%91%E3%82%8B%E3%81%A8%E4%BD%95%E3%81%8C%E5%AC%89%E3%81%97%E3%81%84%E3%81%AE%EF%BC%9F)参照

pip env をインストール

```bash
pip install pipenv
```

app にディレクトリ移動

```bash
cd app
```

仮想環境にパッケージをインストール

```bash
pipenv install -r requirements.txt
```

仮想環境の中に入る

```bash
pipenv shell
```

仮想環境の中でサーバー立ち上げる

```bash
uvicorn main:app --reload
```

仮想環境の中でコード整形を行う

```bash
black .
```

### VScode の import エラー直し方

VSCode のコマンドパレット `(Ctrl+Shift+P)`から、Python: Select Interpreterw を選択。
VSCode が使用可能な Python 環境一覧が表示されるため、そこから使用したい環境を選択。
<img width="988" alt="vscode" src="https://github.com/mikaijun/fast-api-onboarding/assets/74134232/4f13a283-8ea5-4758-b3e9-70061201a4cc">

## ローカル URL

エンドポイント
http://localhost:8000/

スキーマ(Open API)
http://127.0.0.1:8000/docs

## 拡張機能

### python

説明不要の拡張機能

https://marketplace.visualstudio.com/items?itemName=ms-python.python

### Pylance

Python の入力補完周りが有効になる

https://marketplace.visualstudio.com/items?itemName=ms-python.vscode-pylance

### Python Indent

引数改行時にインデント調整してくれる

https://marketplace.visualstudio.com/items?itemName=KevinRose.vsc-python-indent

### mypy

インデントや型のチェックを行ってくれる

https://marketplace.visualstudio.com/items?itemName=matangover.mypy

### Black Formatter

コードの整形を自動で行ってくれる

https://marketplace.visualstudio.com/items?itemName=ms-python.black-formatter
