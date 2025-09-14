import json
import datetime
from pathlib import Path

class TaskCLI:
    def __init__(self):
        self.last_id = 0
        self.task_list = []

        self.task_file_path = Path("tasks.json")

        self.open_task_file()
    

    def open_task_file(self):
        if self.task_file_path.exists():
            with open(self.task_file_path, 'r') as file_reader:
                task_db = dict(json.load(file_reader))
                self.task_list = list(task_db["task-list"])
                self.last_id = int(task_db["last-id"])


    def write_task_file(self):
        with open(self.task_file_path, "w") as file_writer:
            file_writer.write(self.__str__())


    def add(self, description: str) -> str:
        """
        Add a new task
        
        Parameters:
            description (int): The task's description

        Returns:
            str: The message of succesfull add and the task's ID
        
        """

        id_task = self.last_id + 1
        new_task = {
            "id": id_task,
            "description": description,
            "status": "todo",
            "createdAt": str(datetime.datetime.now()),
            "updatedAt": None
        }

        self.last_id = id_task

        self.task_list.append(new_task)
        self.write_task_file()
        
        return f"Task added successfully (ID: {id_task})"


    def update(self, id_task: int, description: str) -> None:
        ...

    
    def delete(self, id_task: int) -> None:
        ...
    


    def __str__(self):
        t = {
            "task-list": self.task_list,
            "last-id": self.last_id
        }

        return json.dumps(t, indent=4)
         



