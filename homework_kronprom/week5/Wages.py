# -*- coding: utf-8 -*-
"""
Created on Thu Feb  8 19:27:32 2018

@author: kronprom
"""

class Wages:
    def __init__(self, name="", hours=0.0, wage=0.0):
        self._name = name
        self._hour = hours
        self.wage = wage
    
    def get_name(self):
        return self._name
        
    def set_name(self, name):
        self._name = name
        
    def set_hours(self, hours):
        self._hours = hours
        
    def set_wage(self, wage):
        self._wage = wage
    
    def payment(self):
        if self._hours <= 40:
            wage = self._hours * self._wage
        else:
            wage = (self._wage * 40)+((self._hours - 40) * self._wage * 1.5)
        return str(wage)
    
    def __str__(self):
        return self._name
    
    
input_name = input("Enter person's name:")
input_hours = int(input("Enter number of hours worked:"))
input_wage = float(input("Enter hourly wage:"))

wage1 = Wages()
wage1.set_name(input_name)
wage1.set_hours(input_hours)
wage1.set_wage(input_wage)

print ("Pay for {0} : ${1:,.2f}".format(wage1.get_name(),float(wage1.payment())))



    
    
    