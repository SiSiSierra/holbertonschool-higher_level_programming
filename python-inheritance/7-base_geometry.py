#!/usr/bin/python3
""" Module

Classes:
    BaseGeometry()

"""


class BaseGeometry():
    """BaseGeometry

    Instance:
    Functions:
        area(self): Area of shape
        integer_validator(self, name, value): Validate value to integer
    """

    def area(self):
        """ not implemented
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ Validate if value is a positive integer

        Parameters:
            name: String assigned to name of attribute
            value: Should be positive integer

        Raises:
            TypeError if value is not an int
            ValueError is value is not positive
        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
