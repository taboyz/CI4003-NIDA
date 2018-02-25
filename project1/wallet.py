# -*- coding: utf-8 -*-
"""
Created on Tue Feb 13 22:03:19 2018

@author: kronprom
"""
#import forex
import mysql.connector

##  Mysql Config
conn = mysql.connector.connect(
         user='kronprom',
         password='',
         host='192.168.230.128',
         database='ci4003')
## End Mysql Config

class currency:
    def __init__(self,code,name,currency_type):
        self._code = code
        self._name = name
        self._currency_type = currency_type

    def get_code(self):
        return self._code
    
    def get_name(self):
        return self._name
    
    def get_currency_type(self):
        return self._currency_type
    
    def __str__(self):
        return "Loaded"
    
class currency_in_wallet:
    def __init__(self,currency_list =[]):
        self._currency_list = []
        
    def append_currency(self,currency):
        self._currency_list.append(currency)
        
    def show_curency(self):
        
        print ("{0:10}{1:30}{2:10}".format("CODE","NAME","TYPE"))
        for i in self._currency_list:
            print ("{0:10}{1:30}{2:10}".format(str(i.get_code()),str(i.get_name()),str(i.get_currency_type())))
            #all_currency += (str(i.get_code())+"\t"+str(i.get_name())+"\t\t\t"+str(i.get_currency_type())+"\n")
        
        return "OK"
    
    def get_curency_code_in_wallet(self):
        current_code_list = [str(i.get_code()) for i in self._currency_list]
        #print (current_code_list)
        return current_code_list
        
    def __str__(self):
        return "Hello"      


class wallet:
    def __init__(self, transaction=[]):
        self._list_transaction = []
        
        
        
    def deposit(self,transaction):
#        self._list_transaction.append(transaction)
        self._list_transaction.append(transaction)
        
    def withdraw(self,transaction):
        self._list_transaction.append(transaction)
        
    def get_transaction(self):
        show_item = ""
        for i in self._list_transaction:
            show_item += (str(i.get_time())+" "+i.get_status()+"\t"+str(i.get_currency())+"\t"+str(i.get_amount())+"\n")
        return show_item
    
    def get_balance(self):
        

        balance_dict = {}

        for i in self._list_transaction:
            if i.get_currency() not in balance_dict:
                balance_dict.update({i.get_currency():i.get_amount()})
            else :
                balance_dict.update({i.get_currency():balance_dict[i.get_currency()]+i.get_amount()})                
        return balance_dict

    def show_balance(self):
        

        balance_dict = {}

        for i in self._list_transaction:
            if i.get_currency() not in balance_dict:
                balance_dict.update({i.get_currency():i.get_amount()})
            else :
                balance_dict.update({i.get_currency():balance_dict[i.get_currency()]+i.get_amount()})
        
        print ("="*50)
        print ("Current Balance in Wallet")
        print ("="*50)
        for key,value in sorted(balance_dict.items()):
                print ("{} {}".format(key,value))
        
        return balance_dict    
    
    
    def get_curreny_balance(self,currency):
        

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

        
        return balance_dict
            
  
    
    def __str__(self):
        return "YO!"
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
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
    




def show_menu():
    print ("="*40)
    print ("Wallet Menu\n")
    print ("Please Select :")
    print ("type '0': Show Wallet menu")
    print ("type '1': Show Wallet Balance")
    print ("type '2': Deposit to Wallet")
    print ("type '3': Withdraw from Wallet")
    print ("type '4': Show transaction history")
    print ("type '5': Show Exchange rate from Internet")
    print ("type '6': Covert Balance Currency in Wallet")
    print ("type 'Exit': Exit Wallet")
    print ("="*40)
    
def show_balance(wallet1):
    wallet1.show_balance()
    
    

def deposit(wallet1,conn,currency1):
    from datetime import datetime
    transaction_now = str(datetime.now())
    print (transaction_now)
    
    
    while True:
        currency1.show_curency()
        c = currency1.get_curency_code_in_wallet()
        print (c)
        currency = input ("Input Currency CODE from list above to Deposit:")
        currency = currency.upper()
       
        
        if currency not in c:
            print (" Your Currency Code not in list")
            continue
            
        else:
            print ("{} found".format(currency))
            break
            
    
    #####END HERE####
    
    while True:
        try :
            amount = float(input ("Input Deposit Amount:"))
        except ValueError:
            print ("Please Input Number!!")
            continue
        
        if amount <= 0 :
            print ("Please Input Amount more than '0'!!")
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
    print (" {} {} is deposited to your wallet".format(currency,amount))
    

