# -*- coding: utf-8 -*-
"""
Created on Thu Feb  8 20:10:27 2018

@author: kronprom
"""
class Quizzes:
    def __init__(self, scores):
        self._scores = scores
    
    def get_score(self):
        return self._scores
    
    def average(self):
        list_score = self._scores.split(",")
        list_score = [int(i) for i in list_score]
        lowest_score = min(list_score)
        while lowest_score in list_score:
            list_score.remove(lowest_score)
        
        average_score_drop_lowest = sum(list_score)/len(list_score)
        return average_score_drop_lowest
        
    
    def __str__(self):
#        list_score = self._scores.split(",")
#        list_score = [int(i) for i in list_score]
#        average_score = sum(list_score)/len(list_score)
        return str(self.average())
    
    
    
    
def main():
    input_scores = input("Enter Scores separated by ,:")
    scores1 = Quizzes(input_scores)
    
    print ("Average by Dropping the lowset quiz scores:",scores1.average())
    print (scores1)

    
main()
    