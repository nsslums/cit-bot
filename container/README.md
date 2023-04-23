# build container image

## python版

以下のコマンドでpython版コンテナイメージをbuildします。

docker build -t gitlab-registry.maruru.me/nsslums/cit-bot:0.1.0 --build-arg NOCACHE=$(date +%s) .

## build時の注意事項

Dockerfileと同じ階層で実行してください。
gitlab-registry.maruru.me/nsslums/cit-botはpushするリポジトリに応じて変更してください。
0.1.0はバージョンです。

## バージョニングに関して(仮)

A:  なんか物が変わるレベル
    互換性がなくなるかも
B:  マイナーアップデート
    機能追加など
C:  バグの修正など

バージョンは A.B.C とする。
例: 0.1.0
