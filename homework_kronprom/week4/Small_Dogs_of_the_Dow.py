# -*- coding: utf-8 -*-
"""
Created on 

@author: kronprom
"""

# take second element for sort
def takeThird(elem):
    return elem[2]

infile = open('DOW.txt','r')
dow_list = [  line.rstrip().split(",")   for line in infile]
infile.close()
price_end_list = [[dow_list[index][0],dow_list[index][1],float(dow_list[index][5])]for index,item in enumerate(dow_list)]
price_end_list.sort(key=takeThird)
print ("{:30} {:<20} {:<20}".format("Company","Symbol","Price on 12/31/2013"))
for i in range (5):
    print ("{:30}{:<20}${:<20}".format(price_end_list[i][0],price_end_list[i][1],price_end_list[i][2]))