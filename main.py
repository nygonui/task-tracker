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
            task_cli.update_status(id_task, 'in-progress')
        elif command == 'mark-done':
            id_task = int(values[0])
            task_cli.update_status(id_task, 'done')
        elif command == 'list':
            if values == []:
                task_cli.list_visualization()
            else:
                task_cli.list_visualization(values[0])
        else:
            print(f"Command '{command}' not exists")
        
        

    else:
        print('Please write some command (add, update, delete)')