from agents.task_agent import TaskAgent
from agents.calendar_agent import CalendarAgent
from db.database import Database

class MainAgent:
    def __init__(self):
        self.task_agent = TaskAgent()
        self.calendar_agent = CalendarAgent()
        self.db = Database()

    def handle_task(self, task):
        if "schedule" in task:
            result = self.calendar_agent.schedule(task)
        else:
            result = self.task_agent.add_task(task)

        self.db.save_task(task)
        return {"result": result}

    def get_tasks(self):
        return self.db.get_tasks()
