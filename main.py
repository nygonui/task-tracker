import sys
from task_cli import TaskCLI


if __name__ == '__main__':
    if len(sys.argv) > 1:
        command, *values = sys.argv[1:]

        task_cli = TaskCLI()
        
        if command == 'add':
            description = values[0]
            task_cli.add(description)
        elif command == 'update':
            id_task = int(values[0])
            new_description = values[1]
            task_cli.update(id_task, new_description)
        elif command == 'delete':
            id_task = int(values[0])
            task_cli.delete(id_task)
        elif command == 'mark-in-progress':
            id_task = int(values[0])
            task_cli.mark_in_progress(id_task)
        elif command == 'mark-done':
            id_task = int(values[0])
            task_cli.mark_done(id_task)
        elif command == 'list':
            if values == []:
                task_cli.list_visualization()
            elif values[0] == 'done':
                task_cli.done_tasks_visualization()
            elif values[0] == 'in-progress':
                task_cli.in_progress_tasks_visualization()
            elif values[0] == 'todo':
                task_cli.todo_tasks_visualization()
        else:
            print(f"Command '{command}' not exists")
        
        

    else:
        print('Please write some command (add, update, delete)')