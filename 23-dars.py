# -*- coding: utf-8 -*-
"""
Created on Sat Nov  6 16:27:46 2021

@author: SAYFIDDIN
"""

# import math
# from math import pi
# x= 5
# print(math.sqrt(x))

# print(pow(5,5))


# print(pi)
# print(math.log2(8))
# print(math.log10(100))
# print(math.ceil(x))
# print(math.fabs(x))
# print(math.floor(x))
# print(math.cos(x))
# print(math.sin(x))
# print(math.tan(x))
# print(math.degrees(x))
# print(math.radians(x))
# print(math.e)

import random as r # random modulini r deb chaqirayapmiz

son = r.randint(0,100) # 0 va 100 oralig'ida tasodifiy son
print(son)

ismlar = ['olim','anvar','hasan','husan']
ism = r.choice(ismlar) # ismlar dan tasodifiy ism tanlaymiz
print(ism)
print(r.choice(ism)) # ismdan tasodifiy harf tanlaymiz

x = list(range(0,51,5))
print(x)
print(r.choice(x))

x = list(range(11))
print(x)
r.shuffle(x)
print(x)