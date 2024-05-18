#!/usr/bin/python3

import cmd

class Math(cmd.Cmd):
    def do_multiply(self, s):
        l = s.split()
        if len(l) != 2:
            print("invalid calculation")
            return
        try:
            l = [int(i) for i in l]
        except ValueError:
            print("arguments should be numbers")
            return
        print(l[0] * l[1])

    def do_EOF(self, line):
        print("Exiting....")
        return True

if __name__ == '__main__':
    Math().cmdloop()
