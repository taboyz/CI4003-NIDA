# -*- coding: utf-8 -*-
"""

@author: kronprom
"""

weight_input = input("Enter weight in KG:")
height_input = input("Enter height in M  (ex. 1.65):")

try:
    weight = float(weight_input)
    height = float(height_input)

except:
    weight = 1
    height = 1
    
bmi = weight / (height ** 2)

if bmi < 18.5:
    print (" Underweight")
elif bmi >= 18.5 and bmi < 25:
    print("Normal or Healthy Weight")
elif bmi >= 25 and bmi < 30:
    print("Overweight")
elif bmi >= 30:
    print ("Obese")