# -*- coding: utf-8 -*-
"""
Created on Wed Dec  9 20:09:38 2020

@author: Onkar
"""

"""
Objective
Today, we're learning about a new data type: sets.

Concept

If the inputs are given on one line separated by a space character, use split() to get the separate values in the form of a list:

>> a = raw_input()
5 4 3 2
>> lis = a.split()
>> print (lis)
['5', '4', '3', '2']
If the list values are all integer types, use the map() method to convert all the strings to integers.

>> newlis = list(map(int, lis))
>> print (newlis)
[5, 4, 3, 2]
Sets are an unordered bag of unique values. A single set contains values of any immutable data type.

CREATING SETS

>> myset = {1, 2} # Directly assigning values to a set
>> myset = set()  # Initializing a set
>> myset = set(['a', 'b']) # Creating a set from a list
>> myset
{'a', 'b'}
"""
m = int(input())
M = set(list(map(int, input().split())))
n = int(input())
N = set(list(map(int, input().split())))

mli = list(M.difference(N))
print(mli)
nli = list(N.difference(M))
li = mli+nli
print(sorted(li))