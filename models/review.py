#!/usr/bin/python3
"""This module defines the Review class"""

from models.base_model import BaseModel

class Review(BaseModel):
    """This class represents a review for the HBNB project"""

    # public class attributes
    place_id = "" # it will be the Place.id
    user_id = "" # it will be the User.id
    text = ""
