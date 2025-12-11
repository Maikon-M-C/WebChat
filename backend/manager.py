from typing import List
from fastapi import WebSocket

class ConectionManager:
    def __init__(self):
            self.active_conections: List[WebSocket] = []
            
    async def connect(self, websocket: WebSocket):
         await websocket.accept()
         self.active_conections.append(websocket)

    async def disconnect(self, websocket: WebSocket):
         self.active_conections.remove(websocket)
        
    async def send_personal_message(self, websocket: WebSocket, message: str):
         await websocket.send_text(message)

    async def broadcast(self, message: str):
         for conection in self.active_conections:
               await conection.send_text(message)