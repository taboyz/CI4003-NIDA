# -*- coding: utf-8 -*-
"""
Created on Wed Feb 21 11:46:36 2018

@author: kronprom
Handling Using Input
"""
while True:
    try:
        input_nonzero = int(input("Enter a nonzero integer:"))
        recirocal =  1/input_nonzero
        print ("The reciprocal of {0} is {1} ".format(input_nonzero,recirocal))
        break
    
    except ZeroDivisionError:
        print ("You entered zero. Try again")
        continue
    

