# -*- coding: utf-8 -*-
"""
Created on Thu Feb  8 22:09:16 2018

@author: kronprom
"""
from dice import PairOfDice


def main():
    die2 = PairOfDice()
    count2 = 0
    count3 = 0
    count4 = 0
    count5 = 0
    count6 = 0
    count7 = 0
    count8 = 0
    count9 = 0
    count10 = 0
    count11 = 0
    count12 = 0
    experiment = 100000
    
    for i in range (1,experiment+1):
        die2.roll()
        score = die2.sum()
        #print (i,"=",score)
       
        if score == 2:
            count2 += 1
        elif score == 3:
            count3 += 1
        elif score == 4:
            count4 += 1
        elif score == 5:
            count5 += 1
        elif score == 6:
            count6 += 1
        elif score == 7:
            count7 += 1
        elif score == 8:
            count8 += 1
        elif score == 9:
            count9 += 1
        elif score == 10:
            count10 += 1
        elif score == 11:
            count11 += 1
        elif score == 12:
            count12 += 1
        else:
            print ("outlier")
            
 
#    print ("score 2 = ", count2,"==>",count2/experiment*100 ,"%")
#    print ("score 3 = ", count3,"==>",count3/experiment*100 ,"%")
#    print ("score 4 = ", count4,"==>",count4/experiment*100 ,"%")
#    print ("score 5 = ", count5,"==>",count5/experiment*100 ,"%")
#    print ("score 6 = ", count6,"==>",count6/experiment*100 ,"%")
#    print ("score 7 = ", count7,"==>",count7/experiment*100 ,"%")
#    print ("score 8 = ", count8,"==>",count8/experiment*100 ,"%")
#    print ("score 9 = ", count9,"==>",count9/experiment*100 ,"%")
#    print ("score 10 = ", count10,"==>",count10/experiment*100 ,"%")
#    print ("score 11 = ", count11,"==>",count11/experiment*100 ,"%")
#    print ("score 12 = ", count12,"==>",count12/experiment*100 ,"%")
#    
    print ("experiment: {0:,} times".format(experiment))
    print ("score 7 = {0:,} ==> {1:.2f}% prob stat {2:.2f}%".format(count7,count7/experiment*100,6/36*100))
    
    print ("===EXTra===")
    
    print ("score 2 = {0:,} ==> {1:.2f}% prob stat {2:.2f}%".format(count2,count2/experiment*100,1/36*100))
    print ("score 3 = {0:,} ==> {1:.2f}% prob stat {2:.2f}%".format(count3,count3/experiment*100,2/36*100))
    print ("score 4 = {0:,} ==> {1:.2f}% prob stat {2:.2f}%".format(count4,count4/experiment*100,3/36*100))
    print ("score 5 = {0:,} ==> {1:.2f}% prob stat {2:.2f}%".format(count5,count5/experiment*100,4/36*100))
    print ("score 6 = {0:,} ==> {1:.2f}% prob stat {2:.2f}%".format(count6,count6/experiment*100,5/36*100))
    print ("score 7 = {0:,} ==> {1:.2f}% prob stat {2:.2f}%".format(count7,count7/experiment*100,6/36*100))
    print ("score 8 = {0:,} ==> {1:.2f}% prob stat {2:.2f}%".format(count8,count8/experiment*100,5/36*100))
    print ("score 9 = {0:,} ==> {1:.2f}% prob stat {2:.2f}%".format(count9,count9/experiment*100,4/36*100))
    print ("score 10 = {0:,} ==> {1:.2f}% prob stat {2:.2f}%".format(count10,count10/experiment*100,3/36*100))
    print ("score 11 = {0:,} ==> {1:.2f}% prob stat {2:.2f}%".format(count11,count11/experiment*100,2/36*100))
    print ("score 12 = {0:,} ==> {1:.2f}% prob stat {2:.2f}%".format(count12,count12/experiment*100,1/36*100))
 
    
main()






