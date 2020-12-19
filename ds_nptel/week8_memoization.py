"""
memoization : Compute a problem and store the result in table:
              If the same problem has to be computed again, don't do it,
              look for
              the result in the table for the program

fib(5)

k     #fib(k)
1       1
0       0
2       1
3       2
4       3
"""

def fib(n):
    if fibtable[n]:
        return fibtable[n]
    if n == 0 or n == 1:
        value = n
    else:
        value = fibtable(n-1) or fibtable(n-2)
    fibtable[n] = value
    return value

fib(5)