# -*- coding: utf-8 -*-
"""
Created on Mon Feb 26 15:48:16 2018

@author: kronprom
"""

    
def SumofAllOddSquares(a_int):
    
    SumOfSquares = 0
    for i in range (1,a_int,2) :
        SumOfSquares += i ** 2
    return SumOfSquares



try:
    input_int = int(input('Enter a positive integer:'))
except:
    input_int = 0
    
print (SumofAllOddSquares(input_int))