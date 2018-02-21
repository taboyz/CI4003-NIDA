# -*- coding: utf-8 -*-
"""
Created on Wed Feb 14 11:26:43 2018

@author: kronprom
"""
class Student:
    def __init__(self, name='', midterm=0, final=0):
        self._name = name
        self._midterm = midterm
        self._final = final

    def get_name(self):
        return self._name
    
    def set_name(self,name):
        self._name = name
        
    def set_midterm(self,midterm):
        self._midterm = midterm
        
    def set_final(self, final):
        self._final = final
    
    def __str__(self):
        return f'{self._name} {self._midterm}{self._final}'
    
    
class LGStudent(Student):
    def __init__(self,name,midterm,final):
        super().__init__(name,midterm,final)
        
    def calc_semester_grade(self):
        average_grade = (self._midterm + self._final) /2
        if ((average_grade >= 90) and (average_grade < 100)):
            self._semester_grade = "A"
        elif ((average_grade >= 80) and (average_grade < 90)):
            self._semester_grade = "B"
        elif ((average_grade >= 70) and (average_grade < 80)):
            self._semester_grade = "C"
        elif ((average_grade >= 60) and (average_grade < 70)):
            self._semester_grade = "D"
        elif ((average_grade >= 0) and (average_grade < 60)):
            self._semester_grade = "F"
            
        return self._semester_grade

    def __str__(self):
        return f'{self._name} {self._semester_grade}'

class PFStudent(Student):
    def __init__(self,name="",midterm = 0,final = 0,full_time = True):
        super().__init__(name,midterm,final)
        self._full_time = full_time
        
        
    def set_full_time(self,full_time):
        self._full_time = full_time
        
    def get_full_time(self):
        return self._full_time
    
    def calc_semester_grade(self):
        average = (self._midterm + self._final)/2
        if average >= 60:
            return "Pass"
        else:
            return "Fail"
    def __str__(self):
        return super().__str__() + str(self._full_time)
    
    
def main():
 
    student_list = [] 
    is_countinue = "Y"
    while is_countinue.upper() != "N":
        input_name = input("Enter Student's name:")
        input_midterm = float(input("Enter Student's grade on midterm exam:"))
        input_final = float(input("Enter Student's grade on final exam:"))
        input_cat = input("LG or PF:")
        if input_cat.upper() == "LG":
            lg1 = LGStudent(input_name,input_midterm,input_final)   
            student_list.append(lg1)
        elif input_cat.upper() == "PF":
            input_fulltime = input("Are you a full-time student(Y/N)?")
            if input_fulltime.upper() == "Y":
                full_time = True
            elif input_fulltime.upper() == "N":
                full_time = False
              
            pf1 = PFStudent(input_name,input_midterm,input_final,full_time)
            student_list.append(pf1)
        input_continue = input("Do you want to continue (Y/N)?")
        if (input_continue.upper() == "N"):
            is_countinue = "N"
       
    ### Print Table
    print("Name\tGRADE\tSTATUS\n")
    student_list.sort(key=lambda x: x.get_name())   ## Sort List object by name
    for val in student_list:
        if type(val) == LGStudent:
            print (val.get_name() ,"\t",val.calc_semester_grade(),"\t")
        elif type(val) == PFStudent:
            if val.get_full_time() is True:
                status = "Fulltime Student"
            else:
                status = "Part-time Student"
            print (val.get_name() ,"\t",val.calc_semester_grade(),"\t",status)
        
        
    
main()    
                
        
