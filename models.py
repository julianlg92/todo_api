from datetime import datetime
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DATE, text
from sqlalchemy.orm import relationship

from .database import Base


class User(Base):
    """
    User table class model
    """

    __tablename__ = "user"

    id = Column(Integer, primary_key=True, nullable=False)
    fist_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    hash_password = Column(String, nullable=False)
    is_active = Column(Boolean, default=False)

    todos = relationship("Todo", back_populates="owner")


class Todo(Base):
    """
    ToDo table class model
    """

    __tablename__ = "todo"

    id = Column(Integer, primary_key=True)
    created = Column(DATE, default=datetime.today)
    is_complete = Column(Boolean, default=False)
    due_date = Column(DATE, nullable=True)

    owner = relationship("User", back_populates="todos")
