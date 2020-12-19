# -*- coding: utf-8 -*-
"""
Created on Tue Nov  3 14:25:10 2020

@author: Onkar
"""

class node:
    def __init__(self,initval = None):
        self.value = initval
        self.next = None
        
    def isempty(self):
        return(self.value == None)
    
l1 = node()

l2 = node(5)

x = l1.isempty() #returns True

y = l2.isempty() #returns False

print(x,"\n",y)