def withdraw(wallet1,conn,currency1):
    from datetime import datetime
    ## Show Balance
    print(wallet1.show_balance())
    
    ##date##    
    transaction_now = str(datetime.now())
    print (transaction_now)
    
    ########## HERE
    while True:
        w =wallet1.show_balance()
        #print (w)
        currency = input ("Input Currency CODE from list above to Withdraw:")
        currency = currency.upper()

        if currency not in w:
            print (" Your Currency Code not in list")
            continue
            
        else:
            print ("{} found".format(currency))
            break
 
   
    bw = wallet1.get_curreny_balance(currency)
    #print (type(bw))
    while True:
        try :
            amount = float(input ("Input Withdraw Amount:"))
        except ValueError:
            print ("Please Input Number!!")
            continue
        
        if amount <= 0 :
            print ("Please withdraw amount more than '0'!!")
            continue
        else:
            ## check Balance
            
            if amount > bw[currency]:
                print ("Wallet Balance of {0} is not enough to withdraw\n you have only:  {0} {1} ".format(currency,bw[currency]))
                continue
            else:            
                break
    ######
    c = currency1.get_curency_code_in_wallet()
    #print (c)
    exc = ",".join(c)
    #print(exc)
    convert_currency(currency,exc,amount)
    #######

    amount = -amount
    transaction1 = transaction(transaction_now,currency.upper(),amount,"withdraw")
    wallet1.deposit(transaction1)
    
     ## insert Transaction to Database ###
    try:
        mysql_insert_to_wallet(conn,currency,amount,'withdraw')
        print ("Inserted to Database")
    except:
        print ("Can't insert to Database")
    
    #print (wallet1.get_transaction())
    print (" {} {} is withdraw from your wallet".format(currency,amount))   

def show_transaction_history(wallet1):
    print (wallet1.get_transaction())

#def show_exchange_rate():
#    pass
#    #forex.Forex()

def mysql_insert_to_wallet(conn,currency,amount,status):
    ## Insert
    #print ("{} {} {}".format(currency,amount,status))
    
    cur1 = conn.cursor()
    query1 = ("INSERT INTO `wallet` (`tansaction_id`, `date`, `currency`, `amount`, `status`) VALUES (NULL, CURRENT_TIMESTAMP,'{0}', '{1}', '{2}');".format(currency,amount,status))
  #  query1 = ("INSERT INTO `wallet` (`tansaction_id`, `date`, `currency`, `amount`, `status`) VALUES (NULL, CURRENT_TIMESTAMP, 'USD', '500', 'deposit');")
    cur1.execute(query1)
   # print ("inserted")
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


def load_currency_from_database(currency1,conn):
    cur = conn.cursor()
    query = ("SELECT code, name,currency_type FROM currency WHERE enable ='Y'")
    cur.execute(query)
    for (code, name, currency_type) in cur:
         #print("{}, {}, {}, {}".format(date, currency,amount,status)
        currency_db = currency(str(code.decode('utf8')),str(name.decode('utf8')),str(currency_type.decode('utf8'))    )
                 
#
#        print (currency_db)
         #print ("TEST")
        currency1.append_currency(currency_db)
        print ("Loaded.. currency",str(code.decode('utf8')))

    print ("loaded.currency.Completed") 
    cur.close()
    
    
    

    
    
def convert_currency(base,convert_to,amount):
    import requests
    
    ##https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD
    url_exchange = 'https://min-api.cryptocompare.com/data/price?fsym={0}&tsyms={1}'.format(base,convert_to)
    response = requests.get(url_exchange)

    try:
        if response.status_code == 200 :
            #data_cryptocompare = response.json(parse_float=decimal.Decimal)
            data_cryptocompare = response.json(parse_float=float)
            print(" Wallet Base currency:  {0} \n Withdraw amount = {1}".format(base,amount))
            for key, val in data_cryptocompare.items():
                print(" From :{3:} to {0:} rate {1:>10,}\t   result = {0:} {2:,f}".format(key,val,amount*val,base))
            
            print ('='*80)
            print ("Souce Exchange rate from :\n{}".format(url_exchange))
            print (" * Caching	10 seconds ")
            print ('='*80)
        
        else:
            print ("Error Connect to API : {} ".format(response.status_code))
    except :
        print ("Error Connect to API")

