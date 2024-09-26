from fastapi import APIRouter, Path, HTTPException, status
from model import TodoItem, TodoItems

todo_router = APIRouter()

todo_list = []

@todo_router.post("/todo", status_code=201, response_model=TodoItem)
async def add_todo(todo: TodoItem):
    # Проверка на уникальность ID
    for existing_todo in todo_list:
        if existing_todo.id == todo.id:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Todo with supplied ID already exists",
            )
    todo_list.append(todo)
    return todo

@todo_router.get("/todo", response_model=TodoItems)
async def retrieve_todo():
    return TodoItems(todos=todo_list)

@todo_router.get("/todo/{todo_id}", response_model=TodoItem)
async def get_single_todo(todo_id: int = Path(..., title="The ID of the todo to retrieve.")):
    for todo in todo_list:
        if todo.id == todo_id:
            return todo
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Todo with supplied ID doesn't exist",
    )

@todo_router.put("/todo/{todo_id}", response_model=TodoItem)
async def update_todo(todo_data: TodoItem, todo_id: int = Path(..., title="The ID of the todo to be updated.")):
    for index, todo in enumerate(todo_list):
        if todo.id == todo_id:
            todo_list[index] = todo_data
            return todo_data
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Todo with supplied ID doesn't exist",
    )

@todo_router.delete("/todo/{todo_id}", status_code=204)
async def delete_single_todo(todo_id: int):
    for index, todo in enumerate(todo_list):
        if todo.id == todo_id:
            todo_list.pop(index)
            return
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Todo with supplied ID doesn't exist",
    )

@todo_router.delete("/todo", status_code=204)
async def delete_all_todo():
    todo_list.clear()
    return
