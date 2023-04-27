import discord
import calendar
import datetime
import json
import db

def get_nth_week(year, month, day, firstweekday=0):
    first_dow = calendar.monthrange(year, month)[0]
    offset = (first_dow - firstweekday) % 7
    return (day + offset - 1) // 7 + 1

def now():
    tz = datetime.timezone(datetime.timedelta(hours=9))
    return datetime.datetime.now(tz)

def format_datetime(date, time):
    fdt = None
    hour = 0
    minute = 0
    if date == 0:
        fdt = now() + datetime.timedelta(days=1)
    else:
        fdt = datetime.datetime.strptime(date, "%Y/%m/%d")
    if time != 0:
        hour = int(time / 100)
        minute = time % 100

    return fdt.replace(hour=hour, minute=minute)


def checkToDo():
    global todoList
    for todo in todoList:
        if todo["notification"]:
            continue
        print(todo["data"])

todoList = db.db()

def init(tree_bot):
    tree = tree_bot

    @tree.command(name="pantyetta",description="descriptioin")
    async def pantyetta(interaction: discord.Interaction, private:bool=True):
        await interaction.response.send_message("pancho",ephemeral=private)#ephemeral=True→「これらはあなただけに表示されています」

    @tree.command(name="ohiru",description="weekry launch menu.")
    async def ohiru(interaction: discord.Interaction, private:bool=True):
        date = now()
        image_url='https://www.cit-s.com/wp/wp-content/themes/cit/menu/td_' + str(date.strftime("%Y%m")) + '_' + str(get_nth_week(date.year, date.month, date.day)) + '.png'
        embed=discord.Embed(title= "今週のメニュー",color=0x3c0fbc)
        embed.set_image(url=image_url)#URLでEmbedに画像を貼る
        await interaction.response.send_message(embed=embed, ephemeral=private)

    @tree.command(name="todo",description="todo")
    async def todo(interaction: discord.Interaction, text:str, year:int=now().year, month:int=now().month, day:int=now().day, hour:int=now().hour, minute:int=now().minute, notification:bool=True, mode:str="add"):
        global todoList
        if mode=="add":
            newEvent = db.event(text=text, notis_date=datetime.datetime(year=year, month=month, day=day, hour=hour, minute=minute), notification=notification)
            todoList.add(newEvent)
            
        await interaction.response.send_message("ok", ephemeral=True)