import discord
from discord import app_commands
import os
from dotenv import load_dotenv
from datetime import datetime, timedelta, timezone
from io import StringIO

from timelogger import total_time

## botの使い方
helpMessage = "VCに入ることで研究時間を記録します\n" + "コマンド一覧\n"

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
async def on_message(message):
    print('message event')

@client.event
async def on_voice_state_update(member, before, after): 
    now = datetime.now(JST)
    if before.channel is None and after.channel.category.name == "-----作成する-----":
        print("%s : %sに参加しました",now.strftime('%Y-%m-%d %H:%M:%S'), after.channel.name)
        channel = client.get_channel(os.getenv('CHANNEL_ID'))
        await channel.send(f"{member.name}が{after.channel.name}に参加しました")
    elif after.channel is None:
        print("%s : %sを退出しました",now.strftime('%Y-%m-%d %H:%M:%S'), before.channel.name)
        channel = client.get_channel(os.getenv('CHANNEL_ID'))
        await channel.send(f"{member.name}が{before.channel.name}を退出しました")


@tree.command(name="total_time",description="合計時間を表示します")
async def total_time(interaction: discord.Interaction, user:discord.Member):
    total_time = total_time(user.id)
    await interaction.response.send_message("合計時間はです",ephemeral=True)


@tree.command(name="help",description="ヘルプを表示します")
async def help(interaction: discord.Interaction):
    await interaction.response.send_message(helpMessage,ephemeral=True)

# Botの起動とDiscordサーバーへの接続
client.run(os.getenv('TOKEN'))





