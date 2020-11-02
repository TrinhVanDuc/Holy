import numpy as np
class Vector:
    def __init__(self,*args):
        self.__args = args

    def __str__(self):
        return f'{self.__args}'
    def __add__(self, other):
        return np.add(self.__args, other.__args)
    def __sub__(self, other):
        return np.subtract(self.__args, other.__args)
    def __and__(self, other):
        return np.dot(self.__args, other.__args)
    def dictances(self):
        s = 0
        for i in self.__args:
            s = s+i**2
        distance = s**0.5
        return distance
