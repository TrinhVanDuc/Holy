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

class MyComlexMath(MyMath): # Наследоаоние
    _complex = True  # Инкапсуляция и Наследоаоние
    

if __name__ == "__main__":
    My = MyMath()
    Mycompl = MyComlexMath()
    #возвращающий синус числа (число задано в радианах)
    print('Sin(1) = {}\nSin(pi) = {}\n'.format(My.sin(1),My.sin(MyMath.pi),))

    #класс MyComplexMath не падает и считает корень из отрицательного числа при вызове sqrt от отрицательного числа
    print('Square root of 8 = {}\nSquare root of -8 = {} '.format(My.sqrt(8),Mycompl.sqrt(-8)))

    #класс MyMath падает при вызове метода sqrt от отрицательного числа
    try:
        c = My.sqrt(-8)
        print(c)
    except Exception:
        print('There was an error!')
'''
Мы использовали классовый метод, а не статический потому что, 
классовый метод может получить доступ или изменить состояние класса, а статический метод - нет.
'''






