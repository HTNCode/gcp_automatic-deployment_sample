# ベースイメージの指定
FROM python:3.12-slim-bookworm

# 作業ディレクトリの指定
WORKDIR /

# flaskを使うための環境変数を設定。
# FLASK_APP: Flaskアプリケーションのエントリーポイントとなるファイル名
# FLASK_RUN_HOST: Flaskアプリケーションを実行するホスト名。0.0.0.0はコンテナ内の全てのネットワークインタ―フェースで接続を受け付けることを意味する
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

# 必要なパッケージのインストール
RUN apt-get update

# requirements.txtをコピー
COPY ./server-side/requirements.txt .
# 全てのファイルをコピー
COPY ./server-side .

# pipとsetuptoolsを更新
RUN pip install --upgrade pip setuptools

# Pythonの依存関係をrequirements.txtからインストール
RUN pip install -r requirements.txt

# CloudRun上のコンテナが起動した際に以下コマンドが実行されるようにすることでAPIが動作する
CMD ["flask", "run", "--host=0.0.0.0", "--port=8080"]

# 参考
# https://cloud.google.com/run/docs/troubleshooting?hl=ja
# https://qiita.com/Pitts7/items/542196eaec6bc.b77c8#indexhtml
