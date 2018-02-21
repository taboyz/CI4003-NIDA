# -*- coding: utf-8 -*-
"""
Created on Thu Feb  8 17:27:14 2018

@author: kronprom
"""

class Stock:
    def __init__(self,name,symbol,previous_price,current_price):
        self._name  = name
        self._symbol = symbol
        self._prvious_price = previous_price
        self._current_price = current_price
        
    def get_name(self):
        return self._name
    
    def get_symbol(self):
        return self._symbol
    
    def get_previous_price(self):
        return self._prvious_price
    
    def get_current_price(self):
        return self._current_price
    
    def set_name(self,name):
        self._name = name
        
    def set_symbol(self, symbol):
        self._symbol = symbol
    
    def set_previous_price(self, previous_price):
        self._prvious_price = previous_price
    
    def get_change_percent(self):
        percentage_change =  (self._current_price - self._prvious_price) / self._prvious_price      
        return str(percentage_change)+"%"
    
    def __str__(self):
        
        return  "Current Values is " + self._name 
    
def main():
    stock1 = Stock('boyz','bo',500,400)
    print (stock1)
    print (stock1.get_change_percent())
    
    input_name = input("Enter Stock name:")
    input_symbol = input("Enter Stock Symbol:")
    input_previous_price = float(input("Enter previous price:"))
    input_current_price = float(input("Enter cuurent price:"))
    
    stock2 = Stock(input_name,input_symbol,input_previous_price,input_current_price)
    print (stock2.get_name())
    print (stock2.get_symbol())
    print (stock2.get_previous_price())
    print (stock2.get_current_price())
    print ("Percentage of change = ",stock2.get_change_percent())
    
    

  
    
main()

    
    
    
    
        
        
