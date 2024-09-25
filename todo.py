from fastapi import APIRouter, HTTPException, Path
from typing import List
from model import Todo  # Убедитесь, что этот импорт корректен

todo_router = APIRouter()

# Инициализация списка задач
todo_list: List[Todo] = []

@todo_router.post("/todo/", response_model=Todo, status_code=201)
async def add_todo(todo: Todo) -> Todo:
    # Проверка уникальности ID
    for existing_todo in todo_list:
        if existing_todo.id == todo.id:
            raise HTTPException(status_code=400, detail="Задача с таким ID уже существует")
    todo_list.append(todo)
    return todo  # Возвращаем объект Todo напрямую

@todo_router.get("/todo/", response_model=List[Todo])
async def retrieve_todos() -> List[Todo]:
    return todo_list  # Возвращаем список задач напрямую

@todo_router.get("/todo/{todo_id}", response_model=Todo)
async def get_single_todo(
    todo_id: int = Path(..., title='ID задачи для получения', ge=1)
) -> Todo:
    for todo in todo_list:
        if todo.id == todo_id:
            return todo  # Возвращаем объект Todo напрямую
    raise HTTPException(status_code=404, detail="Задача с таким ID не существует.")
