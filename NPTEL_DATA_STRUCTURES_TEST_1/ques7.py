"""
Question 7
Write a Python program that reads input from the keyboard (standard input). The input will consist of some number of lines of text. The input will be terminated by a blank line. The first line will consist of a single word to be interpreted as a pattern, after discarding the new line character. Your program should print every line from the second line onward that contains an occurrence of the pattern. You can assume that the input will have a non-empty pattern line. Recall that for a string s and a pattern p, s.find(p) returns the first position in s where p occurs, and returns -1 if p does not occur in s.

For instance, if the input is the following:

the
"Spot the mistake
in the following argument",
Jack challenged
1+(-1+1)+(-1+1)+... = (1+ -1)+(1+ -1)+...
so therefore,
1 = 0
??

then your program should print the following. Note that the pattern string the is matched by the word therefore.

"Spot the mistake
in the following argument",
so therefore,
"""
a = input()
b =a
l =[]
while a != "":
    a = input()
    l.append(a)
for i in range(0,len(l)):
    if l[i].find(b) != -1:
        print(l[i])