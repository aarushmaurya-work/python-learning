import json
from pathlib import Path
from pydantic import BaseModel, Field, FilePath
from classes.todolist import TodoList


class Storage(BaseModel):
    path: FilePath = Field(default=Path("todolist.json"))
    todolist: TodoList = Field(default=TodoList())

    def read(self):
        try:
            with open(self.path, "r") as f:
                data = json.load(f)
                return TodoList.model_validate(data)
        except FileNotFoundError:
            return TodoList()

    def write(self, todolist: TodoList):
        with open(self.path, "w") as f:
            json.dump(todolist.model_dump(mode="json"), f, indent=4)
