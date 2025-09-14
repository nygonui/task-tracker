"""
Código criado por: Nicolas G. de Souza (https://github.com/nygonui/)
Data última atualização: 13/09/2025
"""
import sys
from task_cli import TaskCLI


if __name__ == '__main__':
    if len(sys.argv) > 1:
        command, *values = sys.argv[1:]

        task_cli = TaskCLI()
        
        if command == 'add':
            msg_result = task_cli.add(values[0])
            print(msg_result)

    else:
        print('Please write some command (add, update, delete)')