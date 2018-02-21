# -*- coding: utf-8 -*-
"""
Created on Tue Feb 14 06:05:53 2017

@author: Pramote
"""

class Rational:
    def __init__(self, numerator = 1, denominator = 1):
        divisor = gcd(numerator, denominator)
        self._numerator = numerator // divisor
        self._denominator = denominator // divisor
        
    def __add__(self, r2):
        n = self._numerator * r2[1] + self._denominator * r2[0]
        d = self._denominator * r2[1]
        return Rational(n, d)
    
    def __sub__(self, r2):
        n = self._numerator * r2[1] - self._denominator * r2[0]
        d = self._denominator * r2[1]
        return Rational(n, d)
    
    def __mul__(self, r2):
        n = self._numerator * r2[0]
        d = self._denominator * r2[1]
        return Rational(n, d)
    
    def __truediv__(self, r2):
        n = self._numerator * r2[1]
        d = self._denominator * r2[0]
        return Rational(n, d)
    
    def __float__(self):
        return self._numerator / self._denominator
    
    def __int__(self):
        return int(self.__float__())

    def __getitem__(self, index):
        return self._numerator if index==0 else self._denominator
    
    def __lt__(self, r2):
        return self.__cmp__(r2) < 0

    def __le__(self, r2):
        return self.__cmp__(r2) <= 0

    def __gt__(self, r2):
        return self.__cmp__(r2) > 0

    def __ge__(self, r2):
        return self.__cmp__(r2) >= 0    
    
    def __cmp__(self, r2):
        tmp = self.__sub__(r2)
        if tmp[0] > 0:
            return 1
        elif tmp[0] < 0:
            return -1
        else:
            return 0
        
    def __str__(self):
        return str(self._numerator) if self._denominator==1 else str(self._numerator) + '/' + str(self._denominator)
    

def gcd(a, b):

    while b != 0:
        t = b
        b = a % b
        a = t
    return a
#  a, b = b, a%b
    
r1 = Rational(2, 3)
r2 = Rational(1, 3)
r3 = Rational(-1, -5)
r4 = Rational(-3, 4)
r5 = Rational(3, -4)

print(r1-r2)
print(r2-r1)
print(r3)
print (r4)
print(r5)
print(r4 > r5)