# -*- coding: utf-8 -*-
"""
Created on Tue Feb 20 13:58:53 2018

@author: kronprom
"""
import mysql.connector
conn = mysql.connector.connect(
         user='kronprom',
         password='',
         host='192.168.230.128',
         database='ci4003')

#cur = conn.cursor()

#query = ("SELECT * FROM notebook")
#
#cur.execute(query)
#
#for (id, test, test1, test2) in cur:
#  print("{}, {}, {}, {}".format(id, test.decode('utf8'),test1,test2))
#cur.close()

def mysql_insert_to_wallet(conn,currency,amount,status):
    ## Insert
    print ("{} {} {}".format(currency,amount,status))
    
    cur1 = conn.cursor()
    query1 = ("INSERT INTO `wallet` (`tansaction_id`, `date`, `currency`, `amount`, `status`) VALUES (NULL, CURRENT_TIMESTAMP,'{0}', '{1}', '{2}');".format(currency,amount,status))
  #  query1 = ("INSERT INTO `wallet` (`tansaction_id`, `date`, `currency`, `amount`, `status`) VALUES (NULL, CURRENT_TIMESTAMP, 'USD', '500', 'deposit');")
    cur1.execute(query1)
    print ("inserted")
    # Make sure data is committed to the database
    conn.commit()
    conn.close()
    
currency = "chi"
amount = 1000
status = "deposit"
mysql_insert_to_wallet(conn,currency,amount,status)    