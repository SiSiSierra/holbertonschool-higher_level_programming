#!/usr/bin/python3
"""Module

Classes:
    CustomObject
"""
import pickle


class CustomObject():
    """CustomObject

    Functions:
        display
        serialize
        deserialize
    """

    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        print(f"Name: {self.name}\n\
Age: {self.age}\n\
Is Student: {self.is_student}")

    def serialize(self, filename):
        with open(filename, "wb") as f:
            pickle.dump(self, f)

    @classmethod
    def deserialize(cls, filename):
        try:
            with open(filename, "rb") as f:
                return pickle.load(f)
        except OSError:
            return None
        except pickle.UnpicklingError:
            return None
