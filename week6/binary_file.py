# -*- coding: utf-8 -*-
"""
Created on Fri Feb  9 12:55:12 2018

@author: Pramote
"""

import pickle

def write_file(filename, data):
    outfile = open(filename, 'wb')
    pickle.dump(data, outfile)
    outfile.close()

def read_file(filename):
    infile = open(filename, 'rb')
    data = pickle.load(infile)
    infile.close()
    return data

def main():
    data = [2, 3, 4, 5, 9, 8, 7, 6]
    write_file('numbers.dat', data)
    data2 = read_file('numbers.dat')
    print(data2)

main()
