from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from Schemas import *
from manager import ConectionManager
from fastapi.middleware.cors import CORSMiddleware


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
users = []  #temporario


@app.post('/login/', response_model=UserPublic)
def login(user: UserSchema):
     user = UserPublic(**user.model_dump() ,id=len(users) +1)
     users.append(user)
     return user

@app.get('/users/', response_model=ListUsersSchema)
def get_users():
     return ListUsersSchema(users=users)



##WebSocket Endpoint
@app.websocket('/ws/{user_id}')
async def websocket_endpoint(websocket: WebSocket, user_id: int):
    await manager.connect(websocket)
    await manager.broadcast(f'{user_id} se conectou.')

    try:
         while True:
              recv = await websocket.receive_text()
              data: str = f'{user_id}: {recv}'
              await manager.broadcast(data)

    except WebSocketDisconnect:
         manager.disconnect(websocket)
         await manager.broadcast(f'{user_id} deixou o chat.')

