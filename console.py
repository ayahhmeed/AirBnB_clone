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
        args = arg.split()
        if not args:
            print("**class name is missing**")
            return
        class_name = args[0]
        if class_name not in HBNBCommand.__classes:
            print("**class doesnot exist**")
            return
        if len (args) < 2:
            print("**instance id is missing**")
            return
        obj.id = args[1]
        key = "{}.{}".format(class_name, obj_id)
        obj = storage.all().get(key)
        if obj is None:
            print("**no instance found**")
        else:
            print(obj)


HBNBCommand().cmdloop()

if __name__ == '__main__':
    HBNBCommand().cmdloop()
