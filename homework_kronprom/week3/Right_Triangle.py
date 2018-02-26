# -*- coding: utf-8 -*-
"""
Created on 

@author: kronprom
"""

def  is_right_triangle(a,b,c):
    
    if (c ** 2) == (a**2) + (b**2):
        return "is right triangle"
    else:
        return "NOT Right triangle"
    
    
a = float(input("a:"))
b = float(input("b:"))
c = float(input("c opposite side:"))
print (is_right_triangle(a,b,c))