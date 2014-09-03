
import sys
import os

from todo import TaskManager

TODO_LIST_FILE = os.environ.get('ACADEMIS_TODO_FILE', 'todo.list')

if __name__ == '__main__':
    taskmng = TaskManager(open(TODO_LIST_FILE))
    if len(sys.argv) > 1:
        term = ' '.join(sys.argv[1:])
        task = taskmng.find_wip(term)
        taskmng.move_to_done(task)
        taskmng.write_tasks(open(TODO_LIST_FILE, 'w'))
        print 'task finished:', task

