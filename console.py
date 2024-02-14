#!/usr/bin/python3

"""
Defines the HBnB console.
"""

import cmd
import argparse
from codeop import CommandCompiler
import linecache
import re
# import sys
from models import storage
from models.base_model import BaseModel
# from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


def parse (arg: str) -> list:
    # parser = argparse.ArgumentParser(description='Process commands.')
    # parser.add_argument('command')
    # arguments = parser.parse_args()
    # print(arguments)
   paresed = re.split(r"[ .(),]", arg)
   return paresed


class HBNBCommand(cmd.Cmd):

    """
    Defines the HBnB command interpreter.
    """
    prompt = '(hbnb)'
    __classes = {
        "BaseModel",
        "User",
        "State",
        "City",
        "Place",
        "Amenity",
        "Review"
    }


    def default(self, arg):
        """Default behavior for cmd module when input is invalid"""
        pass

    def emptyline(self):
        """Do nothing upon receiving an empty line."""
        pass

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, arg):
        """EOF signal to exit the program."""
        print("")
        return True

    def do_create(self, arg):
        """Create a new class instance and print its id."""
        args = arg.split()
        if not args:
            print("**the class name missing**")
            return

        class_name = args[0]
        if class_name not in HBNBCommand.__classes:
            print("**the class does not exist**")
            return
        new_obj = eval("{}()".format(class_name))
        new_obj.save()
        print(new_obj.id)
        

    def do_show(self, arg):
        """show instance based on class name and id"""
        commands = parse(arg)
        if arg == "":
            print("** class name missing **")
        elif commands[0] not in HBNBCommand.CLASSNAMES:
            print("** class doesn't exist **")
        elif len(commands) < 2:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(commands[0], commands[1])
            if key not in storage.all():
                print("** no instance found **")
            else:
                print(storage.all()[key])
    def do_destroy(self, arg):
        comm = arg.split()
        if not comm or len(comm) != 2 or comm[0] != "id":
            print("destroy id")
            return
        try:
            obj = int(comm[1])
        except ValueError:
            print("invalid id")
            return
        del object(obj)
        def do_all(self, arg):
        pass
    def do_count(self, arg):


HBNBCommand().cmdloop()

if __name__ == '__main__':
    HBNBCommand().cmdloop()
