# -*- coding: utf-8 -*-
"""
Created on Tue Feb  6 18:44:48 2018

@author: kronprom
"""

input_int = int(input('Enter a positive integer'))

def SumofAllOddSquares(a_int):
    
    SumOfSquares = 0
    for i in range (1,a_int,2) :
        print ("{} = {}".format(i,i**2))
        SumOfSquares += i ** 2
    return SumOfSquares

print (SumofAllOddSquares(input_int))