# ① ベースとなる OS + Python
FROM python:3.10-slim

# ② コンテナ内の作業ディレクトリ
WORKDIR /app

# ③ ライブラリ一覧をコピー
COPY requirements.txt .

# ④ pip install
RUN pip install --no-cache-dir -r requirements.txt

# ⑤ プロジェクトのファイルをコピー
COPY . .

# ⑥ コンテナ起動時に実行するコマンド
CMD ["python", "server.py"]
