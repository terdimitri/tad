#!/usr/bin/env python
"""An application for storing and managing tasks in a hierarchal manner."""
import argparse
import task_utils

COLORS = {
        'red': '\u001b[31m',
        'green': '\u001b[32m',
        'yellow': '\u001b[33m',
        'blue': '\u001b[34m',
        'magneta': '\u001b[35m',
        'cyan': '\u001b[36m',
        'white': '\u001b[37m',
        'bold': '\u001b[1m',
        'reset': '\u001b[0m',
        }

def add(args):
    task_utils.add_task(args.name)

def ls(args):
    task = './' if args.task is None else args.task
    padding = 2 + max(len(task_utils.task_name(tsk))
            for tsk in task_utils.subtasks(task))

    for subtask in task_utils.subtasks(task):
        is_done = task_utils.is_done(task)
        entry = '[' + ('X' if is_done else ' ') + '] '
        entry += COLORS['green'] if is_done else COLORS['blue'] + COLORS['bold']
        entry += task_utils.task_name(subtask).ljust(padding)
        entry += COLORS['reset']
        entry += task_utils.task_description(subtask)
        print(entry)

def done(args):
    task_utils.complete_task(args.task)

def edit(args):
    task_utils.edit_attribute(args.attribute, create=args.create)

def main():
    """the current task is stored either in an environment variable or in the
    .smt directory.
    """
    parser = argparse.ArgumentParser(description=__doc__)
    actions = parser.add_subparsers(dest='action')

    ls_action = actions.add_parser('list', aliases=['ls'],
            help='list subtasks of the active task')
    ls_action.add_argument('task', nargs='?',
            help='specify the active task')
    ls_action.set_defaults(func=ls)

    add_action = actions.add_parser('add',
            help='Add a task')
    add_action.add_argument('name',
            help='The name of the task')
    add_action.add_argument('-d', '--description',
            help='The description of the task')
    add_action.add_argument('--due-date',
            help='The due date of the task in iso format')
    add_action.add_argument('--completion-time',
            help='The expected time to complete the task')
    add_action.set_defaults(func=add)

    done_action = actions.add_parser('done',
            help='mark the active task as complete')
    done_action.add_argument('task',
            help='spectify the active task')
    done_action.set_defaults(func=done)

    edit_action = actions.add_parser('edit',
            help='change an attribute of the current task')
    edit_action.add_argument('attribute',
            help='the attibute you would like to change')
    edit_action.add_argument('-c', '--create', action='store_true',
            help='create the attribute if it does not exist')
    edit_action.set_defaults(func=edit)

    args = parser.parse_args()

    if args.action is None:
        pass
    else:
        args.func(args)


if __name__ == '__main__':
    main()
