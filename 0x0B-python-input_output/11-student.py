#!/usr/bin/python3
"""
a module that contains a class Student
"""


class Student:
    """a class that defines a student"""
    def __init__(self, first_name, last_name, age):
        """Instantiation"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Public method that retrieves a dictionary"""
        if (type(attrs) == list and
                all(type(ele) == str for ele in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__

    def reload_from_json(self, json):
        """Public method that replaces all attributes"""
        for k, v in json.items():
            setattr(self, k, v)
