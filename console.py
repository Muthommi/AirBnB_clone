#!/usr/bin/python3

import cmd


class HBNB(cmd.Cmd):
    """Console for managing objects."""

    prompt = '(hbnb)'

    def do_create(self, args):
        """Creates a new user."""
        pass

    def do_update(self, args):
        """Updates the details of the user."""
        pass

    def do_destroy(self, args):
        """Deletes a certain user."""
        pass

    def do_show(self, args):
        """Shows the user."""
        pass

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
    if sys.stdin.isatty():
        HBNB().cmdloop()
    else:
        HBNB().stdin = sys.stdin
        HBNB().stdout = sys.stdout
        HBNB().cmdloop()
