# 研究室で時間測る用のDiscordBot
インテントは現在デフォルトで使用できます。
## About
電子商取引研究室で学生がリモートで研究を行う場合に使用します。
卒業研究に必要な作業時間を担保するために明示的にDiscordのVCに入って作業をし研究時間を計測します。

## 環境構築
> [!NOTE]
> stagingに関しては自前の[Discord Developer Portal(新規作成)](https://discord.com/developers/applications?new_application=true)から新しくアプリケーションを作成して検証作業を行なってください。
#### docker環境（推奨）
docker-composeを使用して環境構築を行います。(versionアプデ未対応)
```shell
# .envファイルを作成してください
touch .env
vi .env

docker-compose build
docker-compose up -d
```
#### ローカル環境
python環境を各自構築してください。
anacondaを入れた場合(Jupiter Notebook等をローカルに入れている場合）は注意してください。

1. python3をインストール
2. pip3をインストール
3. 以下のコマンドでscriptを走らせる
```shell
# .envファイルを作成してください
touch .env
vi .env

cd script 
init_run.sh
```
> [!WARNING]
> - 一応スクリプトを書きましたがCI等でライブラリ管理していないので各自でアップデート対応が必要です。
> - discord.pyのバージョンはv2以上を使用しています。

## デプロイ環境
2024年度現在，ECL研究室で使用しているサーバーで運用しています。
デプロイはCDを用意していないので自前で本リポジトリからpullしてdockerimageの再生成を行なって反映させています。
```sh
(本リポジトリに移動)
git pull
docker compose build --no-cache
docker compose up -d
```
CDの実装はssh deploymentになるので難しいかも

## コントリビューション
[issue](https://github.com/kindai-ecl/discord-bot-commit-time/issues)から各自で作成してPR投げてくださいmm

