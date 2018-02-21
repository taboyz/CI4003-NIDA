# -*- coding: utf-8 -*-
"""
Created on Wed Jan 31 10:05:04 2018

@author: Pramote
"""

def main():
    infile = open('nums.txt')
    for line in infile:
        print(line.strip())
    infile.close()
    
    infile = open('nums.txt')
    nums = [int(line.strip()) for line in infile]
    print(nums)
    

main()