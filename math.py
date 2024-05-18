#!/usr/bin/python3

import cmd

class Math(cmd.Cmd):
    """simple command line processor."""

    prompt = '(hbnb)'

    def do_multiply(self, s):
        """multiply two numbers provided as arguments."""
        args = s.split()
        if len(args) != 2:
            print("invalid calculation")
            return
        try:
            args = [int(arg) for arg in args]
        except ValueError:
            print("arguments should be numbers")
            return
        print(args[0] * args[1])

    def do_EOF(self, line):
        """Handle end of file (EOF)command to exit."""
        print("Exiting....")
        return True
    def do_quit(self, line):
        """Quit command to exit the program."""
        return True

if __name__ == '__main__':
    import sys
    if sys.stdin.isatty():
        Math().cmdloop()
    else:
        Math().stdin = sys.stdin
        Math().stdout = sys.stdout
        Math().cmdloop()
