#!/usr/bin/env python
"""Usage:
    tad <command> [<args>...]
    tad -h | --help

Create and manage tasks.

Commands:
    list    List tasks
    tree    Show task tree
    add     Add a task
    done    Mark a task as done
    edit    Edit attributes of a task

Options:
    -h, --help         Show this message and exit
"""

import docopt
import sys

def main():
    """le program"""
    args = docopt.docopt(__doc__,
                         options_first=True)
    argv = [args['<command>']] + args['<args>']

    if args['<command>'] == 'list':
        import commands.tad_list as command

    elif args['<command>'] == 'tree':
        import commands.tad_tree as command

    elif args['<command>'] == 'add':
        import commands.tad_add as command

    elif args['<command>'] == 'done':
        import commands.tad_done as command

    elif args['<command>'] == 'edit':
        import commands.tad_edit as command
    
    else:
        print("tad: %r is not a valid command. See 'tad --help'."
                % args['<command>'])
        sys.exit(1)

    command.main(docopt.docopt(command.__doc__, argv=argv))

if __name__ == '__main__':
    main()
