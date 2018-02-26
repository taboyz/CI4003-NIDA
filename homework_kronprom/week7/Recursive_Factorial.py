# -*- coding: utf-8 -*-
"""
Created on Wed Feb 21 18:55:01 2018

@author: kronprom
"""
def factorial(n):
    if n == 1 or n == 0:
        return 1
    else:
        return  n * factorial(n-1)
    
    
    
    
print (factorial(10))