# -*- coding: utf-8 -*-
"""
Created on 

@author: kronprom
"""

number_input = input("Enter a Number:")
try:
    number = float(number_input)
    
except:
    number = 0
    print ("Error input type")
    
if (number % 2) == 0:
    print ("even")
    
else:
    print ("odd")