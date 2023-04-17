# cit-bot

cit-botはdiscord上からcitサービスへのアスセスを行います．

pythonとjava での実装があります．
新しいバージョンを作成する場合は**必ずブランチを作成**してください．

### 環境変数 .env
.envファイルは以下のように新しく作成し，必ず.gitignoreに追加されていることを確認してください．　<span style="color: red; ">**commitをしないように！**</span>
```zsh
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

## Command
```zsh
/ohiru
```
###  引数
1. private 個人メッセージを有効にするかを指定する事ができます．


更新：2023/04/17