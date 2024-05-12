# 研究室で時間測る用のDiscordBot
  ＊　Intents.voice_states を有効にする必要があります。

## About
電子商取引研究室で学生がリモートで研究を行う場合に使用します。
卒業研究に必要な作業時間を担保するために明示的にDiscordのVCに入って作業をし研究時間を計測します。

## 環境構築
python環境を各自構築してください。
anacondaを入れた場合(Jupiter Notebook等)をローカルに入れている場合は注意してください。

1. python3をインストール
2. pip3をインストール
3. 以下のコマンドでscriptを走らせる
```
cd script 
init_run.sh
```
> [!WARNING]
> - 一応スクリプトを書きましたがCI等でライブラリ管理していないので各自でアップデート対応が必要です。
> - discord.pyのバージョンはv2以上を使用しています。

## コントリビューション
[issue](https://github.com/kindai-ecl/discord-bot-commit-time/issues)から各自で作成してPR投げてくださいmm
