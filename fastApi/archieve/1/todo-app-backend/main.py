from uuid import uuid4
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, mapped_column, Mapped, DeclarativeBase

DATABASE_URL = "postgresql+psycopg://postgres:admin@127.0.0.1:15432/postgres"
engine = create_engine(DATABASE_URL)
SessionLocal= sessionmaker[Session](bind=engine)

class Base(DeclarativeBase): 
  id: Mapped[str] = mapped_column(primary_key = True, default = lambda: str(uuid4()))

class TaskORM(Base):
  # Какое название будет в базе данных
  __tablename__ = "tasks"

  title: Mapped[str]
  completed: Mapped[bool] = mapped_column(default = False)

@asyncontextmanager
async def lifespan(_: FastAPI):
  Base.metadata.create_all()
  yield

app = FastAPI(lifespan = lifespan)

app.add_middleware(
  CORSMiddleware,
  allow_origins = ["http://localhost:3000"],
  allow_methods = ["*"]
)

class TaskSchema(BaseModel):
  id: str
  title: str
  completed: bool

class TaskCreateSchema(BaseModel):
  title: str

class TaskUpdateSchema(BaseModel):
  title: str | None = None
  completed: bool | None = None

tasks: list[TaskSchema] = []

@app.get('/')
def read_base_page():
  return {'message': 'Hello world'}

@app.get('/tasks')
def read_tasks():
  return tasks

@app.post('/tasks')
def create_test(payload: TaskCreateSchema):
  new_task = TaskSchema(
    id = str(uuid4()), 
    title = payload.title, 
    completed = False
  )

  tasks.append(new_task)
  return new_task

@app.patch("/tasks/{task_id}")
def update_task(task_id: str, payload: TaskUpdateSchema):
  for task in tasks:
    if task.id == task_id:
      if payload.title:
        task.title = payload.title
      if payload.completed is not None:
        task.completed = payload.completed

      return task

@app.delete("/tasks/{task_id}")
def delete_task(task_id):
  for task in tasks:
    if task.id == task_id:
      task.remove

      return task