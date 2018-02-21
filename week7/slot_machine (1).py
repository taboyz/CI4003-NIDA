# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 14:19:19 2017

@author: Pramote
"""

import random

class SlotMachine:
    
    def __init__(self):
        self._stake = 0
        self._winning = 0
        self._wheels = [None, None, None]
        self._items = ['Cherry', 'Lemom', 'Melon', 'Orange', 'Plum', 'Bell', 'Bar']
 
    def spin_wheels(self):
        self._wheels[0] = random.choice(self._items)
        self._wheels[1] = random.choice(self._items)
        self._wheels[2] = random.choice(self._items)
    
    def deposit(self, amount):
        self._stake += amount
    
    def get_stake(self):
        return self._stake
    
    def play(self):
        if self._stake > 0:
            self.spin_wheels()
            self.calculate_payouts()
            self.display()
        else:
            print('Please deposit more cash.')
        
    def calculate_payouts(self):
        winning = {'Cherry': 2,
                   'CherryCherry': 5,
                   'CherryCherryCherry': 7,
                   'OrangeOrangeOrange': 10,
                   'OrangeOrangeBar': 10,
                   'PlumPlumPlum': 15,
                   'PlumPlumBar': 15,
                   'BellBellBell': 20,
                   'BellBellBar': 20,
                   'BarBarBar': 100}                
        
        check = 3
        done = False
        while not done and check > 0:
            
#            if check == 3:
#                key = self._wheels[0] + self._wheels[1] + self._wheels[2] 
#            elif check == 2:
#                key = self._wheels[0] + self._wheels[1]
#            else:
#                key = self._wheels[0]
            
            key = ''.join(self._wheels[:check])    
            try: 
                self._winning = winning[key]
                done = True
            except KeyError:
                self._winning = -1
                check -= 1
        self._stake += self._winning
        
        
    def display(self):
        print('{0:^10}{1:^10}{2:^10}'.format(self._wheels[0], self._wheels[1], self._wheels[2]),end='')
        print('--> You win ' + str(self._winning) if self._winning > 0  else '--> You lose', end=' ') 
        print('Cash ' + str(self._stake))
        
            
def main():
    
    sm = SlotMachine()
    done = False
    while not done:
        if sm.get_stake() > 0:
            ans = input('Press Enter to Continue and Q to quit : ')
            if ans in {'Q', 'q'}:
                done = True
            else:
                sm.play()

        else:
            try:
                ans = input('Please deposit cash : ')
                amount = int(ans)
                if amount > 0:
                    sm.deposit(amount)
                else:
                    done = True
                
            except ValueError:
                print('If you do not want to play, enter 0')

main()

        