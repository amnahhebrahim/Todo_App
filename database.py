from sqlalchemy import Column, String, Integer,create_engine
from sqlalchemy.orm import sessionmaker, declarative_base  #to create different models
from sqlalchemy.ext.asyncio import create_async_engine

postgres_db_url="postgresql+psycopg2://postgres:12345@localhost:5432/todo_db"

engine = create_engine(
    url=postgres_db_url
)

# SessionLocal = sessionmaker(autocommit=True, autoflush=False, bind=engine)
Base= declarative_base()

#Naming convention is that the class is singular and the table is plural
class Todo(Base): #inheret the Base
    __tablename__="todos"
    #columns:
    id=Column(Integer, primary_key=True)
    Item=Column(String)

Base.metadata.create_all(engine)