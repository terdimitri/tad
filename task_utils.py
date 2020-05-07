"""utility class for working with the tad folder. All functions are dependent
on the current working directory.
"""
import os
import subprocess
import datetime

class Colors:
    RED = '\u001b[31m'
    GREEN = '\u001b[32m'
    YELLOW = '\u001b[33m'
    BLUE = '\u001b[34m'
    MAGNETA = '\u001b[35m'
    CYAN = '\u001b[36m'
    WHITE = '\u001b[37m'
    BOLD = '\u001b[1m'
    RESET = '\u001b[0m'

def add_task(name, parent_task='./', **kwargs):
    """Create a task as a subtask of parent_task"""
    location = os.path.join(parent_task, name)
    os.mkdir(location)
    for key in kwargs:
        with open(os.path.join(location, key.upper()), 'w') as file:
            file.write(kwargs[key])
    os.mknod(os.path.join(location, 'DONE'))
    return location

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

def edit_attribute(attribute, task='./', create=False, fuzzy=False):
    """Open a given attribute of a task in an editor"""
    if fuzzy:
        attribute_options = [attr for attr in os.listdir(task)
                             if os.path.isfile(os.path.join(task, attr))]
        attribute = fuzzy_find(attribute.upper(), attribute_options)

    attribute = os.path.join(task, attribute.upper())
    try:
        editor = os.environ['EDITOR']
    except KeyError:
        editor = 'vi'
    if not(create or os.path.exists(attribute)):
        raise FileNotFoundError(f'the attribute {attribute} does not exist')
    subprocess.call([editor, attribute])

def write_attribte(text, attribute, task='./'):
    """Write the given text to the attribute"""
    attribute = os.path.join(task, attribute)
    with open(attribute, 'w') as file:
        file.write(text+'\n')

def longest_common_substring(str1, str2):
    """return the length of the longest longest common substring of the given
    strings
    """
    lcs = [[0] * (len(str2) + 1) for _ in range(len(str1) + 1)]
    for i, c1 in enumerate(str1):
        for j, c2 in enumerate(str2):
            if c1 == c2:
                lcs[i+1][j+1] = lcs[i][j] + 1
            else:
                lcs[i+1][j+1] = max(lcs[i][j+1], lcs[i+1][j])
    return lcs[-1][-1]

def fuzzy_find(search_string, options):
    """Find the option closest to the search string"""
    return max(options,
               key=lambda s: longest_common_substring(search_string, s))

def format_task_line(task, padding=0):
    """Return a formatted string representing the task and its state"""
    name = task_name(task)
    if is_done(task):
        return f'[X] {Colors.GREEN}{name.ljust(padding)}{Colors.RESET}  {task_description(task)}'
    return f'[ ] {Colors.BLUE}{Colors.BOLD}{name.ljust(padding)}{Colors.RESET}  {task_description(task)}'

def ls_lines(task):
    """Return a list of nicely formatted lines listing all subtasks of the
    given task with indicators for the completion status
    """
    try:
        maxlen = max(len(task_name(subtask)) for subtask in subtasks(task))
    except ValueError:
        # no subtasks
        return
    for subtask in subtasks(task):
        yield format_task_line(subtask, padding=maxlen)

def tree_lines(task):
    """Return formatted lines that whatever idk"""
