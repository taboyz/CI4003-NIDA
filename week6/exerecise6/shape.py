# -*- coding: utf-8 -*-
"""
Created on Wed Feb 14 10:40:53 2018

@author: kronprom
"""

class Shape:
    def __init__(self, color):
        self._color = color
        
    def get_color(self):
        return self._color
    
    def set_color(self, color):
        self._color = color
    
    def get_area (self):
        return "0"
    
    def get_circumference(self):
        return "0" 
    


    def __str__(self):
        return "Hello"
    
    
class Circle(Shape):
    def __init__(self, color, radius):
        super().__init__(color)
        self._radius = radius
        
    def get_area(self):
        return (22/7)*self._radius*self._radius

    def get_circumference(self):
            return (22/7)*2*self._radius
        
    def __str__(self):
        return "Circle"
    
class Square(Shape):
    def __init__(self, color, width):
        super().__init__(color)
        self._width = width
    
    def get_area(self):
        return 2*self._width

    def get_circumference(self):
            return 4*self._width
        
    def __str__(self):
        return "Square"    
    

class Triangle(Shape):
    def __init__(self, color, a, b, c):
        super().__init__(color)
        self._a = a
        self._b = b
        self._c = c
    
    def get_area(self):
        import math
        s = (self._a+self._b+self._c)/2
        area = math.sqrt(s*((s-self._a)*(s-self._b)*(s-self._c)))  
        return area

    def get_circumference(self):
        return self._a + self._b + self._c
        
    def __str__(self):
        return "Triangle"    

class Rectangle(Shape):
    def __init__(self, color, width, height):
        super().__init__(color)
        self._width = width
        self._height = height
    
    
    def get_area(self):
        return self._width * self._height

    def get_circumference(self):
        return 2 * (self._width + self._height)
        
    def __str__(self):
        return "Rectangle" 


circle1 = Circle('REF',3)
print (circle1)
print (circle1.get_area())
print (circle1.get_circumference())


sq1 = Square('SQ1',3)
print (sq1)
print (sq1.get_area())
print (sq1.get_circumference())


t1 = Triangle('SQ1',3,4,5)
print (t1)
print (t1.get_area())
print (t1.get_circumference())

r1 = Rectangle('SQ1',3,4)
print (r1)
print (r1.get_area())
print (r1.get_circumference())

