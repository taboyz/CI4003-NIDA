# -*- coding: utf-8 -*-
"""
Created on Tue Feb 20 16:46:55 2018

@author: kronprom
"""

import pickle

#def write_file(filename, data):
#    outfile = open(filename, 'wb')
#    pickle.dump(data, outfile)
#    outfile.close()

def read_file(filename):
    infile = open(filename, 'rb')
    data = pickle.load(infile)
    infile.close()
    return data


def show_menu():
    print ("1: Display bachelor degrees conferred.")
    print ("2: Display percentage change.")
    print ("3: Display histrogram.")
    print ("4: Quit")


def option1(data1):
    print ("Bachelor degree conferred in certain fields.\n")
   # print (type(data1))
   
    print ("{0:40}\t {1:15} {2:15}".format("Filed of Study","1981","2010"))

    for key,value in sorted(data1.items()): ## Sorted Key
        print ("{0:40} {1:15,.0f} {2:15,.0f}".format(key,value[0],value[1])  )
        #print (type(value))
    print ("end option1")

def option2(data1):
    print ("Percentage change in Bachelor degree conferred \n")
    sorted_percent_dict = {}
    print ("{0:40} {1:15}".format("Filed of Study","% Change (1981-2010)"))
    for key,value in data1.items():
        percentage_change = ((value[1]-value[0]) /value[0])*100
        sorted_percent_dict.update({key:percentage_change})
    
   # print (sorted_percent_dict)        
    #Sort#
    for value in sorted(sorted_percent_dict , key=sorted_percent_dict.__getitem__,reverse =True):
         print ("{0:40} {1:15,.1f}%".format(value,sorted_percent_dict[value]))
    th
        
    print ("end option2")

def option3(data1):
    histogram_dict = {}
    print ("Bachelor degree conferred in 2010 in certain fields\n")
    for key,value in data1.items():
        histogram_dict.update({key:value[1]})
    #print (histogram_dict)
    for value in sorted(histogram_dict, key=histogram_dict.__getitem__):
        star = round(histogram_dict[value] / 10000)
        #print (star)
        print ("{0:>30} {1:} {2:,.0f}".format(value,"*"*star,histogram_dict[value]))
    
    
def main():
    show_menu()
    is_quit = 'No'
    ## read Data
    data1 = read_file('DegreesDict.dat')
    #print(data1)
    #print (type(data1))
    ## Option
    while is_quit != "yes":
        input_option = input("Enter one of the option:")
        if input_option == "1":
            option1(data1)
        elif input_option == "2":
            option2(data1)
        elif input_option == "3":
            option3(data1)
        elif input_option == "4":
            is_quit = "yes"
        
    print ("Bood Bye!!")            


main()
