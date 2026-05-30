from abc import ABC, abstractmethod
""" Module

Classes:
    Animal(ABC)
    Dog(Animal)
    Cat(Animal)
"""


class Animal(ABC):
    """Abstract class Animal

    Functions:
        sound() (abstract)
    """
    @abstractmethod
    def sound(self):
        ...


class Dog(Animal):
    """Dog

    Functions:
        sound()
    """
    def sound(self):
        return "Bark"


class Cat(Animal):
    """Cat

    Functions:
        sound()
    """
    def sound(self):
        return "Meow"
