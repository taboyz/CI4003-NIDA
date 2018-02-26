# -*- coding: utf-8 -*-
"""
Created on Mon Feb 26 17:54:47 2018

@author: kronprom
"""
class Stock:
    def __init__(self, name ,symbol, previous_price, current_price):
        self._name = name
        self._symbol =symbol
        self._previous_price = previous_price
        self._current_price = current_price
        
    def set_name(self,name):
        self._name = name

    def set_symbol(self,symbol):
        self._symbol =symbol
        
    def set_previous_price(self, previuos_price):
        self._previous_price = previuos_price
        
    def set_current_price(self,current_price):
        self._current_price = current_price
        
    def get_name(self):
        return self._name
    
    def get_symbol(self):
        return self._symbol
    
    def get_previous_price(self):
        return self._previous_price
    
    def get_current_price(self):
        return self.current_price
    
    def get_change_percent(self):
        percent_change = ((self._current_price - self._previous_price)/self._previous_price)* 100
        return str("{0:.2f} %".format(percent_change))
    
    def __str__(self):
        return "{0:}{1}{2}{3}".format(self._name,self._symbol,self._previous_price,self._current_price)
    


input_name = input("Enter Stock name:")
input_symbol = input("Enter Stock Symbol:")
input_previous_price = float(input("Enter Privious price:"))
input_current_price = float(input("Enter current price:"))
stock1 = Stock(input_name, input_symbol, input_previous_price, input_current_price)
print ("percentage change: {} ".format(stock1.get_change_percent()))    

    
        
        
                
        
