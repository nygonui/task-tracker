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
        
        print(f"Task added successfully (ID: {id_task})")


    def update(self, id_task: int, description: str) -> None:
        """
        Update the description of some task, the task is updated by ID

        Parameters:
            id_task (int): Task Id
            description (str): The new description
        """
        if not self.task_file_path.exists():
            print("Just maybe ... add a task first")
            return

        index = self.binary_search_task_list(id_task)
        if index == None:
            print("Erro to update task: ID not found")
        else:
            self.task_list[index]["description"] = description
            self.task_list[index]["updatedAt"] = str(datetime.datetime.now())
            self.write_task_file()
            print(f"Task (ID:{id_task}) updated")

        return
        
    
    def delete(self, id_task: int) -> None:
        """
        Delete task by ID

        Parameters:
            id_task (int): Task Id use to delete task from task list
        """
        if not self.task_file_path.exists():
            print("Just maybe ... add a task first")
            return

        index = self.binary_search_task_list(id_task)
        if index == None:
            print("Erro to update task: ID not found")
        else: 
            self.task_list.pop(index)
            self.write_task_file()
            print(f"Task (ID: {id_task}) successfully deleted")
        
        return
    

    def update_status(self, id_task: int, status: str) -> None:
        if not self.task_file_path.exists():
            print("Just maybe ... add a task first")
            return

        if status == 'done' or status == 'in-progress':
            index = self.binary_search_task_list(id_task)
            if index == None:
                print("Erro to change status from task: ID not found")           
            else:
                self.task_list[index]["status"] = status
                self.task_list[index]["updatedAt"] = str(datetime.datetime.now())

                self.write_task_file()
                print(f"Task (ID:{id_task}) changed status to: {status}")
            return
        else:
            print(f"Erro to change status: {status} status not exist. Try 'done' or 'in-progress.")
            return

    def list_visualization(self, status=None) -> None:
        """
        Show the tasks list
        """
        if not self.task_file_path.exists():
            print("The task list not exists. Use 'add' command to track your first task!")
            return

        count_success = False    
        for task in self.task_list:
            id_d = f"ID:          {task['id']}\n"
            desc_d = f"DESCRIPTION: {task['description']}\n"
            stat_d = f"STATUS:      {task['status']}\n"
            cre_d = f"CREATED AT:  {task['createdAt']}\n"
            upd_d = f"UPDATED AT:  {task['updatedAt']}\n"
            div_d = "-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+\n"

            task_display = id_d + desc_d + stat_d + cre_d + upd_d + div_d

            if status == None:
                print(task_display)
                count_success = True
            elif task['status'] == status:
                print(task_display)
                count_success = True
                      
        if not count_success:
            print(f"Error to display task by status: {status} not exists")     
            
        return


    def binary_search_task_list(self, id_search):
        start = 0
        end = len(self.task_list) - 1
        
        while start <= end:
            middle = int((start + end)/2)
            guess = self.task_list[middle]

            if guess['id'] == id_search:
                return middle
            if guess['id'] > id_search:
                end = middle - 1
            else:
                start = middle + 1
            
        return None


    def __str__(self):
        t = {
            "task-list": self.task_list,
            "last-id": self.last_id
        }

        return json.dumps(t, indent=4)
         



