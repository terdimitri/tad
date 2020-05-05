#!/usr/bin/env python
"""An application for storing and managing tasks in a hierarchal manner."""
import argparse
import json


def main():
    """the current task is stored either in an environment variable or in the
    .smt directory.
    """
    parser = argparse.ArgumentParser(description=__doc__)
    actions = parser.add_subparsers(dest='action')

    ls_action = actions.add_parser('list', aliases=['ls'], help='list subtasks of the active task')

    cd_action = actions.add_parser('cd', help='change the current active task')
    cd_action.add_argument('task')

    add_action = actions.add_parser('add')
    add_action.add_argument('name')
    add_action.add_argument('--description', help='The description of the task')
    add_action.add_argument('--due-date', help='The due date of the task in iso format')
    add_action.add_argument('--completion-time', help='The expected time to complete the task')

    comp_action = actions.add_parser('comp', help='complete a task')
    comp_action.add_argument('task')

    edit_action = actions.add_parser('edit', help='change an attribute of the current task')
    edit_action.add_argument('attribute', help='the attibute you would like to change')

    args = parser.parse_args()
    print(args)

if __name__ == '__main__':
    main()
