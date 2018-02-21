# -*- coding: utf-8 -*-
"""
Created on Fri Feb 16 15:46:43 2018

@author: Pramote
"""

import random

def spin_wheel():
    n = random.randint(1, 20)
    if n > 15:
        return 'Cherries'
    elif n > 10:
        return 'Orange'
    elif n > 5:
        return 'Plum'
    elif n > 2:
        return 'Melon'
    elif n > 1:
        return 'Bell'
    else:
        return 'Bar'

def main():
    
    ans = 'y'
    while ans in ['y', 'Y']:
        for i in range(3):
            outcome = spin_wheel()
            print(outcome, end=' ')
        ans = input('Do you want to continue? ')
        
main()
