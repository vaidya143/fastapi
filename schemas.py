
from pydantic import BaseModel
from typing import Generic, List, Optional, TypeVar

T = TypeVar("T")

class TaskBase(BaseModel):
    title: str
    description: Optional[str] = None
    completed: bool = False

class TaskCreate(TaskBase):
    pass

class TaskUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    completed: Optional[bool] = None

class Task(TaskBase):
    id: int

    class Config:
        from_attributes = True


class Page(BaseModel, Generic[T]):
    items: List[T]
    page: int
    size: int
    total: int
    pages: int

# Concrete alias for response_model
TaskPage = Page[Task]

