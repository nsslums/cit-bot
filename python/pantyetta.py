import discord
import calendar
import datetime
import json

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


todoList = []

def openJson():
    global todoList
    with open('./todo.json', encoding="utf-8") as f:
        todoList = json.load(f)

def writeJson(value):
    with open("./todo.json", "w", encoding="utf-8") as outputFile:
        json.dump(value, outputFile, indent=2, ensure_ascii=False )

def addJson(value):
    global todoList
    todoList.append(value)
    writeJson(todoList)

def checkToDo():
    global todoList
    for todo in todoList:
        if todo["notification"]:
            continue
        print(todo["data"])

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
    async def todo(interaction: discord.Interaction, date:int, time:int, value:str, notification:bool=True, mode:str="add"):
        openJson()
        if mode=="add":
            global todoList
            
            schedule = {}
            schedule["id"] = todoList[len(todoList) -1]["id"] + 1
            schedule["created"] = now()
            schedule["date"] = format_datetime(date, time)
            schedule["value"] = value
            schedule["notification"] = not notification

            addJson(schedule)
            
        await interaction.response.send_message("ok", ephemeral=True)