# -*- coding: utf-8 -*-
"""
Created on Fri Feb 16 15:33:47 2018

@author: Pramote
"""
import random

def is_odd(n):
    if (1 <= n <= 36) and (n%2 != 0):
        return True
    else:
        return False

def profit(n):
    if is_odd(n):
        return 1
    else:
        return -1
    
def play_double_or_nothing(bankroll):   
    amount = bankroll
    times_played = 0
    while 0 < amount < 2 * bankroll:
        # let 37 represent 00
        n = random.randint(0, 37)
        times_played += 1
        amount += profit(n)
    return (amount, times_played)

def main():
    bankroll = int(input('Enter the amount of bankroll : '))
    amount, times_played = play_double_or_nothing(bankroll)
    print(f'Ending bankroll : ${amount:0.0f}')
    print(f'Number of games played {times_played}')

main()