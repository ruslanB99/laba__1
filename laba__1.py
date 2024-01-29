# TODO Написать 3 класса с документацией и аннотацией типов
import doctest
import math


class Figure:
    def __init__(self, perimeter=None, space=None):
      self.perimeter = perimeter
      self.space = space
      self.infoFig = []

    def calcPerimeter(self):
        pass

    def calcSpace(self):
        pass

    def figInfo(self):
        p = self.calcPerimeter()
        s = self.calcSpace()
        print('периметр = %s площадь = %s' % (p, s))
class Rectangle(Figure):
    def __init__(self, x, y, w, h):
     Figure.__init__(self)
     self.x = x
     self.y = y
     self.w = w
     self.h = h
    def calcPerimeter(self):
        perimeter = self.w * 2 + self.h * 2
        return perimeter
    def calcSpace(self):
        space = self.x * self.y
        return space
    def figInfo(self):
        p = self.calcPerimeter()
        s = self.calcSpace()
        print('У прямоугольника периметр = %s площадь = %s' % (p, s))
class Circle(Figure):
    def __init__(self, r):
     Figure.__init__(self)
     self.r = r

    def calcPerimeter1(self):
        perimeter = 2 * self.r * math.pi
        return perimeter

    def calcSpace1(self):
        space = math.pi * self.r ** 2
        return space


    def figInfo1(self):
        p = self.calcPerimeter()
        s = self.calcSpace()
        print('У  круга периметр = %s площадь = %s' % (p,s))

class Triangle(Figure):
    def __init__(self,a,b,c,k):
       Figure.__init__(self)
       self.a = a
       self.b = b
       self.c = c
       self.k = k
    def calcPerimeter2(self):
          perimeter = self.a +  self.b +  self.c
          return perimeter
    def calcSpace2(self):
         space = 0.5 *  self.a * self.k
         return space

    def figInfo2(self):
         p = self.calcPerimeter()
         s = self.calcSpace()
         print('У  треугольника периметр = %s площадь = %s' % (p, s))
if __name__ == "__main__":
    print(Rectangle.calcPerimeter)
    print(Circle.calcPerimeter1)
    print(Triangle.calcPerimeter2)
     doctest.testmod()
    # TODO работоспособность экземпляров класса проверить с помощью doctest

