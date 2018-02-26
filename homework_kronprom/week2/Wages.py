# -*- coding: utf-8 -*-
"""
Created on Mon Feb 26 15:12:53 2018

@author: kronprom
"""

hour_input = input("Enter hours:")
hourly_rate = input ("Enter hourly rate")

try:
    h = float(hour_input)
    r = float(hourly_rate)
except:
    h = 1
    r = 1


ot = 0

if h > 40:
    normal = 40 * r
    ot = (h-40)* (r*1.5)
else:
    normal = h * r
    

print("Normal:",normal, "  OT:",ot, "  Total:",normal+ot)