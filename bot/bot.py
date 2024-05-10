import discord
from discord import app_commands
import os
from dotenv import load_dotenv
from datetime import datetime, timedelta, timezone

import sys
sys.path.append("../")
from timelogger import total_time

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
    # await client.change_presence(activity=discord.Game(new_activity)) 
    print('ログインしました')

@client.event
async def on_voice_state_update(member, before, after): 
    now = datetime.now(JST)
    if after.channel != None and '室' in after.channel.name:
        print("%s : %sに参加しました",now, after.channel.name)
        channel = client.get_channel(874633285047840768)
        await channel.send(f"{member.name}が{after.channel.name}に参加しました")
    elif before.channel != None and '室' in before.channel.name:
        print("%s : %sを退出しました",now, before.channel.name)
        channel = client.get_channel(874633285047840768)
        await channel.send(f"{member.name}が{before.channel.name}を退出しました")
    


@tree.command(name="total_time",description="合計時間を表示します")
async def total_time(interaction: discord.Interaction, user:discord.Member):
    await interaction.response.send_message(user.name + "の合計時間はです",ephemeral=True)


@tree.command(name="help",description="ヘルプを表示します")
async def help(interaction: discord.Interaction):
    await interaction.response.send_message(helpMessage,ephemeral=True)

# Botの起動とDiscordサーバーへの接続
client.run(os.getenv('TOKEN'))





