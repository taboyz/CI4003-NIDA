# -*- coding: utf-8 -*-
"""
Created on Mon Feb 26 16:09:17 2018

@author: kronprom
"""

##  Open File 
infile = open("DOW.TXT",'r')
## read line to list
dow_list = [(line.rstrip().split(",")) for line in  infile]
infile.close()
#print (dow_list)
percentage_change_list = [[dow_list[index][0],round(((float(dow_list[index][5])-float(dow_list[index][4])))/
                            float(dow_list[index][4])*100, 2)] for index,item  in enumerate(dow_list)]
#print (percentage_change_list)

print ("The Best performing Stock:",str(max(percentage_change_list, key = lambda x: x[1])[0])," ",str(max(percentage_change_list, key = lambda x: x[1])[1]),"%")

print ("The Worst performing Stock:",str(min(percentage_change_list,key = lambda x: x[1])[0])," ",str(min(percentage_change_list, key = lambda x: x[1])[1]),"%")
  
    
