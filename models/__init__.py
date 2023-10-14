#!/usr/bin/python3
"""This module creates a unique FileStorage instance for your application"""

from .engine.file_storage import FileStorage # use relative import

storage = FileStorage() # create a unique FileStorage instance
storage.reload() # call reload method on this instance

