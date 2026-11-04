from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel

app = FastAPI(title="Task Manager API")


class TaskInput(BaseModel):
    title: str
    completed: bool = False


class Task(TaskInput):
    id: int


tasks: list[Task] = []
next_task_id = 1


@app.get("/tasks")
def list_tasks():
    # TODO: Return all tasks.
    pass


@app.get("/tasks/{task_id}")
def get_task(task_id: int):
    # TODO: Find and return the task, or raise HTTPException with status 404.
    pass


@app.post("/tasks", status_code=status.HTTP_201_CREATED)
def create_task(task_input: TaskInput):
    global next_task_id
    # TODO: Create a task, assign its ID, store it, and return it.
    pass


@app.put("/tasks/{task_id}")
def update_task(task_id: int, task_input: TaskInput):
    # TODO: Update the matching task, or raise HTTPException with status 404.
    pass


@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    # TODO: Remove the matching task, or raise HTTPException with status 404.
    pass