FROM python:3.11

WORKDIR /api

# 必要なシステムパッケージをインストール
RUN apt-get update && apt-get install -y curl \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Poetryをダウンロードしてインストール
RUN curl -sSL https://install.python-poetry.org | python -

# Pathを通す
ENV PATH /root/.local/bin:$PATH
# 仮想環境をたてない
RUN poetry config virtualenvs.create false

# アプリケーションの依存関係をインストール
COPY pyproject.toml poetry.lock /api/
RUN poetry install

EXPOSE 8080

COPY . /api

WORKDIR /api/app

# ここでワークディレクトリを変えれば良い
CMD ["uvicorn", "main:app", "--reload", "--host", "0.0.0.0", "--port", "8080"]
