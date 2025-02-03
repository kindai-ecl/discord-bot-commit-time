# 研究室で時間測る用のDiscordBot
インテントは現在デフォルトで使用できます。
## About
電子商取引研究室で学生がリモートで研究を行う場合に使用します。
卒業研究に必要な作業時間を担保するために明示的にDiscordのVCに入って作業をし研究時間を計測します。

## 環境構築
> [!NOTE]
> stagingに関しては自前の[Discord Developer Portal(新規作成)](https://discord.com/developers/applications?new_application=true)から新しくアプリケーションを作成して検証作業を行なってください。
> <details>
>  <summary>Developer portalで必要な手順</summary>
>   1. Discord Developer PortalにDiscordアカウントでログイン/サインアップする
>   <img width="444" alt="スクリーンショット 2025-02-03 16 05 11" src="https://github.com/user-attachments/assets/c87cc6f5-4df6-4066-8297-d9d56e33db92" /><br>
>   2. [Discord Developer Portal(新規作成)](https://discord.com/developers/applications?new_application=true) からアプリケーションを新規作成する<br>
>   <img width="430" alt="スクリーンショット 2025-02-03 16 07 21" src="https://github.com/user-attachments/assets/84a66fac-dbd4-4ed5-ac02-3797514917bb" /><br>
>   3. Botに移動してBot情報を入力する。**BotのAPIを叩く際にTOKENが必要になるので必ず覚えておく**
>   <img width="1142" alt="スクリーンショット 2025-02-03 16 22 22" src="https://github.com/user-attachments/assets/3d06e11b-74cd-4c55-ba2f-77e4db5b1b6d" />
>
> </details>
#### docker環境（推奨）
docker-composeを使用して環境構築を行います。(versionアプデ未対応)
```shell
# .envファイルを作成してください
touch .env
echo -n "TOKEN=MTMzNTg2OTI5MzE5NTMwMDk2Nw.GKFEBg.pBnF_qW9EuZggsi4r7POndGggWBnGTfyaa0uzc" > .env
# example
# echo -n "TOKEN=" > .env

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
Docker Desktopから管理できます。（python3というimage名をつけています。）<br>
CDの実装はssh deploymentになるので難しいかも

## コントリビューション
[issue](https://github.com/kindai-ecl/discord-bot-commit-time/issues)から各自で作成してPR投げてくださいmm

