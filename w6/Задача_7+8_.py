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

if __name__ == '__main__':
    #арифметические операции.
    x= Vector(2,3,4)
    y= Vector(1,2,3)
    print(x+y)
    print(x-y)
    print(x&y)

    #найдите и выведите координаты точки, наиболее удаленной от начала координат
    N = int(input())
    i = 0
    list_ranges = []
    tuple_ranges = {}
    while i < N:
        a,b,c = list(map(int, input().split()))
        n = Vector(a,b,c)
        vector = (a,b,c)
        dictance = n.dictances()
        list_ranges.append(dictance)
        tuple_ranges[vector] = dictance
        i +=1
    max_distance = max(list_ranges)
    for vector_ in tuple_ranges.keys():
        if tuple_ranges[vector_] == max_distance:
            print('Vector {} have the farthest distancevector = {}'.format(vector_,max_distance))



