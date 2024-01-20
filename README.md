## pip の導入方法

おそらく[https://pip.pypa.io/en/stable/installation/](ドキュメント)通りのコマンドでできると思います

## 環境構築

仮想環境を採用した理由は[https://zenn.dev/nekoallergy/articles/py-env-pipenv01#%E7%92%B0%E5%A2%83%E3%82%92%E5%88%86%E3%81%91%E3%82%8B%E3%81%A8%E4%BD%95%E3%81%8C%E5%AC%89%E3%81%97%E3%81%84%E3%81%AE%EF%BC%9F](こちら)参照

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

サーバー立ち上げる

```bash
uvicorn main:app --reload
```

## エンドポイント

http://localhost:8000/

## スキーマ確認

http://127.0.0.1:8000/docs
