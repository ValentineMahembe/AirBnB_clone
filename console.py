#!/usr/bin/python3
"""This module defines the HBNBCommand class"""

import cmd

class HBNBCommand(cmd.Cmd):
    """This class represents a command interpreter for the HBNB project"""

    prompt = "(hbnb) " # a custom prompt

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True # return True to exit the cmdloop

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        return True # return True to exit the cmdloop

    def emptyline(self):
        """An empty line + ENTER shouldn’t execute anything"""
        pass # do nothing

if __name__ == '__main__':
    HBNBCommand().cmdloop()
