from datetime import datetime
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, DATE

from ..database import Base


class Todo(Base):
    __tablename__ = "todos"

    id = Column(Integer, primary_key=True)
    title = Column(String(length=50))
    description = Column(String(length=250))
    create_date = Column(DATE, default=datetime.now)
    due_date = Column(DATE, nullable=True)
    is_completed = Column(Boolean, default=False)
    owner_id = Column(Integer, ForeignKey("users.id"))
