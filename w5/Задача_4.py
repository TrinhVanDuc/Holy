class Shape:
    _area = -1

    def __init__(self, area, length):
        self._area = area
        self._length = length

    def get_area(self):
        raise NotImplementedError()

    def __int__(self, width, height):
        self.width = width
        self.height = height
    def area(self):
        print('Area is:',self.get_area())

class Triangle(Shape):
    
    def __init__(self, side1, side2):
        self.side1 = side1
        self.side2 = side2
        
    def get_area(self):
        if self._area == -1:
            self._area = (self.side1)*(self.side2)
        return self._area

tr1 = Triangle(4,3)
tr1.area()
