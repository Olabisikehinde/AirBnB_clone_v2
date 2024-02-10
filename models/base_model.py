#!/usr/bin/python3
from uuid import uuid4
from datetime import datetime

class BaseModel:
    def __init__(self):
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        the_class_name = self.__class__.__name__
        return f"[{the_class_name}] ({self.id}) {self.__dict__}"

    def save(self):
        self.updated_at = datetime.now()

    def to_dict(self):
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

if __name__ == "__main__":
    base1 = BaseModel()
