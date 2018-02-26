# -*- coding: utf-8 -*-
"""
Created on Mon Feb 12 20:36:06 2018

@author: kronprom
"""


def main():
    infile = open("Mileage.txt","r")
    list_mileage = [line.rstrip().split(",") for line in infile]
    infile.close()
    
    
    list_unique_model = []
    for index,x in enumerate(list_mileage):
        if list_mileage[index][0] not in list_unique_model:
            list_unique_model.append(list_mileage[index][0])
    #print (list_unique_model)
    
    list_avg_gallons_per_100_mile = []
    for index_unique,x in enumerate(list_unique_model):
        #print (list_unique_model[index_unique])
        count_model = 0
        sum_model = 0
        for index_file,y in enumerate(list_mileage):
            
            if list_unique_model[index_unique] == list_mileage[index_file][0]:
                count_model += 1
                sum_model += float(list_mileage[index_file][1])
#                print (list_unique_model[index_unique])
#                print (list_mileage[index_file][1])
#                print (count_model)
#                print (sum_model)
        #list_avg_gallons_per_100_mile.append([list_unique_model[index_unique],round((count_model/sum_model),4)])
        list_avg_gallons_per_100_mile.append([list_unique_model[index_unique],round((sum_model/count_model),4)])
    
   
    

    print ("Model\t MPG\n")
     #Sorted by avg
    list_avg_gallons_per_100_mile.sort(key=lambda x:x[1])
    for index,value in enumerate(list_avg_gallons_per_100_mile):
        print ("{}\t{:.2f}".format(list_avg_gallons_per_100_mile[index][0],100/list_avg_gallons_per_100_mile[index][1]))
   
    
    
main()
