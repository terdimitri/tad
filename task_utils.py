"""utility class for working with the tad folder. All functions are dependent
on the current working directory.
"""
import os
import datetime

def add_task(name, parent_task='./', **kwargs):
    """Create a task as a subtask of parent_task"""
    location = os.path.join(parent_task, name)
    os.mkdir(location)
    for key in kwargs:
        with open(os.path.join(location, key.upper()), 'w') as file:
            file.write(kwargs[key])
    os.mknod(os.path.join(location, 'COMPLETED'))

def complete_task(task):
    """Mark task as completed. Lables the completed task with the completion
    time and date
    """
    with open(os.path.join(task, 'COMPLETED'), 'w') as file:
        file.write(f'Completed on {datetime.datetime.now().isoformat()}')

def subtasks(task):
    """list all subtasks of the given task"""
    for subtask in os.listdir(task):
        if os.path.isdir(os.path.join(task, subtask)):
            yield os.path.join(task, subtask)

def subtask_names(task):
    """list the names of all subtasks of the given task"""
    for subtask in subtasks(task):
        yield subtask.basename()
