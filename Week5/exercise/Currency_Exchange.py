# -*- coding: utf-8 -*-
"""
Created on Mon Feb 12 20:03:29 2018

@author: kronprom
"""
def list_country():
    infile = open("Exchrate.txt","r")
    exchange_list = [tuple(line.rstrip().split(",")) for line in infile]
    infile.close()

    for index,i in enumerate(exchange_list):
        print ("{}".format(exchange_list[index][0]))
        
def show_currency(country):
    infile = open("Exchrate.txt","r")
    exchange_list = [tuple(line.rstrip().split(",")) for line in infile]
    infile.close()
    for index,i in enumerate(exchange_list):
        if country.upper() == exchange_list[index][0].upper():
            print ("Currency :",exchange_list[index][1])
            print ("Exchange rate:",exchange_list[index][2])
            
   

def main():
    list_country()
    input_currency = input("Enter the name of a country:")
    show_currency(input_currency)
    

    
main()
