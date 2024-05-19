#!/usr/bin/python3

import cmd


class HBNB(cmd.Cmd):
    """Console for managing objects."""

    prompt = '(hbnb) '

    def do_EOF(self, args):
        """Handle end of file command to exit."""
        print("Exiting...")
        return True

    def do_quit(self, args):
        """Command to quit the console."""
        return True

    def emptyline(self):
        """Do nothing."""
        pass


if __name__ == '__main__':
    HBNB().cmdloop()
    import sys
    if sys.stdin.isatty():
        HBNB().cmdloop()
    else:
        HBNB().stdin = sys.stdin
        HBNB().stdout = sys.stdout
        HBNB().cmdloop()
