from datetime import datetime
import json_tricks
import env
import json
import os

class event:
    def __init__(self, text:str, notis_date:datetime, notification:bool=True) -> None:
        self.id = 0
        self.text = text
        self.created_at = datetime.now()
        self.notis_date = notis_date
        self.notification = notification

class server:
    def __init__(self, id:int) -> None:
        self.id = id
        self.events = []
        
    def add(self, t:event):
        t.id = self.getLastID() + 1 
        self.events.append(t)

    def getSize(self) -> int:
        return len(self.events)
    
    def getLastID(self) -> int:
        if self.getSize() < 1:
            return 0
        return self.events[self.getSize() - 1].id
    
    
class db:
    def __init__(self) -> None:
        self.servers = []
        if os.path.isfile(env.TODOFILE):
            self.load()
        
    def getSize(self) -> int:
        return len(self.servers)    
    
    def isExist_server(self, serverID):
        for server in self.servers:
            if server.id == serverID:
                return True, self.servers.index(server)
        return False, -1
    
    # serverID とeventで各鯖のインスタンスに渡す
    def add(self, serverID, event:event):
        exist, index = self.isExist_server(serverID)
        if exist:
            print("exist", index)
            reciveServer:server = self.servers[index]
            reciveServer.add(event)
        else:
            print("not exist")
            newServer = server(serverID)
            newServer.add(event)
            self.servers.append(newServer)
        self.write()
    
    def list(self, serverID):
        exist, index = self.isExist_server(serverID)
        if exist:
            return self.servers[index].events
        else:
            return []
            
    
    def write(self):
        with open(env.TODOFILE, 'w', encoding="utf-8") as f:
            json_tricks.dump(self.servers, f)
            
    def load(self):
        try:
            with open(env.TODOFILE, 'r', encoding='utf-8') as f:
                self.servers = json_tricks.load(f)
        except FileNotFoundError:
            print("error: json not Found.")
        except json.decoder.JSONDecodeError:
            print("error: not json format.")