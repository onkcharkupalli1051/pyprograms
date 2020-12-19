# -*- coding: utf-8 -*-
"""
Created on Mon Nov  2 16:42:46 2020

@author: Onkar
"""
from math import *

class point():
    def __init__(self,a=0,b=0):
        self.r = sqrt(a**2 + b**2)
        if a == 0:
            self.theta = 0
        else:
            self.theta = atan(b/a)
    
    def __str__(self):
        return("(" + str(self.r) + "," + str(self.theta) + ")")
        
    def odistance(self):
        return(self.r)
    
    def translate(self,deltax,deltay):
        pass
    
    def __add__(self,new):
        #invoked when + is used
        return(point(self.r+new.r))
    
    def pri(self):
        print("R : {:.2f} Theta : {:.2f}".format(self.r,self.theta))
    

p = point(5,5)

p.pri()

y = p.__str__()
print("Y :",y)
print("add : ",)
