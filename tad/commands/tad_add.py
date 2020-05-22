"""Usage:
    tad add [options] <name> [-d [<description>]]

Options:
    -d, --description  Set description of the task. If not given as an
                       argument, write description in an editor.
    -o, --overwrite    Overwrite any existing tasks with the same name.
    -h, --help         Show this message and exit.
"""
import task_utils

def main(args):
    task = task_utils.add_task(args['<name>'])
    if args['--description']:
        if args['<description>'] is not None:
            task_utils.write_attribte(
                    args['<description>']+'\n', 'DESCRIPTION', task
                )
        else:
            task_utils.edit_attribute('DESCRIPTION', task=task, create=True)
