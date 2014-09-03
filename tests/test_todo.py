import sys
import os 
import re
from unittest import TestCase, main
sys.path.append(os.sep.join(os.getcwd().split(os.sep)[:-1]))

#from todo import Task

TEST_DATA_DIR = os.getcwd() + os.sep + 'test_data' + os.sep
TEST_TODO_FILE = TEST_DATA_DIR + 'todo.list' 

class TaskTests(TestCase):

    def setUp(self):
        pass
    
        

class TodoTests(TestCase):
    
    def setUp(self):
        pass

 
class TodoCommandLineTests(TestCase):

    def setUp(self):
        os.system('cp %s todo.tmp' % TEST_TODO_FILE)
        self.pathcmd = 'export ACADEMIS_TODO_FILE=todo.tmp;'

    def tearDown(self):
        if os.path.exists('todo.tmp'):
            os.remove('todo.tmp')
        if os.path.exists('out.tmp'):
            os.remove('out.tmp')
    
    def test_todo(self):
        os.system(self.pathcmd + 'todo > out.tmp')
        out = open('out.tmp').read()
        self.assertTrue('buy milk' in out)
        self.assertTrue('release code' in out)
        self.assertFalse('call Peter' in out)
        self.assertFalse('write test todo-data' in out)

    def test_done(self):
        os.system(self.pathcmd + 'done > out.tmp')
        out = open('out.tmp').read()
        self.assertFalse('buy milk' in out)
        self.assertFalse('release code' in out)
        self.assertFalse('call Peter' in out)
        self.assertFalse('write test todo-data' in out)

    def test_todo_add_message(self):
        os.system(self.pathcmd + 'todo call Mom > out.tmp')
        out = open('out.tmp').read()
        self.assertTrue('task added' in out)

    def test_todo_add_task(self):
        os.system(self.pathcmd + 'todo call Mom > out.tmp')
        todo = open('todo.tmp').readlines()
        self.assertEqual(len(todo), 6)
        todo = open('todo.tmp').read()
        self.assertTrue('call Mom' in todo)


class WipCommandLineTests(TestCase):

    def setUp(self):
        os.system('cp %s todo.tmp' % TEST_TODO_FILE)
        self.pathcmd = 'export ACADEMIS_TODO_FILE=todo.tmp;export ACADEMIS_WIP_LIMIT=3;'

    def tearDown(self):
        if os.path.exists('todo.tmp'):
            os.remove('todo.tmp')
        if os.path.exists('out.tmp'):
            os.remove('out.tmp')
    
    def test_wip(self):
        os.system(self.pathcmd + 'wip > out.tmp')
        out = open('out.tmp').read()
        self.assertFalse('buy milk' in out)
        self.assertFalse('release code' in out)
        self.assertTrue('call Peter' in out)
        self.assertFalse('write test todo-data' in out)

    def test_wip_pull_message(self):
        os.system(self.pathcmd + 'wip milk > out.tmp')
        out = open('out.tmp').read()
        self.assertTrue('buy milk' in out)

    def test_wip_pull(self):
        os.system(self.pathcmd + 'wip milk > out.tmp')
        todo = open('todo.tmp').readlines()
        self.assertEqual(len(todo), 5)
        todo = open('todo.tmp').read()
        self.assertEqual(todo.count('WIP'), 3)

    def test_wip_limit(self):
        os.system(self.pathcmd + 'wip milk > out.tmp')
        os.system(self.pathcmd + 'wip release > out.tmp')
        out = open('out.tmp').read()
        self.assertFalse('release' in out)
        self.assertTrue('WIP limit reached' in out)
        todo = open('todo.tmp').read()
        self.assertEqual(todo.count('WIP'), 3)


class OkCommandLineTests(TestCase):

    def setUp(self):
        os.system('cp %s todo.tmp' % TEST_TODO_FILE)
        self.pathcmd = 'export ACADEMIS_TODO_FILE=todo.tmp;'

    def tearDown(self):
        if os.path.exists('todo.tmp'):
            os.remove('todo.tmp')
        if os.path.exists('out.tmp'):
            os.remove('out.tmp')

    def test_done_message(self):
        os.system(self.pathcmd + 'ok backup > out.tmp')
        out = open('out.tmp').read()
        self.assertTrue('task finished' in out)
        self.assertTrue('do backup' in out)

    def test_done(self):
        os.system(self.pathcmd + 'ok backup > out.tmp')
        todo = open('todo.tmp').readlines()
        self.assertEqual(len(todo), 5)
        todo = open('todo.tmp').read()
        self.assertEqual(todo.count('DONE'), 2)


if __name__ == '__main__':
    main()
