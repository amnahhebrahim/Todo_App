from  fastapi import FastAPI
from fastapi import Path #IMPORT AS OBJECT TO INSTITANTIATE APP
from database import Todo, engine
from sqlalchemy.orm import sessionmaker

#CREATE INSTANCE:
app=FastAPI()
#create api use @app. and specify endpoint (put, get, delete and post)

Session= sessionmaker(bind=engine)
session=Session()

all_todos=[]
# get all todos:
@app.get("/todos")  # create url, to return name
def get_todos():
    # return{"todos": todos}
    todos=session.query(Todo).all()
    for todo in todos:
        # return {"todo_id":todo.id, "todo_item": todo.Item}
        all_todos.append(todo.Item)
    return {"todos": all_todos}
    session.commit()

#get single todo:
@app.get("/todos/{todo_id}") #create url, to return name
def get_todo(todo_id: int):
        todos= session.query(Todo).filter_by(id=todo_id).one_or_none()
        return{"todo": todos.Item}
        session.commit()
#     for todo in todos:
#         if todo.id == todo_id:
#            return{"todos": todo.item}

#
#
#create todo
@app.post("/todos") #create url, to return name
def create_todos(todos: str):
    todo_item = Todo(Item=todos)

    # Todo.id=num_id
    # Todo.Item=todos
    session.add(todo_item)
    return {"todo_last": todo_item}
    session.commit()





#update todo
@app.put("/todos/{todo_id}") #create url, to return name
def update_todos(todo_id: int, todo_object: str):
      todos= session.query(Todo).filter_by(id=todo_id).one_or_none()
      todos.id=todo_id
      todos.Item=todo_object
      session.commit()
#     for todo in todos:
#         if todo.id == todo_id:
#             todo.id=todo.id
#             todo.item= todo_object.item

      return{"message": "todo has been updated"}
#
#delete todo
@app.delete("/todos/{todo_id}") #create url, to return name
def delete_todos(todo_id: int):
      todo= session.query(Todo).filter_by(id=todo_id).one_or_none()
      session.delete(todo)
      session.commit()
      return{"message": "Todo deleted"}



"""""
# ###To add into the db:
# #todos = Todo(Item="Visa")
# # ###To get all db entries:
# # todos=session.query(Todo).all()
# # for todo in todos:
# #      print(f'Todo', todo.id, ': ',todo.Item)
# #GET ONE SPECIFIC TODO:
# # todos= session.query(Todo).filter_by(id=1).one_or_none()
# # print(f'Todo', todos.id, ':',todos.Item)
# 
# #UPDATE ONE TODO:
# todo= session.query(Todo).filter_by(id=1).one_or_none()
# session.delete(todo)
# 
# 
# session.commit()

"""