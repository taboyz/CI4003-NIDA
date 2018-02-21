# -*- coding: utf-8 -*-
"""
Created on Wed Feb 14 09:04:36 2018

@author: Pramote
"""

class Person:
    def __init__(self, citizen_id, firstname, lastname):
        self._citizen_id = citizen_id
        self._firstname = firstname
        self._lastname = lastname
    
    def get_citizen_id(self):
        return self._citizen_id
    
    def get_firstname(self):
        return self._firstname
    
    def get_lastname(self):
        return self._lastname
    
    def set_citizen_id(self, citizen_id):
        self._citizen_id = citizen_id
        
    def set_firstname(self, firstname):
        self._firstname = firstname
    
    def set_lastname(self, lastname):
        self._lastname = lastname
    
    def __str__(self):
        return f'{self._citizen_id} {self._firstname} {self._lastname}'
    
class Employee(Person):
    def __init__(self, citizen_id, firstname, lastname, salary):
        super().__init__(citizen_id, firstname, lastname)
        self._salary = salary
        
    def get_salary(self):
        return self._salary
    
    def raise_salary(self, percentage):
        self._salary *= (1 + percentage/100)
        
    def __str__(self):
        return super().__str__() + f' {self._salary:.2f}'
    
    
    
def main():
    person = Person(111111, 'John', 'Doe')
    print(person)
    person.set_firstname('Jane')
    print(person)
    
    emp1 = Employee(222222, 'James', 'Rose', 100000)
    print(emp1)
    emp1.raise_salary(10)
    print(emp1)
    
    emp1.set_firstname('David')
    print(emp1)
    
main()
    
    