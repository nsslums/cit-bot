import discord
import calendar
from datetime import datetime, timedelta, timezone

def init(tree_bot):
    tree = tree_bot

    @tree.command(name="pantyetta", description="description")
    async def pantyetta(interaction: discord.Interaction, private: bool = True):
        await interaction.response.send_message("pancho", ephemeral=private)     # ephemeral=True→「これらはあなただけに表示されています」

    def get_last_week(year, month):
        _, days_in_month = calendar.monthrange(year, month)
        # 月の週数を計算
        weeks = (days_in_month + calendar.firstweekday() - 1) // 7 + 1
        return weeks

    def get_now_week(day):
        first_day_of_month = day.replace(day=1)
        # 今日が何週目かを計算
        return (day - first_day_of_month).days // 7 + 1

    def get_week(day):
        now_week = get_now_week(day)
        if now_week == 1 and day.weekday() > 1:
            old_day = day.replace(day=1) - timedelta(days=1)
            now_week = get_last_week(old_day.year, old_day.month)
        return now_week

    def today():
        tz = timezone(timedelta(hours=9))
        return datetime.now(tz)

    def yearMonth(day):
        now_week = get_now_week(day)
        if now_week == 1 and day.weekday() > 1:
            old_day = day.replace(day=1) - timedelta(days=1)
            return str(old_day.strftime("%Y%m"))
        return str(day.strftime("%Y%m"))

    @tree.command(name="ohiru",description="weekly launch menu.")
    async def ohiru(interaction: discord.Interaction, private: bool = True):
        date = today()
        image_url = 'https://www.cit-s.com/wp/wp-content/themes/cit/menu/td_' + yearMonth(date) + '_' + str(get_week(date)) + '.png'
        embed = discord.Embed(title="今週のメニュー", color=0x3c0fbc)
        embed.set_image(url=image_url)
        await interaction.response.send_message(embed=embed, ephemeral=private)
    
    @tree.command(name="gomi",description="View garbage live.")
    async def gomi(interaction: discord.Interaction, private: bool = True):
        date = today()
        image_url='https://www.cit-s.com/i_catch/dining/tsudanuma.jpg?' + str(date.strftime("%Y%m%d%H%M%S"))
        embed=discord.Embed(title= "食堂の混雑状況", color=0x3c0fbc)
        embed.set_image(url=image_url)  # URLでEmbedに画像を貼る
        await interaction.response.send_message(embed=embed, ephemeral=private)
    
    @tree.command(name="masa",description="descriptioin")
    async def masa(interaction: discord.Interaction, private: bool = False):
        await interaction.response.send_message("バーニングレッド",ephemeral=private)   # ephemeral=True→「これらはあなただけに表示されています」
    
    @tree.command(name="nemui",description="descriptioin")
    async def nemui(interaction: discord.Interaction, private: bool = False):
        await interaction.response.send_message("おやすみー", ephemeral=private)  # ephemeral=True→「これらはあなただけに表示されています」