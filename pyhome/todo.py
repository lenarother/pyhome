#!/usr/bin/env python3

import sys
import os

TODO_LIST_FILE = os.environ.get('TODO_FILE', 'todo.list')

class TaskManager:

    def __init__(self, lines, wip_limit=3):
        self.todos = []
        self.wip = []
        self.done = []
        self.wip_limit = wip_limit
        for line in lines:
            if line.startswith('TODO'):
                self.todos.append(self.parse(line))
            if line.startswith('WIP'):
                self.wip.append(self.parse(line))
            if line.startswith('DONE'):
                self.done.append(self.parse(line))
    
    def parse(self, line):
        line = line.replace('    ', '\t')
        col = line.strip().split('\t')
        return col[1]

    def write_tasks(self, writer):
        lines = []
        for t in self.todos:
            lines.append('TODO\t' + t + '\n')
        for w in self.wip:
            lines.append('WIP\t' + w + '\n')
        for d in self.done:
            lines.append('DONE\t' + d + '\n')
        writer.writelines(lines)

    def find_todo(self, term):
        for task in self.todos:
            if term in task:
                return task
       
    def find_wip(self, term):
        for task in self.wip:
            if term in task:
                return task
       
    def move_to_wip(self, task):
        if len(self.wip) < self.wip_limit:
            self.todos.remove(task)
            self.wip.append(task)
            return True
        else:
            print('WIP limit reached!')

    def move_to_done(self, task):
        self.wip.remove(task)
        self.done.append(task)
    
def main():
    if not os.getenv('TODO_FILE'):
        print('Set environmental variable TODO_FILE.')
    if not os.path.isfile(os.getenv('TODO_FILE')):
        print('Create todo file {}'.format(os.getenv('TODO_FILE')))
    taskmng = TaskManager(open(TODO_LIST_FILE))
    if len(sys.argv) > 1:
        task = ' '.join(sys.argv[1:])
        taskmng.todos.append(task)
        taskmng.write_tasks(open(TODO_LIST_FILE, 'w'))
        print('task added')
    else:
        for task in taskmng.todos:
            print('    ',task)


if __name__ == '__main__':
    main()
