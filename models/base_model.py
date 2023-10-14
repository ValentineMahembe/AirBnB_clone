#!/usr/bin/python3
"""This module defines the BaseModel class"""

import uuid
from datetime import datetime

class BaseModel:

    """This class represents a base model for other classes"""

    def __init__(self, *args, **kwargs):
        """Initializes a new instance of BaseModel"""
        if kwargs:
            # if kwargs is not empty, create an instance from a dictionary
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    # convert string to datetime object
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key != "__class__":
                    # set the attribute with the value
                    setattr(self, key, value)
        else:
            # if kwargs is empty, create a new instance with default values
            self.id = str(uuid.uuid4()) # generate a unique id
            self.created_at = datetime.now() # assign current datetime
            self.updated_at = self.created_at # assign current datetime

    def __str__(self):
        """Returns a string representation of the instance"""
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """Updates the updated_at attribute with the current datetime"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Returns a dictionary representation of the instance"""
        result = self.__dict__.copy() # make a copy of the instance dictionary
        result["__class__"] = self.__class__.__name__ # add the class name as a key
        result["created_at"] = self.created_at.isoformat() # convert datetime to string
        result["updated_at"] = self.updated_at.isoformat() # convert datetime to string
        return result
