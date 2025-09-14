# 📝 CLI Task Manager (task-tracker)

A simple Python-based **to-do list manager** that runs in the command line interface (CLI).  
It allows you to add, update, delete, and track the status of your tasks directly from the terminal.
This project is inspired by the [Task Tracker](https://roadmap.sh/projects/task-tracker) challenge from the Backend roadmap at roadmap.sh.

---

## 🚀 Features

- Add tasks with descriptions  
- Update existing tasks  
- Delete tasks  
- Mark tasks as **in progress** or **done**  
- List tasks by status (`todo`, `in-progress`, `done`)  

---

## ⚙️ Requirements  

- **Python 3.13.1** (or any version that supports `sys`, `datetime`, `json`, `pathlib`)  
- No external dependencies are required (only built-in libraries).  

---

## 📦 Installation  

1. Clone the repository:  

    ```cmd
      git clone https://github.com/your-username/cli-task-manager.git  
      cd cli-task-manager  
    ```

2. Run the program:
  
    ```cmd
      python main.py <command> <value>  
    ```

---

## 🔧 Usage  

### Available commands

- **add** `<task description>`  
  Add a new task.  
  
  ```cmd
    python main.py add "Buy groceries and cook dinner"  
  ```

- **update** `<task_id>`  
  Update an existing task (e.g., change its description interactively).  
  
  ```cmd
    python main.py update 1  
  ```

- **delete** `<task_id>`  
  Remove a task by its ID.  
  
  ```cmd
    python main.py delete 2  
  ```

- **mark-in-progress** `<task_id>`  
  Mark a task as in progress.  
  
  ```cmd
    python main.py mark-in-progress 3  
  ```

- **mark-done** `<task_id>`  
  Mark a task as completed.

  ```cmd
    python main.py mark-done 3
  ```

- **list** `[status]`  
  List tasks. If no status is provided, all tasks are shown.  
  
  ```cmd
    python main.py list
    python main.py list todo
    python main.py list in-progress
    python main.py list done 
  ```
