from fastapi import FastAPI
from enum import Enum
from routers.users import router as users_router
from typing import Optional


app = FastAPI()
app.include_router(users_router)

@app.get("/tasks", description="Retrieve a list of tasks")
async def getAllTasks():
    return {"message": "List of all tasks"}

@app.get("/tasks/{task_id}", description="Retrieve a specific task by its ID")
async def getTaskById(task_id: int):
    return {"message": f"Details of task with ID {task_id}"}

@app.post("/tasks", description="Create a new task")
async def createTask():
    return {"message": "New task created"}

@app.put("/tasks/{task_id}", description="Update an existing task by its ID")
async def updateTask(task_id: int):
    return {"message": f"Task with ID {task_id} updated"}

@app.delete("/tasks/{task_id}", description="Delete a task by its ID")
async def deleteTask(task_id: int):
    return {"message": f"Task with ID {task_id} deleted"}

@app.patch("/tasks/{task_id}", description="Partially update a task by its ID")
async def partiallyUpdateTask(task_id: int):
    return {"message": f"Task with ID {task_id} partially updated"}


@app.get("/users/{user_id}/items/{item_id}", description="Retrieve a specific item for a user")
async def getUserItem(user_id: int, item_id: str):
    response = {
        "user_id": user_id,
        "item_id": item_id,
        "message": f"Details of item {item_id} for user {user_id}"
    }

    return response

@app.get("/items")
async def getItems(skip: int = 0, limit: int = 10):
    return {"skip": skip, "limit": limit, "items": ["item1", "item2"]}

class TaskStats(str, Enum):
    completed = "completed"
    pending = "pending"
    overdue = "overdue"