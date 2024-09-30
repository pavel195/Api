from typing import List, Optional  # Импорт типов для аннотаций
from fastapi import Form  # Импорт для обработки данных формы в FastAPI
from pydantic import BaseModel  # Импорт базовой модели от Pydantic для валидации данных


class Todo(BaseModel):
    """
    Модель данных для отдельной задачи (Todo).
    """
    id: int | None = None  # Идентификатор задачи. Опциональный, так как может быть автоматически назначен.
    item: str  # Описание задачи.

    @classmethod
    def as_form(
            cls,
            item: str = Form(...)
    ):
        """
        Класс-метод для преобразования данных формы в объект модели Todo.

        Args:
            item (str): Описание задачи, полученное из формы.

        Returns:
            Todo: Созданный объект модели Todo.
        """
        return cls(item=item)

    class Config:
        """
        Конфигурация модели для Pydantic.
        """
        schema_extra = {
            "example": {
                "id": 1,
                "item": "Example schema!"
            }
        }


class TodoItem(BaseModel):
    """
    Модель данных для обновления задачи (частичная информация).
    """
    item: str  # Обновлённое описание задачи.
    @classmethod
    def as_form(
            cls,
            item: str = Form(...)
        ):
        return cls(item=item)

    class Config:
        """
        Конфигурация модели для Pydantic.
        """
        schema_extra = {
            "example": {
                "item": "Read the next chapter of the book"
            }
        }


class TodoItems(BaseModel):
    """
    Модель данных для списка задач.
    """
    todos: List[TodoItem]  # Список объектов TodoItem.

    class Config:
        """
        Конфигурация модели для Pydantic.
        """
        schema_extra = {
            "example": {
                "todos": [
                    {
                        "item": "Example schema 1!"
                    },
                    {
                        "item": "Example schema 2!"
                    }
                ]
            }
        }
