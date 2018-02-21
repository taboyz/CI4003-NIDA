# -*- coding: utf-8 -*-
"""
Created on Fri Feb  9 23:50:57 2018

@author: kronprom

Notes are short memos stored in a notebook. 
Each note should record the day it was written and can have tags added for easy querying. 
It should be possible to modify notes. We also need to be able to search for notes. 
All of these things should be done from the command line.
"""
class note:
    def __init__(self, date,content,tag):
        self._date = date
        self._content = content
        self._tag = tag
    
    def get_date(self):
        return self._date
    
    def get_content(self):
        return self._content
    
    def get_tag(self):
        return self._tag
    
    def set_content(self, content):
        self._content = content
    
    def set_tag(self, tag):
        self._tag = tag
    
    def __str__(self):
        return "Hello"


class notebook:
    def __init__(self,list_of_note=[]):
        self._list_of_note = list_of_note
        
    def add_note(self,list_of_note):
        self._list_of_note.append(list_of_note)
    
    
        
        
    def __str__(self):
        show_note = ""
        for i in self._list_of_note:
            show_note += i.get_date() + " "+i.get_tag()+"\n"
        return show_note 

def write_note(notebook1):
    input_date = input("Enter Date:")
    input_tag =  input("Enter tag:")
    input_content = input("Enter content")
    notebook1 = notebook()
    note1 = note(input_date,input_tag,input_content)
    notebook1.add_note(note1)
    
    outfile = open("notebook.txt","a")
    outfile.write("{},{},{}\n".format(input_date,input_tag,input_content))
    outfile.close()
 
def show_all_note(notebook1):
    print (notebook1)
               
    
    
    
def main():
    notebook1 = notebook()
    
    prompt = "NO"
    while prompt.upper() != "EXIT":
        print ("show all note (showall) / add note (add)/ search tag (tag)")
        input_command = input("Enter command:")
        if input_command.upper() == "ADD":
            print ("Choose ",input_command.upper())
            write_note(notebook1)
        
        elif input_command.upper() == "SHOWALL":
            print ("Choose ",input_command.upper())
            show_all_note(notebook1)
            
            
        elif input_command.upper() == "EXIT":
            print ("Bye!! See you again")
            prompt = "EXIT"
            
    
    print (notebook1)

    
        
main()    