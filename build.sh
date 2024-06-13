#!/bin/bash

# build.sh

# Dockerイメージの名前を設定
IMAGE_NAME="sqlalchemy_learning_env"

# Dockerイメージをビルド
docker build -t $IMAGE_NAME . --no-cache

# ビルドが成功したことを確認するメッセージ
if [ $? -eq 0 ]; then
  echo "Dockerイメージのビルドが成功しました: $IMAGE_NAME"
else
  echo "Dockerイメージのビルドに失敗しました" >&2
  exit 1
fi