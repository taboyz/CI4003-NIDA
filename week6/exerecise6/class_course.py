# -*- coding: utf-8 -*-
"""
Created on Tue Feb 20 20:33:38 2018

@author: kronprom
"""

class Course:
    def __init__(self,course_name, student=[]):
        self._course_name = course_name
        self._student = []

    def add_student(self,student):
        self._student.append(student)
    
    def get_student(self):
#        students_list = ""
#        for i,v in enumerate(self._student):
#            
        return self._student
    
    def get_number_of_students(self):
        return len(self._student)
    
    def get_course_name(self):
        return self._course_name
    
    def drop_student(self, student):
        self._student.remove(student)
        return "done"
    def __str__(self):
        return self._course_name


    
def option2(course):
    print (course.get_course_name())    

def option3(course):
    input_student = input("Enter Student name : ")
    course.add_student(input_student)
    print ("{} added".format(input_student))
    
def option4(course):
    print (course.get_student())
        
def option5(course):
    print ("number of student in", course.get_course_name()," is ",course.get_number_of_students())     

def option6(course):
    print (course.get_student())
    input_student = input("Enter Student name to Drop : ")
    try :
        course.drop_student(input_student)
        print ("{} is Dropped out from {}".format(input_student,course.get_course_name()))
    except:
        print ("can't delete")
    
    
def show_menu():
    print ("1: show menu")
    print ("2: show course name")
    print ("3: Add Student")
    print ("4: List Student")
    print ("5: Get Number of Student")
    print ("6: drop Student")
    print ("0: Exit program")


    
def main():
    show_menu()
    is_quit = 'No'
    
    input_course = input("Enter Course name:")
    course1 = Course(input_course)
    
    while is_quit != "yes":
        input_option = input("Enter one of the option:")
        
        if input_option == "1":
            show_menu()
        elif input_option == "2":
            option2(course1)
        elif input_option == "3":
            option3(course1)
        elif input_option == "4":
            option4(course1)
        elif input_option == "5":
            option5(course1)
        elif input_option == "6":
            option6(course1)    
        elif input_option == "0":
            is_quit = "yes"
        else:
            print ("Sorry no Choice")
        
    print ("Bood Bye!!")            

    
    
    input
    



main()
    
    
    
    