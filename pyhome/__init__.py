import os
from ._version import get_versions

__version__ = get_versions()['version']
del get_versions

TODO_LIST_FILE = os.environ.get('TODO_FILE', 'todo.list')

