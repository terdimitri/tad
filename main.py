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

def main():
    """le program"""
    args = docopt.docopt(__doc__,
                         options_first=True)
    argv = [args['<command>']] + args['<args>']

    if args['<command>'] == 'list':
        import tad_list
        tad_list.main(docopt.docopt(tad_list.__doc__, argv=argv))

    elif args['<command>'] == 'tree':
        import tad_tree
        tad_tree.main(docopt.docopt(tad_tree.__doc__, argv=argv))

    elif args['<command>'] == 'add':
        import tad_add
        tad_add.main(docopt.docopt(tad_add.__doc__, argv=argv))

    elif args['<command>'] == 'done':
        import tad_done
        tad_done.main(docopt.docopt(tad_done.__doc__, argv=argv))

    elif args['<command>'] == 'edit':
        import tad_edit
        tad_edit.main(docopt.docopt(tad_edit.__doc__, argv=argv))
    
    else: print("tad: %r is not a valid command. See 'tad --help'."
                % args['<command>'])

if __name__ == '__main__':
    main()
