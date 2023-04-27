from datetime import datetime
import json_tricks
import env

class event:
    def __init__(self, text:str, notis_date:datetime, notification:bool=True) -> None:
        self.id = 0
        self.text = text
        self.created_at = datetime.now()
        self.notis_date = notis_date
        self.notification = notification
        
class db:
    def __init__(self) -> None:
        self.todoList = []
        
    def add(self, t:event):
        self.todoList.append(t)
    
    def getSize(self):
        return len(self.todoList)
    
    def getLastID(self):
        if self.getSize() < 1:
            return 0
        return self.todoList[self.getSize() - 1].id
    
    def write(self):
        with open(env.TODOFILE, 'w', encoding="utf-8") as f:
            json_tricks.dump(self.todoList, f)
            
    def load(self):
        with open(env.TODOFILE, 'r', encoding='utf-8') as f:
            self.todoList = json_tricks.load(f)