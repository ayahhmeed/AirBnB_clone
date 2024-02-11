#!/usr/bin/python3

"""
Defines the HBnB console.
"""

import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review

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
        pass
    def do_show(self, arg):
        pass
    def do_destroy(self, arg):
        pass
    def do_all(self, arg):
        pass
    def do_count(self, arg):
        pass
    def do_update(self, arg):
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
