#!/usr/bin/python3
"""This module defines the City class"""

from models.base_model import BaseModel

class City(BaseModel):
    """This class represents a city for the HBNB project"""

    # public class attributes
    state_id = "" # it will be the State.id
    name = ""
