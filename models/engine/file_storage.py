#!/usr/bin/python3
"""This module defines the FileStorage class"""

import json
from models.base_model import BaseModel

class FileStorage:
    """This class serializes and deserializes instances to and from a JSON file"""

    __file_path = "file.json" # the path to the JSON file
    __objects = {} # an empty dictionary to store all objects

    def all(self):
        """Returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        key = obj.__class__.__name__ + "." + obj.id
        self.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)"""
        json_dict = {}
        for key, value in self.__objects.items():
            json_dict[key] = value.to_dict() # convert each object to a dictionary
        with open(self.__file_path, "w") as f:
            json.dump(json_dict, f) # write the dictionary to the file

    def reload(self):
        """Deserializes the JSON file to __objects (only if the JSON file 
        (__file_path) exists ; otherwise, do nothing. If the file doesn’t exist,
        no exception should be raised)"""
        try:
            with open(self.__file_path, "r") as f:
                json_dict = json.load(f) # read the dictionary from the file
            for key, value in json_dict.items():
                cls_name = value["__class__"] # get the class name from the dictionary
                cls = eval(cls_name) # get the class object from the name
                self.__objects[key] = cls(**value) # create an instance with the dictionary
        except FileNotFoundError:
            pass # do nothing if the file does not exist

