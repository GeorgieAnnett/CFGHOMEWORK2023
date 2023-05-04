import abc

class Shape(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def calc_perimeter(self, input):
        """Method documentation"""
        return

class Triangle(Shape):

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def calc_perimeter(self):
        perim = self.a + self.b + self.c
        print("Consider me implemented", perim)
        return perim

class Rectangle(Shape):

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calc_perimeter(self):
        perim2 = 2*(self.length + self.width)
        print("Consider me implemented", perim2)
        return perim2

class Square(Shape):

    def __init__(self, equal_side):
        self.equal_side = equal_side

    def calc_perimeter(self):
        perim3 = 4* self.equal_side
        print("Consider me implemented", perim3)
        return perim3

