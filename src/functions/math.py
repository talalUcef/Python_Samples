'''
Created on 2 août 2015

@author: talalUcef
'''

import math

print("Math module :"+str(math))

radians = 0.7
height = math.sin(radians)
print("Height "+ str(height))

degrees = 45
radians = degrees / 360.0 * 2 * math.pi
print(str(math.sin(radians)))

print("Sqrt of 2 "+ str(math.sqrt(2) / 2.0))
