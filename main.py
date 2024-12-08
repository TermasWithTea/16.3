from fastapi import FastAPI

app = FastAPI()

users = {'1': 'Имя: Example, возраст: 18'}

@app.get('/users')
async def get_reurn() -> dict:
    return users

@app.post('/user/{username}/{age}')
async def post_ret(username: str, age: int) -> str:
    user_id = max(users.keys(), default= 0) +1
    users[user_id] = f"Имя: {username}, возраст: {age}"
    return f'User {user_id} is registred!'

@app.put('/user/{user_id}/{username}/{age}')
async def put_ret(user_id: str, username: str, age: str) -> str:
    users[user_id] = f'Имя:{username}, возраст:{age}'
    return f'The user {user_id} is update!'

@app.delete('/user/{user_id}')
async def del_del(user_id: str) -> dict:
    del users[user_id]
    return {'message':f'User {user_id} has been deleted'}

