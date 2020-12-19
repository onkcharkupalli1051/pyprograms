"""
A positive integer n is a sum of three squares if n = i2 + j2 + k2 for integers i,j,k such that i ≥ 1, j ≥ 1 and k ≥ 1. For instance, 29 is a sum of three squares because 10 = 22 + 32 + 42, and so is 6 (12 + 12 + 22). On the other hand, 16 and 20 are not sums of three squares.

Write a Python function sumof3squares(n) that takes a positive integer argument and returns True if the integer is a sum of three squares, and False otherwise.
"""

def sumof3squares(n):
    for i in range(n):
        for j in range(n):
            for k in range(n):
                if(n == i**2 + j**2 + k**2):
                    return True
    return False

print(sumof3squares(16))