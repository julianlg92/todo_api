from datetime import date
from pydantic import BaseModel


class TodoBase(BaseModel):
    title: str
    description: str | None = None
    due_date: date
