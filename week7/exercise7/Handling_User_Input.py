# -*- coding: utf-8 -*-
"""
Created on Wed Feb 21 11:46:36 2018

@author: kronprom
Handling Using Input
"""

while True:
    try:
        input_1 = int(input("Enter a  integer from 1 to 100:"))
       
    except ValueError as error1:
        print (error1)
        print ("You did not input integer")
        continue
    if input_1 not in range(1,100):
        print ("ํYour Number was not between 1 and 100")
        continue
    else: 
        print ("your number is {0}   ".format(input_1))
        break