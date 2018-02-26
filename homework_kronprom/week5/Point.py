# -*main- coding: utf-8 -*-
"""
Created on Mon Feb 26 16:48:27 2018

@author: kronprom
"""

import math
class Point:
    def __init__(self, x, y):
        self._x = x
        self._y = y
        
    def get_x(self):
        return self._x
    
    def get_y(self):
        return self._y
    
    def set_x(self, x):
        self._x = x
    
    def set_y(self, y):
        self._y = y

    def distance_from_origin(self):
        distance = math.sqrt((self._x * self._x)+(self._y * self._y))
        return distance
        
    def __str__(self):
        return ("x is {},y is {}".format(self._x,self._y))
    
    
def main():
    input_x = float(input("Enter the X-coordinate of point:"))
    input_y = float(input("Enter the Y-coordinate of point:"))
    point1 = Point(input_x,input_y)
    print ("Distance from origiin: {0:.2f}".format(point1.distance_from_origin()))
    
    
    
main()    