"""Usage:
    tad done [-u] [<task>]

Mark task as done.

Options:
    -u --undone  Mark task as not done
    -h, --help   Show this message and exit
"""
import task_utils

def main(args):
    task = '.' if args['<task>'] is None else args['<task>']
    if args['--undone']:
        task_utils.uncomplete_task(task)
    else:
        task_utils.complete_task(task)
