#!/usr/bin/env python
"""Usage:
    tad list [<task>]
    tad tree [<task>]
    tad add <task> [-d [<description>]]
    tad done <task>
    tad edit [<task>] [-c | -f] <attribute>
    tad -h | --help

Options:
    list               List the tasks
    tree               List tasks in a tree
    add                Add a task
    done               Mark a task as done
    edit               Edit an attribue of a task
    <task>             The task on which to operate [default: './']
    -d, --description  Specify the description of the task
    <description>      The description of the task, if not given opens an editor
    -c, --create       Create the attribut if it does not exit
    -f, --fuzzy        Fuzzy find for an existing attribute
    <attribute>        The attribute to edit
    -h, --help         Print this message
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
