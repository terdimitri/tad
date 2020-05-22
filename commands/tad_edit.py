"""Usage:
    tad edit [-c | -f] <attribute>
    tad edit <task> [-c | -f] <attribute>

Edit an atribute of a task

Options:
    -c, --create    Create the attribute if it does not exist
    -f, --fuzzy     Fuzzy search for an existing attribute
    -h, --help      Show this message and exit
"""

import task_utils

def main(args):
    task = '.' if args['<task>'] is None else args['<task>']
    task_utils.edit_attribute(
            args['<attribute>'],
            task=task,
            create=args['--create'],
            fuzzy=args['--fuzzy']
        )
