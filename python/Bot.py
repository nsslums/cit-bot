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


@tree.command(name="info",description="serverInfo")
async def info(interaction: discord.Integration):
    embed = discord.Embed(title=interaction.guild.name + " Info")
    embed.add_field(name="Server ID",value=interaction.guild.id)
    embed.add_field(name="Server peoples",value=interaction.guild.member_count)
        
    await interaction.response.send_message(embed=embed, ephemeral=True)


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