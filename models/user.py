#!/usr/bin/python3
<<<<<<< HEAD
"""This module defines a class User"""
=======
>>>>>>> df9672565a70ee496982abbbc11282820c5ff266
from models.base_model import BaseModel


class User(BaseModel):
<<<<<<< HEAD
    """This class defines a user by various attributes"""
    email = ''
    password = ''
    first_name = ''
    last_name = ''
=======
    """ ser class that inherits from BaseModel."""

    email: str = ""
    password: str = ""
    first_name: str = ""
    last_name: str = ""
>>>>>>> df9672565a70ee496982abbbc11282820c5ff266
