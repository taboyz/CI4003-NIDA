# -*- coding: utf-8 -*-
"""
Created on Mon Feb 26 15:11:44 2018

@author: kronprom
"""

amount_input = input("Enter Amount:")
tip_percentage = input("Enter Tip in % :")

try:
    amount = float(amount_input)
    tip = float(tip_percentage)
    
except:
    amount = 1
    tip = 1

tip_amount = amount * tip / 100    
print (" TIP =", tip_amount)
