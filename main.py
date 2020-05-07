#!/usr/bin/env python
"""Usage:
    tad list [<task>]
    tad tree [<task>]
    tad add <task> [-d [<description>]]
    tad done [-u] <task>
    tad edit [<task>] [-c | -f] <attribute>
    tad -h | --help

Create and manage tasks.

Options:
    -h, --help         Show this message and exit
add
    -d, --description
                       Set description of the task. If description not given,
                       open an editor.
done
    -u, --undone       Mark a task as incomplete
edit
    -c, --create       Create the attribut if it does not exit
    -f, --fuzzy        Fuzzy find for an existing attribute
    <attribute>        The attribute to edit
"""

import docopt
import task_utils

def main():
    """le program"""
    arguments = docopt.docopt(__doc__)
    if arguments['<task>'] is None:
        arguments['<task>'] = './'

    if arguments['list']:
        for line in task_utils.ls_lines(arguments['<task>']):
            print(line)

    elif arguments['tree']:
        for line in task_utils.tree_lines(arguments['<task>']):
            print(line)

    elif arguments['add']:
        task = task_utils.add_task(arguments['<task>'])
        if arguments['--description']:
            if arguments['<description>'] is not None:
                task_utils.write_attribte(arguments['<description>']+'\n',
                                          'DESCRIPTION', task)
            else:
                task_utils.edit_attribute('DESCRIPTION', task=task, create=True)

    elif arguments['done']:
        if arguments['--undone']:
            task_utils.uncomplete_task(arguments['<task>'])
        else:
            task_utils.complete_task(arguments['<task>'])

    elif arguments['edit']:
        task_utils.edit_attribute(
                arguments['<attribute>'],
                task=arguments['<task>'],
                create=arguments['--create'],
                fuzzy=arguments['--fuzzy']
            )

if __name__ == '__main__':
    main()
