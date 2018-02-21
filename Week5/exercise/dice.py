# -*- coding: utf-8 -*-
"""
Created on Thu Feb  8 21:39:40 2018

@author: kronprom
"""

import random    


class PairOfDice:
    def __init__(self, red_die=0, blue_die=0):
        pass
    
    def get_red_die(self):
        return self._red_die
    
    def get_blue_die(self):
        return self._blue_die
    
    def roll(self):
        self._red_die = random.randint(1,6)
        self._blue_die = random.randint(1,6)
        
    def sum(self):
        return self._red_die + self._blue_die
    
    
    
def main():
    
    die1 = PairOfDice()
    die1.roll()
    player1 = die1.sum()
    print ("player1:", player1)
    
    die1.roll()
    player2 = die1.sum()
    print ("player2:", player2)
    
    #print ("p1={} p2={}".format(player1,player2))
    
    if player1 == player2:
        print ("TIE")
    elif player1 > player2:
        print ("Player 1 wins")
    elif player1 > player2:
        print ("Player 2 wins")
        
        
    
#main()    
    
        
        