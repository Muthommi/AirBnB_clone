#!/usr/bin/python3

import cmd
import sys


class HBNBCommand(cmd.Cmd):
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
    import sys
    import os
    if os.isatty(sys.stdin.fileno()):
        HBNBCommand().cmdloop()
    else:
        cmd_instance = HBNBCommand()
        cmd_instance.use_rawinput = False
        cmd_instance.stdin = sys.stdin
        cmd_instance.stdout = sys.stdout
        cmd_instance.cmdloop()
