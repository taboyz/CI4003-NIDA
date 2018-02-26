# -*- coding: utf-8 -*-
"""
Created on 

@author: kronprom
"""

input_txt =  input("Enter  Strings:")

def check_vowels(bstring):
    vcounter = 0
    vowels_list = ["a","e","i","o","u"]
    for i in bstring:
        
        if i.lower() in vowels_list :
            vcounter += 1
            print (i," is vowles", " counter =",vcounter) 
            
        else :
             print (i," NO ")
    return vcounter


print ("tolal vowels:",check_vowels(input_txt))