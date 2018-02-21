# -*- coding: utf-8 -*-
"""
Created on Wed Feb  7 09:51:30 2018

@author: Pramote
"""
import rectangle

def main():
    rec1 = rectangle.Rectangle(10, 20)
    print(rec1)
    
    rec2 = rectangle.Rectangle(height=40, width=20)
    print(rec2)
    
    print('Width = ', rec1.get_width())
    print('Height = ', rec1.get_height())
    
    rec1.set_width(50)
    rec1.set_height(100)
    print(rec1)
    
    print('Area = ', rec1.get_area())
    
    
    
    
main()