# -*- coding: utf-8 -*-
"""
Created on Wed Feb 21 11:46:36 2018

@author: kronprom
Handling Using Input
"""
while True:
    try:
        input_file = input("Enter a Fileanme:")
        infile = open(input_file,"r")
        
        break
    
    except FileNotFoundError:
        print ("File {} does not exist. Try again")
        continue
    

  
list_word =  [line.strip()  for line in infile]
infile.close()

print (type(list_word))
word = "".join(list_word)
#print (res)

count_dic = {}
## Count character to dictionary
for i in word:
#    print (i)
    i = i.lower()
    if i not in count_dic:
        count_dic.update({i:1})
    else:
        count_dic.update({i:count_dic[i]+1})

for key,value in sorted(count_dic.items()):
    if  key.isalpha(): ## IS alphabet
        print ("{} appaers {} times".format(key,value)) 