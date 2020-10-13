class Shape:
    def __init__(self,width, height):
        self.width = width
        self.height = height

class Triangle(Shape):
    def area(self):
        return (self.width)*(self.height)*0.5

class Rectangle(Shape):
    def area(self):
        return (self.width)*(self.height)
    
tr1 = Triangle(4,3)
print(tr1.area())   #6.0
tr2 = Rectangle (4,3)
print(tr2.area())   #12
