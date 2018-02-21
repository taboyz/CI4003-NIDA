# -*- coding: utf-8 -*-
"""
Created on Tue Feb 13 22:03:19 2018

@author: kronprom
"""

class wallet:
    def __init__(self, transaction=[]):
        self._list_transaction = []
        
        
        
    def deposit(self,transaction):
#        self._list_transaction.append(transaction)
        self._list_transaction.append(transaction)
        print ("deposit")  
    def withdraw(self,transaction):
        self._list_transaction.append(transaction)
        
    def get_transaction(self):
        show_item = ""
        for i in self._list_transaction:
            show_item += (str(i.get_time())+" "+i.get_status()+"\t"+str(i.get_currency())+"\t"+str(i.get_amount())+"\n")
        return show_item
            
    
    def __str__(self):
        return "YO!"
    
class   transaction:
    def __init__(self,time,currency,amount,status):
        self._time = time
        self._currency = currency
        self._amount =amount
        self._status = status
    
    def get_time(self):
        return self._time
    
    def get_currency(self):
        return self._currency
    
    def get_amount(self):
        return self._amount
    
    def get_status(self):
        return self._status
    
    
    def __str__(self):
        return ("Hello")
    

class currency:
    def __init__(self):
        pass
    def __str__(self):
        return ("cu")


def show_menu():
    print ("0: Show Wallet menu")
    print ("1: Show Balance")
    print ("2: Deposit to Wallet")
    print ("3: Withdraw from Wallet")
    print ("4: Show transaction history")
    print ("5: Show Exchange rate from Internet")
    print ("exit: Exit Wallet")

def show_balance(wallet1):
    pass

def deposit(wallet1):
    from datetime import datetime
    transaction_now = str(datetime.now())
    print (transaction_now)
    currency = input ("Input Currency to Deposit:")
    amount = float(input ("Input Amount:"))
    transaction1 = transaction("12/12/1980 16:00:01",currency,amount,"deposit")
    wallet1.deposit(transaction1)
    
    print (wallet1.get_transaction())
    print ("ok")
    

def withdraw(wallet1):
    pass

def show_transaction_history(wallet1):
    print (wallet1.get_transaction())

def show_exchange_rate():
    pass

def main():
    
    show_menu()
    is_quit = 'No'
  
    wallet1 = wallet()
    
    while is_quit != "yes":
        input_option = input("Enter one of the option:")
        
        if input_option == "0":
            show_menu()
        elif input_option == "1":
            show_balance(wallet1)
        elif input_option == "2":
            deposit(wallet1)
        elif input_option == "3":
            withdraw(wallet1)
        elif input_option == "4":
            show_transaction_history(wallet1)
        elif input_option == "5":
            show_exchange_rate()    
        elif input_option.upper() == "EXIT":
            is_quit = "yes"
        else:
            print ("Sorry no Choice")
            print (" type '0' for help ")
        
    print ("Bood Bye!!")            

    
   
    
    
  
    
    




main()
    