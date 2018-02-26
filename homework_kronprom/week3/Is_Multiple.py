# -*- coding: utf-8 -*-
"""
Created on 

@author: kronprom
"""

def is_multiple(n,m):
    if n % m == 0:
        return "true"
    else:
        return "false"
    
n = int(input(" n:"))    
m = int(input(" m:"))


result = is_multiple(n,m)
print (result)