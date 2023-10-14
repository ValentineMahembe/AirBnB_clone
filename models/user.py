#!/usr/bin/python3
"""This module defines the User class"""

from models.base_model import BaseModel

class User(BaseModel):
    """This class represents a user for the HBNB project"""

    # public class attributes
    email = ""
    password = ""
    first_name = ""
    last_name = ""
