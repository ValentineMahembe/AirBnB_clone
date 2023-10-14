#!/usr/bin/python3
"""This module defines the FileStorage class"""

import json
from models.base_model import BaseModel
from models.user import User # import User class

class FileStorage:
    """This class serializes instances to a JSON file and deserializes JSON file to instances"""

    __file_path = "file.json" # path to the JSON file
    __objects = {} # dictionary that will store all objects by <class name>.id

    def all(self):
        """Returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        key = obj.__class__.__name__ + "." + obj.id # create the key for the object
        self.__objects[key] = obj # set the object in __objects

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)"""
        json_dict = {} # a dictionary to store JSON representations of objects
        for key, obj in self.__objects.items():
            json_dict[key] = obj.to_dict() # convert each object to a dictionary
        with open(self.__file_path, "w") as f:
            json.dump(json_dict, f) # dump the dictionary to the JSON file

    def reload(self):
        """Deserializes the JSON file to __objects (only if the JSON file
        (__file_path) exists ; otherwise, do nothing. If the file doesn’t exist,
        no exception should be raised)"""
        try:
            with open(self.__file_path, "r") as f:
                json_dict = json.load(f) # load the dictionary from the JSON file
                for key, value in json_dict.items():
                    cls_name = value["__class__"] # get the class name from the dictionary
                    cls = eval(cls_name) # get the class object from the name
                    obj = cls(**value) # create an instance of the class with the dictionary values
                    self.__objects[key] = obj # set the object in __objects
        except FileNotFoundError:
            pass # do nothing if the file doesn't exist
