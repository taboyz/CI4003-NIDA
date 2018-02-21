# -*- coding: utf-8 -*-
"""
Created on Tue Feb 20 22:43:50 2018

@author: kronprom
"""
import requests

def Forex():
    chk_symbol = []
    url_forex = 'https://api.fixer.io/latest?base=THB'
   
    response = requests.get(url_forex)

    if response.status_code == 200 :
        data_forex = response.json()
        print (type(data_forex))
        print (data_forex)
        print("Base currency  1 ",data_forex["base"])
        date_c = data_forex["date"]
        print("Date Exchange :",date_c)
        #print("Date Exchange ==> Date :",date_c[8:10],"/",date_c[5:7],"/",date_c[0:4])
        print("Currency Exchange")
        for key, val in data_forex["rates"].items():
            chk_symbol.append(key)
            print( key, ':', val)

        try:
            sym_convert = str(input("Please choose symbol for exchange :"))
            while sym_convert.upper() not in chk_symbol:
                print("Symbol",sym_convert,"not in list.")
                print("Please try again !!!")
                print("Base currency :", data_forex["base"])
                print("Date Exchange :", date_c)
                print("Currency Exchange")
                for key, val in data_forex["rates"].items():
                    chk_symbol.append(key)
                    print(key, ':', val)

                sym_convert = str(input("Please choose symbol for exchange :"))
                #end while loop


            if sym_convert.upper()  in chk_symbol:
                print(data_forex["rates"][sym_convert.upper()])
                return data_forex["rates"][sym_convert.upper()]
            else :
                print("Error in list!!!")



        except :
            print("Program error!!!")
    else :
        print("Can't connnect to website or connection error !!!")

def main():

    a=Forex()
    print("Forex is",a)

