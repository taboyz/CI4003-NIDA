# -*- coding: utf-8 -*-
"""
Created on Fri Feb  9 19:36:04 2018

@author: kronprom
"""

class Purchase:
    def __init__(self, description, price, quantity):
        self._description = description
        self._price = price
        self._quantity = quantity
    
    def get_description(self):
        return self._description
    
    def get_price(self):
        return self._price
    
    def get_quantity(self):
        return self._quantity
    
    
    def set_description(self, description):
        self._description =  description

    def set_price(self, price):
        self._price = price
  
    def set_quantity(self, quantity):
        self._quantity =  quantity
        
    def __str__(self):
        return self._description + " " + str(self._price) +" "+ str(self._quantity)
    

class Cart:
    def __init__(self, list_of_purchase_item=[]):
        self._listitem = list_of_purchase_item
        
    def add_item(self, list_of_purchase_item):
        self._listitem.append(list_of_purchase_item)
        
    def get_items(self):
        show_item = ""
        for i in self._listitem:
            show_item += (i.get_description()+"\t$"+str(i.get_price())+"\t"+str(i.get_quantity())+"\n")
        return show_item
    
    
    
     
    def calculate_total(self):
        total = 0
        for x in self._listitem:
            each_artical = x.get_price() * x.get_quantity()
            total += each_artical
        return total
    
    def __str__(self):
        return self.get_items()
        
            
        
     
        
        
        
 
    
def print_receipt(cart):
    print ("ARTICLE\t PRICE\t Quantity" )
    print (cart.get_items())
    print("TOTAL COST: ${0:,.2f}".format(cart.calculate_total()))
    
def main():
    
    ## create object Cart
    cart1 = Cart()
    
    ## Check Shooping
    continue_shopping = 'Y'
    while continue_shopping != 'N':
        description = input("Enter description of article:")
        price = float(input("Enter price of article:"))
        quantity = int(input("Enter quantity of article:"))
        ## Create object Purchage
        purchase1 = Purchase(description ,price, quantity)
        
        ## Add  Obect Purchase to Cart
        cart1.add_item(purchase1)
        
        prompt = input("Do you want to enter more article (Y/N)?")
        while str.upper(prompt) not in ('Y','N'):
            print ("Please type Y or N  Only!!!!")
            prompt = input("Do you want to enter more article (Y/N)?")
        
        
        continue_shopping = str.upper(prompt)
        
#    print_receipt(cart1)sh
    #print(purchase1)
    #print(cart1.get_items())
    print_receipt(cart1)
   
    
main()

    
    