# -*- coding: utf-8 -*-
"""
Created on Mon Feb 26 17:54:46 2018

@author: kronprom
"""
import pickle

class Note:
    def __init__(self, noteid,day, tag, content):
        self._noteid = noteid
        self._day = day
        self._tag = tag
        self._content = content
        
    def get_noteid(self):
        return self._noteid
    
    def get_day(self):
        return self._day
    
    def get_tag(self):
        return self._tag
    
    def get_content(self):
        return self._content
    
    def set_noteid(self,noteid):
        self._noteid = noteid

    def set_day(self,day):
        self._day = day
    
    def set_tag(self,tag):
        self._tag = tag
        
    def set_content(self,content):
        self._content = content
        
    
    
    def __str__(self):
        return "{0}{1}{2}{3}".format(self._noteid,self._day, self._tag, self._content)
    
    
class Notebook:
    def __init__(self, note_list=[]):
        self._note_list = note_list
        
    def add_note(self, note_list):
        self._note_list.append(note_list)
        
    def modify_note(self, noteid_to_modify,day,tag,content):
        found = ''
        for i in self._note_list:
            noteid = i.get_noteid()
            #print (content)
            if noteid_to_modify == noteid:
                i.set_day(day)
                i.set_tag(tag)
                i.set_content(content)
                
                
                
                
                print ("{0:16}\t {1:10}\t  {2:10}\t {3}\t".format(i.get_noteid(),i.get_day(),i.get_tag(),i.get_content()))
                found = noteid
                
        return found
        
         
    
    def show_note(self):
        print ("{0:16}{1:15}{2:10}{3:}".format('NoteID','Day','TAG','Content'))
       
        for i in self._note_list:
            print ("{0:16}{1:15}{2:10}{3}".format(i.get_noteid(),i.get_day(),i.get_tag(),i.get_content()))
            
    def show_tag(self):
        tag_list = []
        for i in self._note_list:
            if i.get_tag() not in tag_list:
                tag_list.append(i.get_tag())
                print (i.get_tag())
    
    
    def search_noteid(self,search_word):
        found = ''
        for i in self._note_list:
            noteid = i.get_noteid()
            #print (content)
            if search_word == noteid:
                print ("{0:16}\t {1:10}\t  {2:10}\t {3}\t".format(i.get_noteid(),i.get_day(),i.get_tag(),i.get_content()))
                found = noteid
                
        return found
    
    def search_note(self,search_word):
      
        for i in self._note_list:
            content = i.get_content()
            #print (content)
            if search_word in content:
                print ("{0:16}\t {1:10}\t  {2:10}\t {3}\t".format(i.get_noteid(),i.get_day(),i.get_tag(),i.get_content()))
                
    def search_tag(self,search_word):
      
        for i in self._note_list:
            tag = i.get_tag()
            #print (tag)
            if search_word in tag:
                 print ("{0}\t {1}\t  {2}\t {3}\t".format(i.get_noteid(),i.get_day(),i.get_tag(),i.get_content()))
            
            
def showmenu():
    
        print (" Menu :")    
        print (" 0  show menu")
        print (" 1 Add note")
        print (" 2 Show All note")
        print (" 3 Show All TAG")   
        print (" 4 Search Note Content")             
        print (" 5 Search TAG")     
        print (" 6 Modify Note")         
        print (" 99 Save and Exit")
        
        
def add_note(notebook1):
    input_date = input("Enter Day: (dd/mm/yyyy):")
    input_content = input("Enter note content:")
    input_tag = input("Enter tag:")
    from datetime import datetime
    notetime = datetime.now().strftime('%Y%m%d_%H%M%S')

    
    note1 = Note(notetime,input_date, input_tag,input_content )
    notebook1.add_note(note1)
    print ("note is added")
 
def search_note(notebook1):
    input_search = input("Enter word to search content:")
    
    notebook1.search_note(input_search)
    
 
def search_tag(notebook1):
    input_search = input("Enter TAG to search :")
    
    notebook1.search_tag(input_search)
     

def show_note(notebook1):
      
    notebook1.show_note()
    
def show_tag(notebook1):
    print ("Show All TAG")  
    notebook1.show_tag()
    
 
def load_from_file(filename):
    infile = open(filename, 'rb')
    data = pickle.load(infile)
    infile.close()
    return data
    
def save_to_file(filename,notebook1):
    outfile = open(filename, 'wb')
    pickle.dump(notebook1, outfile)
    outfile.close()    


def modify(notebook_def):
    input_noteid = input("Enter  Noteid you want to modify:")
    if notebook_def.search_noteid(input_noteid) == input_noteid:
        print ("found")
        input_date = input("Enter Modify Day : (dd/mm/yyyy):")
        input_content = input("Enter Modify note content:")
        input_tag = input("Enter Modify tag:")
        notebook_def.modify_note(input_noteid,input_date,input_tag ,input_content)
        
    else:
         print ("NoteID not Found")

def main():
    
    
    
    try:
        notebook1 = load_from_file('notebook.dat')
    except:
        print ("Can't load File")
        
    if notebook1 is None:
        print ("Empty File")
        notebook1 = Notebook()
    
    
    print('')
    showmenu()
    
    while True:
        input_option = input("Select option [0-6]   '0' for Menu:")
        if input_option == '0':
            showmenu()
        elif input_option == '1':
            add_note(notebook1)
        elif input_option == '2':
            show_note(notebook1)
        elif input_option == '3':
            show_tag(notebook1)
        elif input_option == '4':
            search_note(notebook1)
        elif input_option == '5':
            search_tag(notebook1)
        elif input_option == '6':
            modify(notebook1)
        elif input_option.upper() == '99':
            save_to_file('notebook.dat',notebook1)
            print ("Good Bye")
            break        
    
    


main()            
                