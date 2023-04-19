# cit-bot

cit-botはdiscord上からcitサービスへのアスセスを行います．

pythonとjava での実装があります．
新しいバージョンを作成する場合は**必ずブランチを作成**してください．

## 初期設定

```
pip install discord.py
pip install load_dotenv
```

## 環境変数 .env
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
/ohiru (private)
```
> 1. 個人メッセージを有効にするかを指定する事ができます．

## Documents Link

> [qiita](https://qiita.com/Luapy/items/3abff9575e132e2955ec)  
> [公式ドキュメント](https://discordpy.readthedocs.io/ja/latest/index.html)

更新：2023/04/19
