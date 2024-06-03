#!/usr/bin/python3
"""
This module defines the HBNBCommand class for the command interpreter.
"""

import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """Command interpreter class for HBNB"""
    prompt = '(hbnb)'

    classes = {
            "BaseModel": BaseModel,
            "User": User,
            "State": State,
            "City": City,
            "Amenity": Amenity,
            "Place": Place,
            "Review": Review
    }

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        return True

    def emptyline(self):
        """Do nothing on empty input line"""
        pass

    def do_create(self, arg):
        """Creates a new instance of BaseModel"""
        if not arg:
            print("** class name missing **")
            return
        if arg not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        new_instance = HBNBCommand.classes[arg]()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, arg):
        """Prints string rep of an instance"""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        if args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = f"{args[0]}.{args[1]}"
        if key not in storage.all():
            print("** no instance found **")
            return
        print(storage.all()[key])

    def do_destroy(self, arg):
        """Deletes an instance based on class name and id"""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        if args[0] not in HNBCommand.classes:
            print("** class doesn't exist")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = f"{args[0]}.{args[1]}"
        if key not in storage.all():
            print("** no intance found **")
            return
        del storage.all()[key]
        storage.save()

    def do_all(self, arg):
        """Prints all string reps of all instances"""
        if arg and arg not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        object = storage.all()
        if not arg:
            print([str(obj) for obj in objects.values()])
        else:
            print([str(obj) for obj in objects.values() if obj.__class__.__name__ == arg])

    def do_update(self, arg):
        """Updates an instance based on the class name and id"""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        if args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = f"{args[0]}.{args[1]}"
        if key not in storage.all():
            print("** no instance found **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return

        instance = storage.all()[key]
        setattr(instance, args[2], eval(args[3]))
        instance.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
