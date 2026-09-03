from classes.task import Task
from pydantic import BaseModel, Field
from typing import Any, Literal


class TodoList(BaseModel):
    tasks: list[Task] = Field(default_factory=list)

    def get_task(self, task_id) -> Task | None:
        for task in self.tasks:
            if task.id == task_id:
                return task
        return None

    def add(self, task: Task):
        if task.id in [t.id for t in self.tasks]:
            raise ValueError("The task already exists")
        else:
            self.tasks.append(task)

    def remove(self, task_id: int):
        task = self.get_task(task_id)
        if task in self.tasks:
            self.tasks.remove(task)
        else:
            raise ValueError("Task not found")

    def update(self, task_id: int, updates: dict[str, Any]) -> None:
        task = self.get_task(task_id)

        if task is None:
            raise ValueError("Task not found")

        new_inputs = task.model_dump() | updates
        validated_task = Task.model_validate(new_inputs)

        self.remove(task_id)
        self.add(validated_task)

    def info(self, task_id: int):
        task = self.get_task(task_id=task_id)
        if task:
            print(f"ID : {task.id}")
            print(f"TITLE :  {task.title}")
            print(f"DESC : {task.desc}")
            print(f"PRIORITY : {task.priority}")
            print(f"STATUS : {task.status}")
            print(f"TIME : {task.time}")
        else:
            raise ValueError("Task not found")
