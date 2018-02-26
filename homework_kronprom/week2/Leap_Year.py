# -*- coding: utf-8 -*-
"""
Created on 

@author: kronprom
"""

input_year = input("Enter AD year:")
try:
    cal_year = int(input_year)
except:
    cal_year = 0

if (cal_year % 100) == 0:
    if cal_year % 400 == 0:
        print ("leap year")
    else :
        print("NOT leap year")
elif cal_year % 4 == 0:
    print  ("leap year")
    
else:
    print ("NOT Leap year")
