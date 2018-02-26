# -*- coding: utf-8 -*-
"""
Created on Mon Feb 12 23:39:12 2018

@author: kronprom
"""

def sumproduct(x):
    total_amount = 0
    for i, value in enumerate(x):
        total_amount += float(x[i][1]) * float(x[i][2])
            
    return total_amount

def display_items(x):
    for i, value in enumerate(x):
        line_total = float(x[i][1]) * float(x[i][2])
        print ("{0:<30}\t{1:>20}\t{2:>10,.2f}\t{3:,.2f}".format(x[i][0],x[i][1],float(x[i][2]),line_total))        

def display_invoice(x):
    print ("-" * 80)
    print ("{0:<30}\t{1:>20}\t{2:>10}\t{3:>}".format("Description","QTY","Unit Price","Line Total"))
    print ("-" * 80)
    display_items(x)
    print ("-" * 80)
    print ("{0:<30}\t{1:>20}\t{2:>10}\t{3:>10,.2f}".format("Subtotal:","","",sumproduct(x)))
    tax = sumproduct(x)* 7/100
    print ("{0:<30}\t{1:>20}\t{2:>10}\t{3:>10,.2f}".format("Tax","","7.00%",tax))
    total = tax + sumproduct(x)
    print ("{0:<30}\t{1:>20}\t{2:>10}\t{3:>10,.2f}".format("Total","","",total))
    

def main():
    infile = open("Order.txt","r")
    list_order = [line.rstrip().split(",") for line in infile]
    infile.close()
    
    #print (list_order)
    display_invoice(list_order)

    
    
    
    
    
main()
    
    
    
    
    