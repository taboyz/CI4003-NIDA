# -*- coding: utf-8 -*-
"""
Created on Mon Feb 26 15:29:25 2018

@author: kronprom
"""

def fv_cal(p,i_year,y):
    i_month = i_year /12
    fv = p * (1 + i_month) ** (y * 12)
    return fv
  
        
input_principle = float(input(" Enter Principle amount:"))
input_int_rate = float(input("Enter int rate per annual  ex  9% input 0.09:"))
input_year = int(input("Year:"))

fv =  fv_cal(input_principle,input_int_rate,input_year)
#print (fv)

print ("table  1 to ",input_year," years")

num_year = 1

while num_year <= input_year :
    
    print("year:", num_year , "fv:", fv_cal(input_principle,input_int_rate,num_year) )   #n
  
    num_year = num_year + 1