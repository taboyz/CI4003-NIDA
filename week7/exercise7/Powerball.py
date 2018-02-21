# -*- coding: utf-8 -*-
"""
Created on Wed Feb 21 18:14:26 2018

@author: kronprom
"""

import random

whiteball_value_list = [x for x in range(1,61)]
powerball_value_list = [x for x in range(1,36)]


print ("White Balls: ", random.sample(whiteball_value_list,5))
print ("Powerball: ",random.choice(powerball_value_list))

