#!/usr/bin/python3
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """ The BaseModel class is a base class.

    Attributes:
        - id (str): unique id genetator
        - created_at (datetime): the timestamp for when object is created
        - updated_at (datetime): the timestamp for when object is updated

     """
    def __init__(self, *args, **kwargs):
        """ Initializing  instances for the cclass named BaseModel

        Parameters:
         - args: this was not used
         - kwargs (dict): Keyword arguments of the object's attributes.
            If "__class__" is present in kwargs, it is ignored.
            If "created_at" or "updated_at" is present, it will be on ISO.
        """

        if kwargs is not None:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                elif key == "created_at" or key == "updated_at":
                    value = datetime.fromisoformat(value)
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """ Returns a string representation of the BaseModel object.

        Returns:
        - str:  A formatted string
        """

        the_class_name = self.__class__.__name__
        return f"[{the_class_name}] ({self.id}) {self.__dict__}"

    def save(self):
        """ Updates the updated_at """

        self.updated_at = datetime.now()

    def to_dict(self):
        """ Converts the BaseModel object to a dictionary.

        Returns:
        - dict: A dictionary
        """

        iso_of_created = self.created_at.isoformat()
        iso_of_updated = self.updated_at.isoformat()
        the_class = self.__class__.__name__

        my_dict = {
                "__class__": the_class,
                "created_at": iso_of_created,
                "updated_at": iso_of_updated,
                }
        my_dict.update(self.__dict__)

        return my_dict
