# -*- coding: utf-8 -*-
"""
Created on 

@author: kronprom
"""

# take second element for sort
def takeThird(elem):
    return elem[2]

##  Open File 
infile = open("DOW.TXT",'r')
## read line to list
dow_list = [(line.rstrip().split(",")) for line in  infile]
infile.close()
#print (dow_list)

yield_list = [[dow_list[index][0],dow_list[index][1],round(float(dow_list[index][7])
            /float(dow_list[index][5])*100,2)] for index,item  in enumerate(dow_list)]  
#print (yield_list)


# sort list with Third key and reverse MAX
yield_list.sort(key=takeThird,reverse=True)


print ("{:35} {:20} {:1} ".format("Company","Symbol","Yield"))
for i in range(10):
    #print (yield_list[i][0],"\t\t",yield_list[i][1],"\t",yield_list[i][2])
    print ("{:35} {:20} {:1}% ".format(yield_list[i][0],yield_list[i][1],yield_list[i][2]))