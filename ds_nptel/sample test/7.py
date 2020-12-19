"""
Question 7
Write a Python program that reads input from the
keyboard (standard input). The input will consist
of some number of lines of text. The input will be
terminated by a blank line. Your program should print
 every third line.

For instance, if the input is the following:

"Spot the mistake
in the following argument",
Jack challenged
1+(-1+1)+(-1+1)+... = (1+ -1)+(1+ -1)+...
so therefore,
1 = 0
??

then the output should be:

Jack challenged
1 = 0
"""

li = []
for _ in range(100):
    str = input()
    if str == "":
        break
    else:
        li.append(str)

print(li[2::3])