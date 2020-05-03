#!/usr/bin/env python
"""An application for storing and managing tasks in a hierarchal manner."""
import argparse
import json


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    actions = parser.add_subparsers()
    add_action = actions.add_parser('add')
    add_action.add_argument('name')
    fin_action = actions.add_parser('fin')

    args = parser.parse_args()
    print(args)

if __name__ == '__main__':
    main()
