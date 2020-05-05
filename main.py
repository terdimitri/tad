#!/usr/bin/env python
"""An application for storing and managing tasks in a hierarchal manner."""
import argparse
import task_utils
import subprocess
import os

def add(args):
    task_utils.add_task(args.name)

def ls(args):
    task = './' if args.task is None else args.task
    for name in task_utils.subtask_names(task):
        print(name)

def done(args):
    task_utils.complete_task(args.task)

def edit(args):
    try:
        editor = os.environ['EDITOR']
    except KeyError:
        editor = 'vim'
    subprocess.call([editor, args.attribute.upper()])


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
    add_action.add_argument('--description',
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
    edit_action.set_defaults(func=edit)

    args = parser.parse_args()

    if args.action is None:
        pass
    else:
        args.func(args)


if __name__ == '__main__':
    main()
