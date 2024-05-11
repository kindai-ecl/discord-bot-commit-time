import discord
from discord import app_commands
import os
from dotenv import load_dotenv
from datetime import datetime, timedelta, timezone

import sys
sys.path.append("../")
import timelogger 

## botの使い方
lines = []
with open(r'../doc/manual.md', encoding='utf-8') as f:
    lines = f.readlines()
helpMessage = ''.join(lines)

load_dotenv()
JST = timezone(timedelta(hours=+9), 'JST')

client = discord.Client(
    intents=discord.Intents.all(),
    activity=discord.Game("研究🤖")
)
tree = app_commands.CommandTree(client)

# 起動時に動作する処理
@client.event
async def on_ready():
    await tree.sync()
    print('ログインしました')

@client.event
async def on_voice_state_update(member, before, after): 
    now = datetime.now(JST)

    if after.channel != None and '室' in after.channel.name:
        timelogger.stamp_time_log(member.id, now, 'start')

    elif before.channel != None and '室' in before.channel.name:
        timelogger.stamp_time_log(member.id, now, 'end')

### コマンド実装部分 ###

@tree.command(name="total_time",description="合計時間を表示します")
async def total_time(interaction: discord.Interaction, user:discord.Member):
    await interaction.response.send_message(user.name + "の合計時間はです",ephemeral=True)

@tree.command(name="help",description="ヘルプを表示します")
async def help(interaction: discord.Interaction):
    await interaction.response.send_message(helpMessage,ephemeral=True)

# Botの起動とDiscordサーバーへの接続
client.run(os.getenv('TOKEN'))





