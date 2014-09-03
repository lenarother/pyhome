
import sys
import os

from todo import TaskManager

TODO_LIST_FILE = os.environ.get('ACADEMIS_TODO_FILE', 'todo.list')
WIP_LIMIT = int(os.environ.get('ACADEMIS_WIP_LIMIT', '3'))


if __name__ == '__main__':
    taskmng = TaskManager(open(TODO_LIST_FILE), WIP_LIMIT)
    if len(sys.argv) > 1:
        term = ' '.join(sys.argv[1:])
        task = taskmng.find_todo(term)
        if taskmng.move_to_wip(task):
            taskmng.write_tasks(open(TODO_LIST_FILE, 'w'))
            print 'Task in progress:', task
    else:
        for task in taskmng.wip:
            print '    ',task

