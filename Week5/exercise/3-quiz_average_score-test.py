# -*- coding: utf-8 -*-
"""
Created on Thu Feb  8 20:27:14 2018

@author: kronprom
"""


score = input("Enter score:")
#score = "4,1,5,2,1,1,1,1,3,4"
print (score)
list_score = score.split(",")
list_score = [int(i) for i in list_score]
print (list_score)
print (min(list_score))

#list_score.remove(min(list_score))
lowest_value = min(list_score)
#for index,value in enumerate(list_score):
#    print (index,"==>",value)
#    if value == lowest_value:
#       list_score.pop(index)
#       print ("Remove",index,"=>",value,)

while lowest_value in list_score:
    list_score.remove(lowest_value)
    
print (sum(list_score))
        
