from fastapi import FastAPI
from database import Base
from sqlalchemy.orm import Mapped,
from pydantic import BaseModel

""""
cLass note
id str
title str
content str
date_created str 
"""
class Todo(Base):
    __tablename__="notes"
    id: int
    item: str
    date_created: datetime