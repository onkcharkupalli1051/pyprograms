# -*- coding: utf-8 -*-
"""
Created on Mon Nov  2 16:11:19 2020

@author: Onkar
"""
from math import sqrt

class point:
    def __init__(self,a,b):
        self.x = a
        self.y = b
        
    def print(self):
        print("a :",self.x,"b :",self.y)
    
    def translate(self,deltax,deltay):
        self.x += deltax
        self.y += deltay
    
    def odistace(self):
        return(sqrt(self.x**2+self.y**2))
    
p = point(3,2)
p.print()

p.translate(5,5)
p.print()

y = p.odistace()
print("Distance of point from origin :{:.2f}".format(y))