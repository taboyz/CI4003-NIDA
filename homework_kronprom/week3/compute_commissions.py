

# -*- coding: utf-8 -*-
"""
Created on Wed Jan 24 15:24:40 2018

@author: kronprom
"""

def compute_commission(sales_amount):
    print ("Sales Amount:",sales_amount)
    print ("="*30)
    total_commission = 0
    
    while sales_amount > 0 :
        if sales_amount > 1000000.01:
            commission = (sales_amount - 1000000)*(12/100)
            print (sales_amount - 1000000,"com 12% => ", commission)
            total_commission = total_commission + commission
            sales_amount = 1000000
            continue
        elif sales_amount >= 500000.01 and sales_amount <= 1000000:
            commission = (sales_amount - 500000)*(10/100)
            print (sales_amount - 500000,"com 10% => ", commission)
            total_commission = total_commission + commission
            sales_amount = 500000
            continue
        elif sales_amount >= 100000.01 and sales_amount <= 500000:
            commission = (sales_amount - 100000)*(8/100)
            print (sales_amount - 100000,"com 8% => ", commission)
            total_commission = total_commission + commission
            sales_amount = 100000
            continue
        elif sales_amount <= 100000 and sales_amount > 0:
            commission = sales_amount*(6/100)
            print (sales_amount,"com 6% => ", commission)
            total_commission = total_commission + commission
            sales_amount = 0
            continue
    print ("-"*30)    
    print ("Commission:",total_commission)
    print ("-"*30,"\n")   
    return total_commission
        
    
#sale_amount_input = float(input("Amount:"))
#total_commission_1 = compute_commission(sale_amount_input)    

n = 100000
while n <= 1000000:
    compute_commission(n)
    n = n+100000
    
