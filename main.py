from fastapi import FastAPI
from agents.main_agent import MainAgent

app = FastAPI()
agent = MainAgent()

@app.post("/task")
def create_task(task: str):
    return agent.handle_task(task)

@app.get("/tasks")
def get_tasks():
    return agent.get_tasks()
