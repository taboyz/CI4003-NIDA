# -*- coding: utf-8 -*-
"""
Created on 

@author: kronprom
"""
def tip(amount,percent):
     return (amount * percent) / 100

    
amountin = input("amount:")
percentin = input("Percent:")
amount_1 = float(amountin)
percent_1 = float(percentin)
              
tip_amount = tip(amount_1,percent_1)
print ("tip:>",percent_1,"%   =",tip_amount)
print ( "Total paid:",tip_amount + amount_1)
