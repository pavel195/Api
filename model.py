from pydantic import BaseModel
from typing import List
class TodoItem(BaseModel):
    id : int
    item:str

    class Config:
        schema_extra = {
            'example': {
                'id': 1,
                'item' : "Read more books to become smarter!"
            }
        }

class TodoItems(BaseModel):
    todos: List[TodoItem]
