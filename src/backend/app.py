from fastapi import FastAPI, APIRouter
from api.todos.routes import router as todo_router

app = FastAPI()

router = APIRouter()

app.include_router(todo_router, prefix='/api/v1/todos')

