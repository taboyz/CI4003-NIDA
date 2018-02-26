# -*- coding: utf-8 -*-
"""
Created on Mon Feb 26 15:56:50 2018

@author: kronprom
"""

def DisplayStock(stock_symbol):

    a = [item for item in dow_list if stock_symbol.upper() in item[:][1]]
    #print (a)
    print ("Company:", a[0][0])
    print ("Industry:",a[0][3])
    print ("Enchange:",a[0][2])
    print ('Growth in 2013:{:5.2f}%'.format((float(a[0][5]) - float(a[0][4]))/float(a[0][4])*100))
    print ("Price/Earnings ratio in 2013:  {:5.2f}".format(float(a[0][5])/float(a[0][6])))
    
infile = open("DOW.TXT",'r')
#dow_list = [(line.rstrip()) for line in  infile]
dow_list = [tuple(line.rstrip().split(",")) for line in  infile]
infile.close()


print ("Symbol for the Thirty DOW Stock")
i = 0
dow_list_symbol = []
while  i < len(dow_list) :
    print (dow_list[i][1],end="\t ")
    dow_list_symbol.append(dow_list[i][1])
    i += 1
    if i % 10 == 0:
        print("\n")

while True:
   input_stock = input("\nEnter Stock Symbol:")
   if input_stock.upper() not in dow_list_symbol:
       print ("Symbol not Found!!")
       continue
   else:
       break

DisplayStock(input_stock)