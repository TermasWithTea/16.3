from fastapi import FastAPI
from fastapi import HTTPException

app = FastAPI()

users = {'1': 'Имя: Example, возраст: 18'}

@app.get('/users')
async def get_reurn() -> dict:
    return users

@app.post('/user/{username}/{age}')
async def post_user(username: str, age: int) -> str:
    if age < 0:
        raise HTTPException(status_code=400, detail="Возраст не может быть отрицательным")
    if users:
        user_id = str(max(map(int, users.keys())) + 1)
    else:
        user_id = '1'
    users[user_id] = f"Имя: {username}, возраст: {age}"
    return f'User {user_id} is registered!'

@app.put('/user/{user_id}/{username}/{age}')
async def put_ret(user_id: str, username: str, age: str) -> str:
    users[user_id] = f'Имя:{username}, возраст:{age}'
    return f'The user {user_id} is update!'

@app.delete('/user/{user_id}')
async def del_del(user_id: str) -> dict:
    del users[user_id]
    return {'message':f'User {user_id} has been deleted'}
