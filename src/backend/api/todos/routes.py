from fastapi import APIRouter
from .. import db  # import the db module from the current package


router = APIRouter()

todos = []
def load_todos():
    cursor = db.db.cursor()
    cursor.execute("SELECT * FROM TODOS")
    for todo in cursor.fetchall():
        todos.append({'id': todo[0], 'title': todo[1], 'description': todo[2], 'done': todo[3]})
    cursor.close()
    return todos




print(load_todos())

@router.get("/")
async def index():
    return {"message": "PING working"}

@router.get("/todos", tags=["todos"])
async def get_todos() -> list:
    return todos

@router.post("/todos")
async def create_todos(todo: dict) -> dict:
    todo['id'] = len(todos) + 1
    todos.append(todo)
    return todo

@router.put("/todos/{id}")
async def update_todos(id: int, todo: dict) -> dict:
    for index, item in enumerate(todos):
        if item['id'] == id:
            todos[index] = todo
    return todo

@router.delete("/todos/{id}")
async def delete_todos(id: int) -> dict:
    for index, item in enumerate(todos):
        if item['id'] == id:
            todos.pop(index)
    return {"message": "Todo deleted successfully"}

@router.get("/todos/{id}")
async def get_todo_by_id(id: int) -> dict:
    for todo in todos:
        if todo['id'] == id:
            return todo
    return {"message": "Todo not found"}