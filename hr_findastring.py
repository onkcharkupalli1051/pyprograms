# -*- coding: utf-8 -*-
"""
Created on Sun Nov 29 19:44:07 2020

@author: Onkar
"""

"""

HackerRank Logo
Find a string

165 more points to get your gold badge!
Rank: 175425|Points: 235/400
Python
Problem
Submissions
Leaderboard
Editorial
In this challenge, the user enters a string and a substring. You have to print the number of times that the substring occurs in the given string. String traversal will take place from left to right, not from right to left.

NOTE: String letters are case-sensitive.

Input Format

The first line of input contains the original string. The next line contains the substring.

Constraints


Each character in the string is an ascii character.

Output Format

Output the integer number indicating the total number of occurrences of the substring in the original string.

Sample Input

ABCDCDC
CDC
Sample Output

2
Concept

Some string processing examples, such as these, might be useful.
There are a couple of new concepts:
In Python, the length of a string is found by the function len(s), where  is the string.
To traverse through the length of a string, use a for loop:

for i in range(0, len(s)):
    print (s[i])
A range function is used to loop over some length:

range (0, 5)
Here, the range loops over  to .  is excluded.
"""

def count_substring(string, sub_string):
    count = 0
    ls = list(string)
    lss = list(sub_string)
    for i in range(len(ls)):
        if(lss == ls[i:i+len(lss)]):
            count+=1
    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    print(string)
    print(sub_string)
    count = count_substring(string, sub_string)
    print(count)