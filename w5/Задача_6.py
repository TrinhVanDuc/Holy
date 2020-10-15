class Animal:
    __name = None
    __age = None
    __place = "Earth"
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def get_place(self):
        return self.__place

    def __str__(self):
        return self.print_animal()

class Zebra(Animal):
    __food = "Meat"

    def __init__(self,name, age, food):
        super().__init__(name, age)
        self.__food = food

    def get_food(self):
        return self.__food

    def print_animal(self):
        return f"Name:{self.get_name()}  Age:{self.get_age()}  Food:{self.get_food()}"

class Dolphin(Animal):
    __color = "Blue"

    def __init__(self,name, age, color):
        super().__init__(name, age)
        self.__color = color

    def get_color(self):
        return self.__color

    def print_animal(self):
        return f"Name:{self.get_name()}  Age:{self.get_age()}  color:{self.get_color()}"

    def what_especially(self):
        return ("clever")


z=Zebra("Roronoa","2","Grass")
z.get_place()
print(z)
d= Dolphin("Sunny","1","White")
d.get_place()
print(d, "\nHe is very",d.what_especially())



