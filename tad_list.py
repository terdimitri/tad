"""Usage:
    tad list [options] [<task>]

List subtasks.

Options:
    -h, --help   Show this message and exit.
"""
import task_utils

def main(args):
    task = '.' if args['<task>'] is None else args['<task>']
    for line in task_utils.ls_lines(task):
        print(line)
