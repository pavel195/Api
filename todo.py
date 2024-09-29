from fastapi import APIRouter, Path, HTTPException, status, Request, Depends
from model import TodoItem, TodoItems
from fastapi.templating import Jinja2Templates

todo_router = APIRouter()

todo_list = []

templates = Jinja2Templates(directory =  "templates/")

@todo_router.post("/todo", status_code=201, response_model=TodoItem)
async def add_todo(request : Request, todo: TodoItem = Depends(TodoItem.as_form)):
    # Проверка на уникальность ID
    for existing_todo in todo_list:
        todo.id = len(todo_list)+ 1
        todo_list.append(todo)
        return templates.TemplateResponse("todo.html", {
            "request" : request,
            "todos"  :todo_list
        })

@todo_router.get("/todo", response_model=TodoItems)
async def retrieve_todo(request : Request):
    return templates.TemplateResponse("todo.html", {
            "request" : request,
            "todos"  :todo_list
        })


@todo_router.get("/todo/{todo_id}", response_model=TodoItem)
async def get_single_todo(request: Request, todo_id = Path(..., title="The ID of the todo to retrieve.")):
    for todo in todo_list:
        if todo.id == todo_id:
            return {
                "request" : request,
                "todo" : todo
            }
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
