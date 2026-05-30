from abc import ABC, abstractmethod


class VerboseList(list):

    def append(self, value):
        super().append(value)
        print(f"Added [{value}] to the list")

    def extend(self, value):
        super().extend(value)
        print(f"Extended the list with [{len(value)}] items")

    def remove(self, value):
        print(f"Removed [{value}] from the list")
        super().remove(value)

    def pop(self, value=-1):
        print(f"Popped [{self[value]}] from the list")
        return super().pop(value)
