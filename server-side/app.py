# エンドポイントにgetリクエストがあるとhello worldを返すだけのapi
from flask import Flask
import os

# cloudBuild.yamlの環境変数を取得する
USER_NAME = os.environ.get('USER_NAME')

app = Flask(__name__)

@app.route('/')
def hello_world():
    return f'Hello, {USER_NAME}!'

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080)) # 環境変数からポート番号を取得し、なければ8080を使う
    app.run(host='0.0.0.0', port=port) # 上記のport含め、左記もDockerを使用しない環境で（例えばローカルで）アプリケーションを実行する際に必要な記述（Dockerのみを使用する場合は不要）