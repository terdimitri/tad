"""Usage:
    tad tree [-d <depth>] [<task>]

Show the task tree.

Options:
    -h, --help           Show this message and exit.
    -d, --depth <depth>  Maximum recusion depth to show tasks.
"""

import task_utils

def main(args):
    task = '.' if args['<task>'] is None else args['<task>']
    for line in task_utils.tree_lines(task):
        print(line)
