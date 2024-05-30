#!/usr/bin/python3
import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """Console for managing objects."""

    prompt = '(hbnb) '

    classes = {
        'BaseModel': BaseModel,
        'User': User,
        'Place': Place,
        'State': State,
        'City': City,
        'Amenity': Amenity,
        'Review': Review
    }

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

    def default(self, line):
        """Called on input line when the command prefix isn't recognized."""
        print(f"*** Unknown command: {line}")

    def do_create(self, line):
        """Creates an object."""
        args = line.split()
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in self.classes:
            print("** class doesn't exist **")
            return
        new_instance = self.classes[class_name]()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, line):
        """Show an object."""
        args = line.split()
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in self.classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        obj_id = args[1]
        key = f"{class_name}.{obj_id}"
        obj = storage.all().get(key)
        if not obj:
            print("** no instance found **")
        else:
            print(obj)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
