
import sys
import os

from .todo import TaskManager
from pyhome import TODO_LIST_FILE

def main():
    taskmng = TaskManager(open(TODO_LIST_FILE))
    if len(sys.argv) > 1:
        term = ' '.join(sys.argv[1:])
        task = taskmng.find_wip(term)
        taskmng.move_to_done(task)
        taskmng.write_tasks(open(TODO_LIST_FILE, 'w'))
        print('task finished:', task)

if __name__ == '__main__':
    main()


