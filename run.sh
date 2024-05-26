#!/bin/bash

# Dockerイメージの名前を設定
IMAGE_NAME="sqlalchemy_learning_env"

# コンテナ名を設定
CONTAINER_NAME="sqlalchemy_learning_container"

# ホストのワークスペースディレクトリを設定
####!!!! 使用先のディレクトリを指定すること !!!!####

# My Mac
HOST_WORKSPACE="/Users/mn/workspace/db_study/sql_alchemy_study/workspace"

# My Windows
#HOST_WORKSPACE="/home/mn/workspace/sql_alchemy_study/workspace"


# コンテナ内のワークスペースディレクトリを設定
CONTAINER_WORKSPACE="/workspace"

# 既存のコンテナがあるか確認し、削除
if [ $(docker ps -a -q -f name=${CONTAINER_NAME}) ]; then
  echo "既存のコンテナを削除しています: ${CONTAINER_NAME}"
  docker rm -f ${CONTAINER_NAME}
fi

# 新しいコンテナを作成して起動
echo "新しいコンテナを作成して起動しています: ${CONTAINER_NAME}"
docker run -d \
  --name ${CONTAINER_NAME} \
  -p 5432:5432 \
  -v ${HOST_WORKSPACE}:${CONTAINER_WORKSPACE} \
  ${IMAGE_NAME}

# コンテナが正しく起動したことを確認するメッセージ
if [ $? -eq 0 ]; then
  echo "Dockerコンテナが正常に起動しました: ${CONTAINER_NAME}"
else
  echo "Dockerコンテナの起動に失敗しました" >&2
  exit 1
fi

# 数秒待機してカウントダウンを表示
echo "コンテナの起動を待っています..."
for i in {20..1}; do
  printf "\rWaiting... %2d seconds" $i
  sleep 1
done
echo -e "\n接続を試みます..."

# コンテナにログインし、psqlを実行してデータベースに接続
echo "コンテナにログインし、psqlを実行してデータベースに接続しています: ${CONTAINER_NAME}"
docker exec -it ${CONTAINER_NAME} su - postgres -c "psql -U docker -d docker"