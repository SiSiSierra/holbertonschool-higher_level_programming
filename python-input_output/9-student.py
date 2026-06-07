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
    """

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        dic = {
                'first_name': self.first_name,
                'last_name': self.last_name,
                'age': self.age
                }
        return (dic)