def convert_currency_from_api(base,convert_to,amount):
    import requests
    
    ##https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD
    url_exchange = 'https://min-api.cryptocompare.com/data/price?fsym={0}&tsyms={1}'.format(base,convert_to)
    response = requests.get(url_exchange)

    try:
        if response.status_code == 200 :
            #data_cryptocompare = response.json(parse_float=decimal.Decimal)
            data_cryptocompare = response.json(parse_float=float)
           # print(" Wallet Base currency:  {0} \n Withdraw amount = {1}".format(base,amount))
            for key, val in data_cryptocompare.items():
                result = amount*val
            
           
        
        else:
            print ("Error Connect to API : {} ".format(response.status_code))
    except :
        print ("Error Connect to API")
        
    return [val,result]


def convert_currency_in_wallet(wallet1,currency1):
    
        
    while True:
        currency1.show_curency()
        c = currency1.get_curency_code_in_wallet()
        #print (c)
        currency = input ("Input Currency CODE from list above your Convert Wallet to:")
        currency = currency.upper()
       
        if currency not in c:
            print (" Your Currency Code not in list")
            continue
            
        else:
            print ("{} found".format(currency))
            break
        
    print ('='*80)    
    print ("Converting Wallet to {} ".format(currency)  )
    print ('='*80)
    total_convert = 0
    for key,value in sorted(wallet1.get_balance().items()):
        
        apiconvert = convert_currency_from_api(key,currency,value)
        print ("from {0} {1:15,f} exchange rate: {2:15,f} = {4} {3:20,f}".format(key,value,apiconvert[0],apiconvert[1],currency) )
        total_convert += apiconvert[1]
    print ("\nTotal amount {0} in wallet :{0} {1:,.2f} ".format(currency,total_convert))
        
    print ('='*80)
    print ("Souce Exchange rate from https://min-api.cryptocompare.com/data/ \n")
    print (" * Caching	10 seconds ")
    print ('='*80)
        
    
    
def show_exchange_rate(wallet1,currency1):
    
        
    while True:
        currency1.show_curency()
        c = currency1.get_curency_code_in_wallet()
        #print (c)
        currency = input ("Input Currency CODE from list above to show Exchange rate from API:")
        currency = currency.upper()
       
        if currency not in c:
            print (" Your Currency Code not in list")
            continue
            
        else:
            print ("{} found".format(currency))
            break
        
    print ('='*80)    
    print (" Base Currency : {} ".format(currency)  )
    print ('='*80)
 
    for code in c:
        
        apiconvert = convert_currency_from_api(currency,code,1)
        print ("{0:<10} exchange rate: {2:} {1:15,f} ".format(code,apiconvert[0],currency) )
  ##here
        
    print ('='*80)
    print ("Souce Exchange rate from https://min-api.cryptocompare.com/data/ \n")
    print (" * Caching	10 seconds ")
    print ('='*80)
        
        

def main():
    
    ##initial Wallet
    wallet1 = wallet()
    ##load wallet transaction to object ##
    load_wallet_from_database(wallet1,conn)
    
    ##initial Wallet currecncy
    currency1 = currency_in_wallet()
    ##load enble cuuenct to object
    load_currency_from_database(currency1,conn)
    
    
    show_menu()
    is_quit = 'No'
    
    
    while is_quit != "yes":
        input_option = input("Enter one of the option  ['0' for menu]:")
        
        if input_option == "0":
            show_menu()
        elif input_option == "1":
            show_balance(wallet1)
        elif input_option == "2":
            deposit(wallet1,conn,currency1)
        elif input_option == "3":
            withdraw(wallet1,conn,currency1)
        elif input_option == "4":
            show_transaction_history(wallet1)
        elif input_option == "5":
            show_exchange_rate(wallet1,currency1)   
        elif input_option == "6":
            convert_currency_in_wallet(wallet1,currency1) 
        elif input_option.upper() == "EXIT":
            is_quit = "yes"
        else:
            print ("Sorry no Choice")
            print (" type '0' for help ")
        
    print ("Bood Bye!!")            

    
   
    
    
  
    
    




main()
    