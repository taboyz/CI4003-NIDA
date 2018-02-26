# -*- coding: utf-8 -*-
"""
Created on 

@author: kronprom
"""

def is_triangle(a, b, c):
    max_t =max(a,b,c)
    print ("Max Value is :",max_t)
    if max_t < ((a+b+c)-max_t) :
        return "Is Triangle"
    else:
        return "Not Triangle"
    
    

a = float(input("a:"))
b = float(input("b:"))
c = float(input("c:"))

print (is_triangle(a,b,c))