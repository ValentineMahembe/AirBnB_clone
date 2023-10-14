#!/usr/bin/python3
"""This module defines the HBNBCommand class"""

import cmd
import json
from models.base_model import BaseModel
from models import storage

class HBNBCommand(cmd.Cmd):
    """This class represents a command interpreter for the HBNB project"""

    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True # return True to exit the cmdloop

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        return True # return True to exit the cmdloop

    def emptyline(self):
        """An empty line + ENTER shouldn’t execute anything"""
        pass # do nothing

    def do_create(self, arg):
        """Creates a new instance of BaseModel, saves it (to the JSON file)
        and prints the id. Ex: $ create BaseModel"""
        if not arg:
            print("** class name missing **") # if the class name is missing
        elif arg not in ["BaseModel"]: # you can add more valid class names here
            print("** class doesn't exist **") # if the class name doesn't exist
        else:
            obj = eval(arg)() # create a new instance of the class
            obj.save() # save it to the JSON file
            print(obj.id) # print the id

    def do_show(self, arg):
        """Prints the string representation of an instance based on th
        e class name and id. Ex: $ show BaseModel 1234-1234-1234."""
        args = arg.split() # split the arguments by space
        if not args:
            print("** class name missing **") # if the class name is missing
        elif args[0] not in ["BaseModel"]: # you can add more valid class names here
            print("** class doesn't exist **") # if the class name doesn't exist
        elif len(args) == 1:
            print("** instance id missing **") # if the id is missing
        else:
            key = args[0] + "." + args[1] # create the key for the object
            if key not in storage.all():
                print("** no instance found **") # if the instance doesn't exist for the id
            else:
                print(storage.all()[key]) # print the string representation of the object

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id (save
        the change into the JSON file). Ex: $ destroy BaseModel 1234-1234-1234."""
        args = arg.split() # split the arguments by space
        if not args:
            print("** class name missing **") # if the class name is missing
        elif args[0] not in ["BaseModel"]: # you can add more valid class names here
            print("** class doesn't exist **") # if the class name doesn't exist
        elif len(args) == 1:
            print("** instance id missing **") # if the id is missing
        else:
            key = args[0] + "." + args[1] # create the key for the object
            if key not in storage.all():
                print("** no instance found **") # if the instance doesn't exist for the id
            else:
                del storage.all()[key] # delete the object from storage
                storage.save() # save the change to the JSON file

    def do_all(self, arg):
        """Prints all string representation of all instances based or not
        on the class name. Ex: $ all BaseModel or $ all."""
        args = arg.split() # split the arguments by space
        result = [] # a list to store all string representations
        if not args: 
            for obj in storage.all().values(): 
                result.append(obj.__str__()) # add all objects to result
        elif args[0] not in ["BaseModel"]: # you can add more valid class names here
            print("** class doesn't exist **") # if the class name doesn't exist
            return 
        else: 
            for obj in storage.all().values(): 
                if obj.__class__.__name__ == args[0]: 
                    result.append(obj.__str__()) # add only objects of that class to result
        
        print(result) # print result as a list of strings

    def do_update(self, arg):
        """Updates an instance based on the class name and id by adding or updating 
        attribute (save the change into the JSON file)."""
        args = arg.split() # split the arguments by space
        if not args:
            print("** class name missing **") # if the class name is missing
        elif args[0] not in ["BaseModel"]: # you can add more valid class names here
            print("** class doesn't exist **") # if the class name doesn't exist
        elif len(args) == 1:
            print("** instance id missing **") # if the id is missing
        else:
            key = args[0] + "." + args[1] # create the key for the object
            if key not in storage.all():
                print("** no instance found **") # if the instance doesn't exist for the id
            elif len(args) == 2:
                print("** attribute name missing **") # if the attribute name is missing
            elif len(args) == 3:
                print("** value missing **") # if the value for the attribute name is missing
            else:
                obj = storage.all()[key] # get the object from storage
                try:
                    value = eval(args[3]) # try to evaluate the value as a Python literal
                except:
                    value = args[3] # otherwise, use the value as a string
                setattr(obj, args[2], value) # set or update the attribute with the value
                obj.save() # save the change to the JSON file

if __name__ == '__main__':
    HBNBCommand().cmdloop()
