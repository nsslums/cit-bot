import discord

def init(tree_bot):
    tree = tree_bot

    @tree.command(name="pantyetta", description="description")
    async def pantyetta(interaction: discord.Interaction, private: bool = True):
        await interaction.response.send_message("pancho", ephemeral=private)     # ephemeral=True→「これらはあなただけに表示されています」
    
    @tree.command(name="masa",description="descriptioin")
    async def masa(interaction: discord.Interaction, private: bool = False):
        await interaction.response.send_message("バーニングレッド",ephemeral=private)   # ephemeral=True→「これらはあなただけに表示されています」
    
    @tree.command(name="nemui",description="descriptioin")
    async def nemui(interaction: discord.Interaction, private: bool = False):
        await interaction.response.send_message("おやすみー", ephemeral=private)  # ephemeral=True→「これらはあなただけに表示されています」