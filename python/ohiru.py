import discord
import calendar
from datetime import datetime, timedelta, timezone

def init(tree_bot):
    tree = tree_bot

   # 何週目かを計算
    def week_count(day:datetime) -> int:
        first_day_of_month = day.replace(day=1)
        return (day - first_day_of_month).days // 7 + 1

    def get_week(day):
        now_week = week_count(day)
        first_day_of_month = day.replace(day=1)
        if first_day_of_month.weekday() > 0 :
            now_week += 1
        return now_week

    def today():
        tz = timezone(timedelta(hours=9))
        return datetime.now(tz)

    def yearMonth(day):
        now_week = week_count(day)
        first_day_of_month = day.replace(day=1)
        if now_week == 1 and first_day_of_month.weekday() > 0:
            old_day = day.replace(day=1) - timedelta(days=1)
            return str(old_day.strftime("%Y%m"))
        return str(day.strftime("%Y%m"))

    @tree.command(name="ohiru",description="weekly launch menu.")
    async def ohiru(interaction: discord.Interaction, private: bool = True):
        date = today()
        image_url = f'https://www.cit-s.com/wp/wp-content/themes/cit/menu/td_{str(yearMonth(date))}_{str(get_week(date))}.png'
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