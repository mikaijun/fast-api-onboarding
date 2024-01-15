## できたこと
- FastAPIの環境構築
- firebaseを使ったユーザー新規作成
- firebaseログイン(token生成)
- firebase認証(tokenがないと認証エラー出す)

## ライブラリのインストール

```bash
pip install -r requirements.txt
```

## サーバー立ち上げ

```bash
uvicorn main:app --reload
```

## エンドポイント

http://localhost:8000/

## スキーマ確認

http://127.0.0.1:8000/docs
