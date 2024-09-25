from fastapi import FastAPI
from todo import todo_router

app = FastAPI()

@app.get("/") # когда пользователь совершает get запрос к главной странице / - будет вызвана функция welcome
async def welcome() -> dict: # -> dict указывает на то , что функция будет возрвращать словарь(помогает улучшить читаемость кода)
    return {"message":"Hello world!"}

app.include_router(todo_router)
