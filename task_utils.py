"""utility class for working with the tad folder. All functions are dependent
on the current working directory.
"""
import os
import subprocess
import datetime

def add_task(name, parent_task='./', **kwargs):
    """Create a task as a subtask of parent_task"""
    location = os.path.join(parent_task, name)
    os.mkdir(location)
    for key in kwargs:
        with open(os.path.join(location, key.upper()), 'w') as file:
            file.write(kwargs[key])
    os.mknod(os.path.join(location, 'DONE'))

def complete_task(task):
    """Mark task as done. Lables the finished task with the completion
    time and date.
    """
    with open(os.path.join(task, 'DONE'), 'w') as file:
        file.write(f'Completed on {datetime.datetime.now().isoformat()}')

def task_name(task):
    """Return only the name of the given task"""
    return os.path.basename(task)

def task_description(task):
    """Return the first line of the description of the task"""
    try:
        with open(os.path.join(task, 'DESCRIPTION')) as file:
            return file.readline().rstrip()
    except FileNotFoundError:
        return ''

def subtasks(task):
    """List all subtasks of the given task."""
    for subtask in os.listdir(task):
        if os.path.isdir(os.path.join(task, subtask)):
            yield os.path.join(task, subtask)

def is_done(task):
    """Check if task is done"""
    try:
        if os.path.getsize(os.path.join(task, 'DONE')) > 0:
            return True
    except OSError:
        pass
    return False

def edit_attribute(attribute, task='./'):
    """Open a given attribute of a task in an editor"""
    attribute = os.path.join(task, attribute.upper())
    try:
        editor = os.environ['EDITOR']
    except KeyError:
        editor = 'vi'
    if os.path.exists(attribute):
        subprocess.call([editor, attribute])
