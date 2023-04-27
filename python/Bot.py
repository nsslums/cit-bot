import discord
from discord import app_commands
import sys
import env
import pantyetta


intents = discord.Intents.default()#適当に。
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)

pantyetta.init(tree)


@tree.command(name="ping",description="descriptioin")
async def ping(interaction: discord.Interaction):
    await interaction.response.send_message("pong",ephemeral=True)#ephemeral=True→「これらはあなただけに表示されています」


@client.event
async def on_ready():
    print("起動完了")
    await tree.sync()#スラッシュコマンドを同期


if "--debug" in sys.argv:
    print("--- DEBUG MODE ---")
    client.run(env.TOKEN_DEBUG)
else:
    print("--- NORMAL MODE ---")
    client.run(env.TOKEN)