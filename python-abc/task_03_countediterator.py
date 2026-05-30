class CountedIterator():

    def __init__(self, data):
        self.__counter = 0
        self.__iterator = iter(data)

    def get_count(self):
        return self.__counter

    def __next__(self):
        self.__counter += 1
        return next(self.__iterator)
