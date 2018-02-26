# -*- coding: utf-8 -*-
"""
Created on Mon Feb 26 15:53:49 2018

@author: kronprom
"""

input_numbers = input('Enter a sequence of numbers separated by comma (,):')

def CheckDistinctNumber(a_seq):  
    seq_list = a_seq.split(",")

    for i in seq_list:
        print (i , "count",seq_list.count(i))
        if seq_list.count(i) > 1 :
            return_result = "Duplicate Found"
        else:
            return_result = "Not Duplicate"
            
    return  return_result

print (CheckDistinctNumber(input_numbers))