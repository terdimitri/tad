#!/usr/bin/env python
"""An application for storing and managing tasks in a hierarchal manner."""
import argparse


def main():
    """the current task is stored either in an environment variable or in the
    .smt directory.
    """
    parser = argparse.ArgumentParser(description=__doc__)
    actions = parser.add_subparsers(dest='action')

    ls_action = actions.add_parser('list', aliases=['ls'],
            help='list subtasks of the active task')
    ls_action.add_argument('task',
            help='specify the active task')

    add_action = actions.add_parser('add')
    add_action.add_argument('name')
    add_action.add_argument('--description',
            help='The description of the task')
    add_action.add_argument('--due-date',
            help='The due date of the task in iso format')
    add_action.add_argument('--completion-time',
            help='The expected time to complete the task')

    done_action = actions.add_parser('done',
            help='mark the active task as complete')
    done_action.add_argument('task',
            help='spectify the active task')

    edit_action = actions.add_parser('edit',
            help='change an attribute of the current task')
    edit_action.add_argument('attribute',
            help='the attibute you would like to change')

    args = parser.parse_args()

    if args.action is None:
        pass


if __name__ == '__main__':
    main()
