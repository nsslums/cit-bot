import discord
import calendar
import datetime

def init(tree_bot):
    tree = tree_bot

    @tree.command(name="pantyetta",description="descriptioin")
    async def pantyetta(interaction: discord.Interaction, private:bool=True):
        await interaction.response.send_message("pancho",ephemeral=private)#ephemeral=True→「これらはあなただけに表示されています」

    def get_nth_week(year, month, day, firstweekday=0):
        first_dow = calendar.monthrange(year, month)[0]
        offset = (first_dow - firstweekday) % 7
        return (day + offset - 1) // 7

    def today():
        tz = datetime.timezone(datetime.timedelta(hours=9))
        return datetime.datetime.now(tz)

    @tree.command(name="ohiru",description="weekry launch menu.")
    async def ohiru(interaction: discord.Interaction, private:bool=True):
        date = today()
        image_url='https://www.cit-s.com/wp/wp-content/themes/cit/menu/td_' + str(date.strftime("%Y%m")) + '_' + str(get_nth_week(date.year, date.month, date.day)) + '.png'
        embed=discord.Embed(title= "今週のメニュー",color=0x3c0fbc)
        embed.set_image(url=image_url)#URLでEmbedに画像を貼る
        await interaction.response.send_message(embed=embed, ephemeral=private)
    
    @tree.command(name="masa",description="descriptioin")
    async def pantyetta(interaction: discord.Interaction, private:bool=False):
        await interaction.response.send_message("バーニングレッド",ephemeral=private)#ephemeral=True→「これらはあなただけに表示されています」