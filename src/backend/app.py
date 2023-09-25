from fastapi import FastAPI

app = FastAPI()

todos = [{'id': 1, 'title': 'First Todo', 'description': 'This is the first todo', 'done': False}]

@app.get("/")
async def index():
    return {"message": "Hello World"}

@app.get("/api/todos")
async def get_todos() -> list:
    return todos

@app.post("/api/todos")
async def create_todos(todo: dict) -> dict:
    todo['id'] = len(todos) + 1
    todos.append(todo)
    return todo

@app.put("/api/todos/{id}")
async def update_todos(id: int, todo: dict) -> dict:
    for index, item in enumerate(todos):
        if item['id'] == id:
            todos[index] = todo
    return todo

@app.delete("/api/todos/{id}")
async def delete_todos(id: int) -> dict:
    for index, item in enumerate(todos):
        if item['id'] == id:
            todos.pop(index)
    return {"message": "Todo deleted successfully"}

@app.get("/api/todos/{id}")
async def get_todo_by_id(id: int) -> dict:
    for todo in todos:
        if todo['id'] == id:
            return todo
    return {"message": "Todo not found"}