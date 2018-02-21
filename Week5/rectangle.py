# -*- coding: utf-8 -*-
"""
Created on Wed Feb  7 09:42:23 2018

@author: Pramote
"""

class Rectangle:
    def __init__(self, width=0, height=0):
        self._width = width
        self._height = height
    
    def get_width(self):
        return self._width
    
    def get_height(self):
        return self._height
    
    def set_width(self, width):
        self._width = width
        
    def set_height(self, height):
        self._height = height
        
    def get_area(self):
        return self._width * self._height
        
    def __str__(self):
        return f'{self._width}x{self._height}'
    