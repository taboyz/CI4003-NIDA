# -*- coding: utf-8 -*-
"""
Created on Tue Feb 13 22:03:19 2018

@author: kronprom
"""
import forex
import mysql.connector

##  Mysql Config
conn = mysql.connector.connect(
         user='kronprom',
         password='',
         host='192.168.230.128',
         database='ci4003')
## End Mysql Config




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
    
    def get_balance(self):
        
        show_balance = ""
        balance_dict = {}

        for i in self._list_transaction:
            if i.get_currency() not in balance_dict:
                balance_dict.update({i.get_currency():i.get_amount()})
            else :
                balance_dict.update({i.get_currency():balance_dict[i.get_currency()]+i.get_amount()})
            
        print (balance_dict)
#            for key,value in sorted(balance_dict.items()):
#                print ("{} {}".format(key,value))
#         
            
            
            #   show_balance += (str(i.get_time())+" "+i.get_status()+"\t"+str(i.get_currency())+"\t"+str(i.get_amount())+"\n")

        
        return show_balance
    
    
    def get_curreny_balance(self,currency):
        
        show_balance = ""
        balance_dict = {}
        
        
        for i in self._list_transaction:
            if i.get_currency() ==  currency:
                
                if i.get_currency() not in balance_dict:
                    balance_dict.update({i.get_currency():i.get_amount()})
                else :
                    balance_dict.update({i.get_currency():balance_dict[i.get_currency()]+i.get_amount()})
            
        print (balance_dict)
#            for key,value in sorted(balance_dict.items()):
#                print ("{} {}".format(key,value))
#         
            
            
            #   show_balance += (str(i.get_time())+" "+i.get_status()+"\t"+str(i.get_currency())+"\t"+str(i.get_amount())+"\n")

        
        return show_balance
            
    
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
    print(wallet1.get_balance())
    

def deposit(wallet1,conn):
    from datetime import datetime
    transaction_now = str(datetime.now())
    print (transaction_now)
    currency = input ("Input Currency to Deposit:")
    
    
    while True:
        try :
            amount = float(input ("Input Amount:"))
        except ValueError:
            print ("Please Input Number!!")
            continue
        
        if amount < 0 :
            print ("Please Input Positive Number!!")
            continue
        else:
            break
        
    transaction1 = transaction(transaction_now,currency.upper(),amount,"deposit")
    wallet1.deposit(transaction1)
    
    
    ## insert Transaction to Database ###
    try:
        mysql_insert_to_wallet(conn,currency,amount,'deposit')
        print ("Inserted to Database")
    except:
        print ("Can't insert to Database")
        
    print (wallet1.get_transaction())
    print ("ok")
    

def withdraw(wallet1,conn):
    from datetime import datetime
    ## Show Balance
    print(wallet1.get_balance())
    
    
    transaction_now = str(datetime.now())
    print (transaction_now)
    currency = input ("Input Currency to withdraw:")
    currency = currency.upper()
    ###### show Balance ### Before Withdraw ###
    print (wallet1.get_curreny_balance(currency))
    
    while True:
        try :
            amount = float(input ("Input With draw Amount:"))
        except ValueError:
            print ("Please Input Number!!")
            continue
        
        if amount < 0 :
            print ("Please Input Positive Number!!")
            continue
        else:
            break
    
    ###### check Balance ### Before Withdraw ###
    
    
    
    
    amount = -amount
    transaction1 = transaction(transaction_now,currency.upper(),amount,"withdraw")
    wallet1.deposit(transaction1)
    
     ## insert Transaction to Database ###
    try:
        mysql_insert_to_wallet(conn,currency,amount,'withdraw')
        print ("Inserted to Database")
    except:
        print ("Can't insert to Database")
    
    
    
    
    print (wallet1.get_transaction())
    print ("withdraw --ok")

def show_transaction_history(wallet1):
    print (wallet1.get_transaction())

def show_exchange_rate():
    forex.Forex()

def mysql_insert_to_wallet(conn,currency,amount,status):
    ## Insert
    #print ("{} {} {}".format(currency,amount,status))
    
    cur1 = conn.cursor()
    query1 = ("INSERT INTO `wallet` (`tansaction_id`, `date`, `currency`, `amount`, `status`) VALUES (NULL, CURRENT_TIMESTAMP,'{0}', '{1}', '{2}');".format(currency,amount,status))
  #  query1 = ("INSERT INTO `wallet` (`tansaction_id`, `date`, `currency`, `amount`, `status`) VALUES (NULL, CURRENT_TIMESTAMP, 'USD', '500', 'deposit');")
    cur1.execute(query1)
    print ("inserted")
    # Make sure data is committed to the database
    conn.commit()
#    conn.close()

def load_wallet_from_database(wallet1,conn):
    cur = conn.cursor()
    query = ("SELECT date, currency,amount, status FROM wallet")
    cur.execute(query)
    for (date, currency, amount, status) in cur:
         #print("{}, {}, {}, {}".format(date, currency,amount,status)
         
         
         transaction_db = transaction(date,str(currency.decode('utf8')),amount,str(status.decode('utf8')))
         
         
#
         #print (transaction_db)
         #print ("TEST")
         wallet1.deposit(transaction_db)
         
         print ("Loaded..")

     
    cur.close()




def main():
    
    ##initial Wallet
    wallet1 = wallet()
    
    ##load wallet transaction to object ##
    load_wallet_from_database(wallet1,conn)
    show_menu()
    is_quit = 'No'
  
    
    
    while is_quit != "yes":
        input_option = input("Enter one of the option:")
        
        if input_option == "0":
            show_menu()
        elif input_option == "1":
            show_balance(wallet1)
        elif input_option == "2":
            deposit(wallet1,conn)
        elif input_option == "3":
            withdraw(wallet1,conn)
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
    