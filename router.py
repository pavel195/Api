from fastapi import APIRouter

router = APIRouter()

todo_list = []
@router.post("/hello")
async def add_todo(todo: dict):
    todo_list.append(todo)
    return({"message": "Todo added successfully "})
