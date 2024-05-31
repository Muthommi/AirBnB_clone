#!/usr/bin/python3
import cmd


class HBNBCommand(cmd.Cmd):

    prompt = '(hbnb)'

    def do_quit(self, arg):
        """Quit command that exits the program"""
        return True

    def do_EOF(self, arg):
        """Exits on EOF signal"""
        print()
        return True

    def emptyline(self):
        """Does nothing"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
