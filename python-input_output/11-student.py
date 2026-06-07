#!/usr/bin/python3
""" Module

Classes:
    Student
"""


class Student:
    """ Student class

    +first_name
    +last_name
    +age
    ---
    +to_json(self)
    +reload_from_json(self, json)
    """

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        dic = {}
        if type(attrs) is not list:
            dic = {
                    'first_name': self.first_name,
                    'last_name': self.last_name,
                    'age': self.age
                    }
        else:
            if 'first_name' in attrs:
                dic['first_name'] = self.first_name
            if 'last_name' in attrs:
                dic['last_name'] = self.last_name
            if 'age' in attrs:
                dic['age'] = self.age
        return (dic)

    def reload_from_json(self, json):
        """Set attributes from loaded json

        Parameters:
            json: Dict to use
        """
        try:
            self.first_name = json['first_name']
        except KeyError:
            pass
        try:
            self.last_name = json['last_name']
        except KeyError:
            pass
        try:
            self.age = json['age']
        except KeyError:
            pass
