# -*- coding: utf-8 -*-
"""
Created on Wed Feb 21 18:26:28 2018

@author: kronprom
"""
import random

class paoyingchob:
    def __init__(self,hand=""):
        self._hand = hand
        self._value = ['paper','scissors','rock']
    
    def play(self):
        return random.choice(self._value)
    
    def __str__(self):
        return "Paoyingchob"+self._hand
    

def result(p1,p2):
    print ("Player 1:",p1)
    print ("Player 2:",p2)
    if p1 == p2:
        print ("TIE")
        
    elif p1 == "paper" and p2 == "rock":
        print ("Player 1 wins")
    
    elif p1 == "rock" and p2 == "scissors":
        print ("Player 1 wins")

    elif p1 == "scissors" and p2 == "paper":
        print ("Player 1 wins")
    else:
        print ("Player 2 wins")

def main():
    player1 = paoyingchob()
#    player1_result = player1.play()
    
    player2 = paoyingchob()
#    player2_result = player2.play()
    
    result( player1.play(), player2.play())


main()    
                