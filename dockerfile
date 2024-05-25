# ベースイメージとしてUbuntu 22.04を使用
FROM ubuntu:22.04

# 環境変数の設定
ENV DEBIAN_FRONTEND=noninteractive

# 必要なパッケージのインストールとPython 3.11のセットアップ
RUN apt-get update && \
    apt-get install -y software-properties-common wget curl gnupg && \
    add-apt-repository ppa:deadsnakes/ppa && \
    wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | apt-key add - && \
    sh -c 'echo "deb http://apt.postgresql.org/pub/repos/apt jammy-pgdg main" > /etc/apt/sources.list.d/pgdg.list' && \
    apt-get update && \
    apt-get install -y \
    python3.11 \
    python3.11-venv \
    python3.11-dev \
    build-essential \
    libpq-dev \
    git \
    vim \
    postgresql-16 \
    postgresql-client-16

# デフォルトのPythonをPython 3.11に設定
RUN update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.11 1 && \
    update-alternatives --set python3 /usr/bin/python3.11 && \
    curl -sS https://bootstrap.pypa.io/get-pip.py | python3.11

# PostgreSQLの初期設定をするディレクトリの作成とスクリプトの作成
RUN mkdir -p /docker-entrypoint-initdb.d
RUN echo "#!/bin/bash\n\
set -e\n\
echo 'Updating pg_hba.conf to use trust authentication...'\n\
sed -i \"s/peer/trust/g\" /etc/postgresql/16/main/pg_hba.conf\n\
echo 'Restarting PostgreSQL...'\n\
service postgresql restart\n\
sleep 5\n\
echo 'Setting password for postgres user...'\n\
psql -U postgres -c \"ALTER USER postgres PASSWORD 'postgres';\" && echo 'Postgres password set'\n\
echo 'Creating docker user...'\n\
psql -U postgres -c \"CREATE USER docker WITH SUPERUSER PASSWORD 'docker';\" && echo 'Docker user created'\n\
echo 'Creating docker database...'\n\
createdb -U postgres -O docker docker && echo 'Docker database created'\n\
echo 'Updating pg_hba.conf to use md5 authentication...'\n\
sed -i \"s/trust/md5/g\" /etc/postgresql/16/main/pg_hba.conf\n\
echo 'Restarting PostgreSQL...'\n\
service postgresql restart\n\
echo 'PostgreSQL initialization completed.'" > /docker-entrypoint-initdb.d/init-user-db.sh

# スクリプトに実行権限を付与
RUN chmod +x /docker-entrypoint-initdb.d/init-user-db.sh

# 仮想環境の作成
RUN python3 -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

# 必要なPythonパッケージのインストール
RUN /opt/venv/bin/pip install --upgrade pip && \
    /opt/venv/bin/pip install sqlalchemy psycopg2-binary

# 作業ディレクトリの作成
WORKDIR /workspace

# 開発用ポートの公開
EXPOSE 5432

# PostgreSQLサービスの起動スクリプト
CMD service postgresql start && sleep 5 && \
    /docker-entrypoint-initdb.d/init-user-db.sh && \
    tail -f /dev/null