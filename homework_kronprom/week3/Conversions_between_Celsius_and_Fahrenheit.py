# -*- coding: utf-8 -*-
"""
Created on Mon Feb 26 15:32:52 2018

@author: kronprom
"""

def celsius_to_fahrenheit(celsius):
    return (9 / 5) * celsius + 32

def fahrenheit_to_celsius(fahrenheit):
    return (5 / 9) * (fahrenheit - 32)

n = 0
while n <= 10 :
    print ( n, " c = ",celsius_to_fahrenheit(n) , "f")
    n = n + 1

n = 0   
while n <= 10 :
    print ( n, " f = ",fahrenheit_to_celsius(n) , "c")
    n = n + 1
