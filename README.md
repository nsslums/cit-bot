# cit-bot

cit-botはdiscord上からcitサービスへのアスセスを行います．

pythonとjava での実装があります．
新しいバージョンを作成する場合は**必ずブランチを作成**してください．

### 環境変数 .env
.envファイルは以下のように新しく作成し，必ず.gitignoreに追加されていることを確認してください．　<span style="color: red; ">**commitをしないように！**</span>
```
/cit-bot
 |-- java/
 |-- python/
 |-- .gitignore
 |-- .env
```
.envの内容はこちらを置き換えてお使いください．
```
TOKEN="xxxxxxxxxxxxxxxxxxxxxxxxxxx"
```

## オリジナルファイル
各ファイルのテンプレートです．(pantyetta.py)
```python:pantyeyta.py
import discord

def init(tree_bot):
    tree = tree_bot

     @tree.command(name="pantyetta",description="descriptioin")
    async def pantyetta(interaction: discord.Interaction):
        await interaction.response.send_message("pancho",ephemeral=True)#ephemeral=True→「これらはあなただけに表示されていす」
```
Bot.pyに
```
pantyetta.init(tree)
```
などの表記が必要です．


## Command
```
/ohiru
```
###  引数
1. private 個人メッセージを有効にするかを指定する事ができます．


更新：2023/04/17
