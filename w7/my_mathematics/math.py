import math
import cmath
class MyMath:
    pi = 3.14
    _complex = False # Инкапсуляция

    @staticmethod
    def sin(x):
        return math.sin(x)

    @classmethod
    def complex(cls):
        return cls._complex
    @classmethod
    def sqrt(cls, x):
        if x < 0:
            if cls.complex() == False: # Полимофизм
                raise ValueError('This is an error')
            else:
                y = cmath.sqrt(x)
                return (y.real, y.imag)
        else:
            return math.sqrt(x)
class MyComplexMath(MyMath): # Наследоаоние
    _complex = True
