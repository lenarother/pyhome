
import sys
import os

from .todo import TaskManager
from pyhome import TODO_LIST_FILE

WIP_LIMIT = int(os.environ.get('WIP_LIMIT', '3'))

def main():
    taskmng = TaskManager(open(TODO_LIST_FILE), WIP_LIMIT)
    if len(sys.argv) > 1:
        term = ' '.join(sys.argv[1:])
        task = taskmng.find_todo(term)
        if taskmng.move_to_wip(task):
            taskmng.write_tasks(open(TODO_LIST_FILE, 'w'))
            print('Task in progress:', task)
    else:
        for task in taskmng.wip:
            print('    ',task)


if __name__ == '__main__':
    main()

