
# coding: utf-8

# # Week 1 Assignment (2018/1/10)# 
# by Kronprom Thirwat  6020411001
# 

# ---

# ### Assignment 1 :  จงเขียนโปรแกรมคำนวณหา  Speed โดยรับค่า Input ระยะทาง (Distance) และ เวลา (Time)   หน่วยตามใจชอบ###
#  **Given Formalar :**   Speed = Distance / Time

# In[1]:


distance = input('Please input Distance in kilometer:')
time = input('Please input Time in hour:')
speed = float(distance)/float(time)
print ("your speed is ",speed," Kilometres per hour")


# ---

# ### Assignment 2 :  จงเขียนโปรแกรมแปลงค่าอุณหภูมิจาก Celsius (°C) to Fahrenheit (°F)  โดย  รับค่าเป็น  Celsius
# 
# สูคร T(°F) = T(°C) × 1.8 + 32  **อ้างอิงจาก** https://www.rapidtables.com/convert/temperature/celsius-to-fahrenheit.html

# In[2]:


celsius = input("Please input Temperature in Celcuis (°C): ")
fahrenheit = float(celsius) * 1.8 + 32
print ("Result is : ",fahrenheit,"°F")


# ---
