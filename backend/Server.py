from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from Schemas import *
from manager import ConectionManager
from fastapi.middleware.cors import CORSMiddleware
from database.controler import Controler

app = FastAPI(name='Web Chat')

allow_origins = [
    "*",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=allow_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

manager  = ConectionManager()
controler = Controler()


@app.post('/register/', response_model=UserPublic | None)
def register(user: UserSchema):
     result = controler.create_user(user.model_dump())

     return result

@app.post('/login/', response_model=UserPublic | None)
def login(user: UserLogin):
     query1 = controler.get_user(('email', '==', user.email))
     query2 = controler.get_user(('password', '==', user.password))

     intersection = set(query1).intersection(set(query2))

     user = [user_.to_dict() for user_ in intersection]
     if not user:
          return None
     
     return user[0]

@app.get('/users/', response_model=ListUsersSchema)
def get_users():
     usuarios = controler.read_all_users()
     users = [UserPublic(**usuario.to_dict()) for usuario in usuarios]
     return ListUsersSchema(users=users)


##WebSocket Endpoint
@app.websocket('/ws/{username}')
async def websocket_endpoint(websocket: WebSocket, username: str):
    await manager.connect(websocket)
    await manager.broadcast(username)

    try:
         while True:
              recv = await websocket.receive_text()
              await manager.broadcast(recv)

    except WebSocketDisconnect:
         await manager.broadcast(username)

